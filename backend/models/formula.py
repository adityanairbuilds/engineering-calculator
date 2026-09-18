"""Internal formula representation.

This mirrors the frontend's TypeScript `Formula`/`Variable` types
(src/types/index.ts), with one difference: `solve` holds real Python
functions, not JSON-serializable data. The API layer never returns a
`Formula` directly — see schemas/formula.py for the response shape.
"""

from collections.abc import Callable
from dataclasses import dataclass, field

# A solve function computes one variable from the values of all the others.
# It may raise ValueError for an out-of-domain input (negative sqrt,
# non-integer factorial, no real solution, etc.) — that message is shown
# to the user as-is.
SolveFn = Callable[[dict[str, float]], float]


@dataclass(frozen=True)
class Variable:
    symbol: str
    name: str
    unit: str


# eq=False: variables/keywords/solve aren't hashable, so the default value-based
# __eq__/__hash__ dataclass would generate here would crash the moment a Formula is
# hashed. Identity equality is fine — code compares formulas by `.id`, never by `==`.
@dataclass(frozen=True, eq=False)
class Formula:
    id: str
    name: str
    category: str
    subcategory: str
    equation: str
    description: str
    variables: list[Variable]
    keywords: list[str]
    solve: dict[str, SolveFn] = field(default_factory=dict)
