"""Runs a formula's solve function for one target variable.

A formula's solve functions raise ValueError for an out-of-domain input
(negative sqrt, non-integer factorial, no real solution, ...) — that
message is passed straight through to the caller.

Python and JavaScript disagree on a few arithmetic edge cases that the
original formulas relied on: dividing by zero raises ZeroDivisionError
in Python instead of returning Infinity, and very large `**`/`exp` results
raise OverflowError instead of returning Infinity. Both are treated the
same way JS's `!Number.isFinite(result)` check treated them.
"""

import math

from ..models.formula import Formula


class SolveError(Exception):
    """A clean, user-facing calculation error."""


def solve(formula: Formula, target: str, values: dict[str, float]) -> float:
    solver = formula.solve.get(target)
    if solver is None:
        raise SolveError(f"This formula can't be solved for {target} directly.")

    required = [v.symbol for v in formula.variables if v.symbol != target]
    missing = [s for s in required if s not in values]
    if missing:
        raise SolveError(f"Missing value(s) for: {', '.join(missing)}.")

    try:
        result = solver({s: values[s] for s in required})
    except (ZeroDivisionError, OverflowError):
        raise SolveError("Result is undefined — check for division by zero.")
    except ValueError as e:
        raise SolveError(str(e) or "Could not compute a result for these inputs.")
    except Exception:
        # Anything else (a coding mistake in a solve function, not a domain
        # error) still shouldn't surface as a raw 500 to the frontend.
        raise SolveError("Could not compute a result for these inputs.")

    if isinstance(result, complex) or not math.isfinite(result):
        raise SolveError("Result is undefined — check for division by zero.")

    return result
