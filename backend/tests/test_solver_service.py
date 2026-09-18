import pytest

from backend.models.formula import Formula, Variable
from backend.services.solver_service import SolveError, solve

# A small fixture formula — F = m*a — independent of the real formula
# registry, so these tests check the solver's own behavior (missing
# values, bad targets, error translation) rather than any one formula's
# math.
_FORCE_FORMULA = Formula(
    id="test-force",
    name="Test Force",
    category="Physics",
    subcategory="Dynamics",
    equation="F = ma",
    description="",
    variables=[Variable("F", "Force", "N"), Variable("m", "Mass", "kg"), Variable("a", "Acceleration", "m/s^2")],
    keywords=[],
    solve={
        "F": lambda v: v["m"] * v["a"],
        "m": lambda v: v["F"] / v["a"],
        "a": lambda v: v["F"] / v["m"],
    },
)


def test_solve_success():
    assert solve(_FORCE_FORMULA, "F", {"m": 2, "a": 3}) == 6


def test_solve_unknown_target():
    with pytest.raises(SolveError, match="can't be solved for"):
        solve(_FORCE_FORMULA, "torque", {"m": 2, "a": 3})


def test_solve_missing_values():
    with pytest.raises(SolveError, match="Missing value"):
        solve(_FORCE_FORMULA, "F", {"m": 2})


def test_solve_division_by_zero_becomes_clean_error():
    with pytest.raises(SolveError, match="undefined"):
        solve(_FORCE_FORMULA, "m", {"F": 10, "a": 0})


def _sqrt_y(v: dict[str, float]) -> float:
    if v["y"] < 0:
        raise ValueError("y must be non-negative")
    return v["y"] ** 0.5


def test_solve_domain_value_error_passes_through():
    guarded = Formula(
        id="test-guarded",
        name="Guarded",
        category="Physics",
        subcategory="Dynamics",
        equation="x = sqrt(y)",
        description="",
        variables=[Variable("x", "x", ""), Variable("y", "y", "")],
        keywords=[],
        solve={"x": _sqrt_y},
    )
    with pytest.raises(SolveError, match="y must be non-negative"):
        solve(guarded, "x", {"y": -1})


def test_solve_extra_values_are_ignored():
    # Only the variables the formula actually declares are passed through —
    # a caller sending stray extra keys shouldn't break anything.
    assert solve(_FORCE_FORMULA, "F", {"m": 2, "a": 3, "unrelated": 99}) == 6


def _typo(v: dict[str, float]) -> float:
    return v["masss"] * v["a"]  # a bug: wrong key, not a domain error


def test_solve_non_valueerror_bug_still_becomes_clean_error():
    # A coding mistake in a solve function (KeyError, TypeError, ...) must
    # not leak past solve() as a raw exception — the API layer only knows
    # how to turn a SolveError into a clean 400.
    buggy = Formula(
        id="test-buggy",
        name="Buggy",
        category="Physics",
        subcategory="Dynamics",
        equation="F = ma",
        description="",
        variables=[Variable("F", "Force", "N"), Variable("m", "Mass", "kg"), Variable("a", "Acceleration", "m/s^2")],
        keywords=[],
        solve={"F": _typo},
    )
    with pytest.raises(SolveError):
        solve(buggy, "F", {"m": 2, "a": 3})
