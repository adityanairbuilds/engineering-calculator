from backend.models.formula import Formula, Variable
from backend.services.search_service import search_formulas

_FORMULAS = [
    Formula(
        id="ohms-law",
        name="Ohm's Law",
        category="Physics",
        subcategory="Circuits",
        equation="V = IR",
        description="Relates voltage, current, and resistance.",
        variables=[Variable("V", "Voltage", "V"), Variable("I", "Current", "A"), Variable("R", "Resistance", "Ω")],
        keywords=["ohm's law", "resistance", "voltage", "current", "electric resistance"],
        solve={"V": lambda v: v["I"] * v["R"]},
    ),
    Formula(
        id="newtons-second-law",
        name="Newton's Second Law",
        category="Physics",
        subcategory="Dynamics",
        equation="F = ma",
        description="Calculates net force.",
        variables=[Variable("F", "Force", "N"), Variable("m", "Mass", "kg"), Variable("a", "Acceleration", "m/s^2")],
        keywords=["force", "mass", "acceleration", "newton", "f=ma"],
        solve={"F": lambda v: v["m"] * v["a"]},
    ),
]


def test_empty_query_returns_nothing():
    assert search_formulas(_FORMULAS, "") == []
    assert search_formulas(_FORMULAS, "   ") == []


def test_exact_name_match_ranks_first():
    results = search_formulas(_FORMULAS, "ohm's law")
    assert results[0].id == "ohms-law"


def test_equation_query_matches():
    results = search_formulas(_FORMULAS, "F=ma")
    assert [f.id for f in results] == ["newtons-second-law"]


def test_keyword_alias_matches_unrelated_name():
    # "electric resistance" doesn't appear in the name "Ohm's Law", only
    # in a keyword — this is the case the multi-word token scoring exists for.
    results = search_formulas(_FORMULAS, "electric resistance")
    assert results[0].id == "ohms-law"


def test_no_match_returns_empty():
    assert search_formulas(_FORMULAS, "quantum chromodynamics") == []
