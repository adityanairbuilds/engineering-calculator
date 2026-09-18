"""Algebra formulas: lines, quadratics, sequences and series, finance."""

import math

from ...models.formula import Formula, Variable

ALGEBRA_FORMULAS: list[Formula] = []


def _slope_m(v: dict[str, float]) -> float:
    if v["x2"] == v["x1"]:
        raise ValueError("The line is vertical — slope is undefined.")
    return (v["y2"] - v["y1"]) / (v["x2"] - v["x1"])


ALGEBRA_FORMULAS.append(
    Formula(
        id="slope-between-two-points",
        name="Slope",
        category="Mathematics",
        subcategory="Algebra",
        equation="m = (y₂ − y₁) / (x₂ − x₁)",
        description="Finds the slope of a line through two points.",
        variables=[
            Variable("m", "Slope", "dimensionless"),
            Variable("x1", "x of point 1", "dimensionless"),
            Variable("y1", "y of point 1", "dimensionless"),
            Variable("x2", "x of point 2", "dimensionless"),
            Variable("y2", "y of point 2", "dimensionless"),
        ],
        keywords=["slope", "gradient", "line", "rise over run"],
        solve={"m": _slope_m},
    )
)

ALGEBRA_FORMULAS.append(
    Formula(
        id="distance-formula-2d",
        name="Distance Formula",
        category="Mathematics",
        subcategory="Algebra",
        equation="d = √((x₂ − x₁)² + (y₂ − y₁)²)",
        description="Finds the straight-line distance between two points on a plane.",
        variables=[
            Variable("d", "Distance", "dimensionless"),
            Variable("x1", "x of point 1", "dimensionless"),
            Variable("y1", "y of point 1", "dimensionless"),
            Variable("x2", "x of point 2", "dimensionless"),
            Variable("y2", "y of point 2", "dimensionless"),
        ],
        keywords=["distance", "two points", "coordinate geometry"],
        solve={"d": lambda v: math.sqrt((v["x2"] - v["x1"]) ** 2 + (v["y2"] - v["y1"]) ** 2)},
    )
)

ALGEBRA_FORMULAS.append(
    Formula(
        id="midpoint-formula",
        name="Midpoint Formula",
        category="Mathematics",
        subcategory="Algebra",
        equation="M = ((x₁ + x₂) / 2, (y₁ + y₂) / 2)",
        description="Finds the x-coordinate of the midpoint between two points (solve again with x and y swapped for Mᵧ).",
        variables=[
            Variable("Mx", "Midpoint x", "dimensionless"),
            Variable("x1", "x of point 1", "dimensionless"),
            Variable("x2", "x of point 2", "dimensionless"),
        ],
        keywords=["midpoint", "coordinate geometry", "center point"],
        solve={"Mx": lambda v: (v["x1"] + v["x2"]) / 2},
    )
)


def _quadratic_x(v: dict[str, float]) -> float:
    if v["a"] == 0:
        raise ValueError("a cannot be 0 — this would not be a quadratic equation.")
    discriminant = v["b"] ** 2 - 4 * v["a"] * v["c"]
    if discriminant < 0:
        raise ValueError("Negative discriminant — no real roots.")
    return (-v["b"] + math.sqrt(discriminant)) / (2 * v["a"])


ALGEBRA_FORMULAS.append(
    Formula(
        id="quadratic-formula",
        name="Quadratic Formula",
        category="Mathematics",
        subcategory="Algebra",
        equation="x = (−b + √(b² − 4ac)) / 2a",
        description="Solves ax² + bx + c = 0 for the larger root. For the second root, flip the sign in front of the square root by hand.",
        variables=[
            Variable("x", "Root", "dimensionless"),
            Variable("a", "Quadratic coefficient", "dimensionless"),
            Variable("b", "Linear coefficient", "dimensionless"),
            Variable("c", "Constant term", "dimensionless"),
        ],
        keywords=["quadratic", "roots", "parabola", "ax^2+bx+c"],
        solve={"x": _quadratic_x},
    )
)

ALGEBRA_FORMULAS.append(
    Formula(
        id="arithmetic-sequence-nth-term",
        name="Arithmetic Sequence (nth Term)",
        category="Mathematics",
        subcategory="Algebra",
        equation="aₙ = a₁ + (n − 1)d",
        description="Finds the nth term of an arithmetic sequence.",
        variables=[
            Variable("an", "nth term", "dimensionless"),
            Variable("a1", "First term", "dimensionless"),
            Variable("n", "Term number", "dimensionless"),
            Variable("d", "Common difference", "dimensionless"),
        ],
        keywords=["arithmetic sequence", "nth term", "common difference"],
        solve={"an": lambda v: v["a1"] + (v["n"] - 1) * v["d"]},
    )
)

ALGEBRA_FORMULAS.append(
    Formula(
        id="geometric-sequence-nth-term",
        name="Geometric Sequence (nth Term)",
        category="Mathematics",
        subcategory="Algebra",
        equation="aₙ = a₁ · r^(n − 1)",
        description="Finds the nth term of a geometric sequence.",
        variables=[
            Variable("an", "nth term", "dimensionless"),
            Variable("a1", "First term", "dimensionless"),
            Variable("r", "Common ratio", "dimensionless"),
            Variable("n", "Term number", "dimensionless"),
        ],
        keywords=["geometric sequence", "nth term", "common ratio"],
        solve={"an": lambda v: v["a1"] * v["r"] ** (v["n"] - 1)},
    )
)


def _compound_interest_t(v: dict[str, float]) -> float:
    if v["P"] <= 0 or v["A"] <= 0:
        raise ValueError("Amounts must be positive.")
    return math.log(v["A"] / v["P"]) / (v["n"] * math.log(1 + v["r"] / v["n"]))


def _compound_interest_r(v: dict[str, float]) -> float:
    if v["P"] <= 0 or v["A"] <= 0:
        raise ValueError("Amounts must be positive.")
    return v["n"] * ((v["A"] / v["P"]) ** (1 / (v["n"] * v["t"])) - 1)


ALGEBRA_FORMULAS.append(
    Formula(
        id="compound-interest",
        name="Compound Interest",
        category="Mathematics",
        subcategory="Algebra",
        equation="A = P(1 + r/n)^(nt)",
        description="Calculates the future value of an investment earning compound interest.",
        variables=[
            Variable("A", "Final amount", "$"),
            Variable("P", "Principal (initial amount)", "$"),
            Variable("r", "Annual interest rate (decimal, e.g. 0.05 for 5%)", "dimensionless"),
            Variable("n", "Compounding periods per year", "dimensionless"),
            Variable("t", "Time", "years"),
        ],
        keywords=["compound interest", "investment", "finance", "future value", "principal"],
        solve={
            "A": lambda v: v["P"] * (1 + v["r"] / v["n"]) ** (v["n"] * v["t"]),
            "P": lambda v: v["A"] / (1 + v["r"] / v["n"]) ** (v["n"] * v["t"]),
            "t": _compound_interest_t,
            "r": _compound_interest_r,
        },
    )
)

ALGEBRA_FORMULAS.append(
    Formula(
        id="exponent-product-rule",
        name="Product of Powers Rule",
        category="Mathematics",
        subcategory="Algebra",
        equation="aᵐ · aⁿ = a^(m + n)",
        description="Multiplies two powers with the same base by adding their exponents.",
        variables=[
            Variable("result", "Product, a^(m+n)", "dimensionless"),
            Variable("a", "Base", "dimensionless"),
            Variable("m", "First exponent", "dimensionless"),
            Variable("n", "Second exponent", "dimensionless"),
        ],
        keywords=["exponent rules", "product of powers", "multiplying exponents", "laws of exponents"],
        solve={"result": lambda v: v["a"] ** (v["m"] + v["n"])},
    )
)

ALGEBRA_FORMULAS.append(
    Formula(
        id="exponent-power-rule",
        name="Power of a Power Rule",
        category="Mathematics",
        subcategory="Algebra",
        equation="(aᵐ)ⁿ = a^(mn)",
        description="Raises a power to another power by multiplying the exponents.",
        variables=[
            Variable("result", "Result, a^(mn)", "dimensionless"),
            Variable("a", "Base", "dimensionless"),
            Variable("m", "Inner exponent", "dimensionless"),
            Variable("n", "Outer exponent", "dimensionless"),
        ],
        keywords=["exponent rules", "power of a power", "laws of exponents"],
        solve={"result": lambda v: (v["a"] ** v["m"]) ** v["n"]},
    )
)

ALGEBRA_FORMULAS.append(
    Formula(
        id="exponent-quotient-rule",
        name="Quotient of Powers Rule",
        category="Mathematics",
        subcategory="Algebra",
        equation="aᵐ / aⁿ = a^(m − n)",
        description="Divides two powers with the same base by subtracting their exponents.",
        variables=[
            Variable("result", "Quotient, a^(m−n)", "dimensionless"),
            Variable("a", "Base", "dimensionless"),
            Variable("m", "Numerator exponent", "dimensionless"),
            Variable("n", "Denominator exponent", "dimensionless"),
        ],
        keywords=["exponent rules", "quotient of powers", "dividing exponents", "laws of exponents"],
        solve={"result": lambda v: v["a"] ** v["m"] / v["a"] ** v["n"]},
    )
)

ALGEBRA_FORMULAS.append(
    Formula(
        id="arithmetic-series-sum",
        name="Arithmetic Series Sum",
        category="Mathematics",
        subcategory="Algebra",
        equation="Sₙ = n(a₁ + aₙ) / 2",
        description="Sums the first n terms of an arithmetic sequence.",
        variables=[
            Variable("S", "Sum of n terms", "dimensionless"),
            Variable("n", "Number of terms", "dimensionless"),
            Variable("a1", "First term", "dimensionless"),
            Variable("an", "Last (nth) term", "dimensionless"),
        ],
        keywords=["arithmetic series", "sum of sequence", "partial sum", "series"],
        solve={
            "S": lambda v: (v["n"] * (v["a1"] + v["an"])) / 2,
            "n": lambda v: (2 * v["S"]) / (v["a1"] + v["an"]),
            "a1": lambda v: (2 * v["S"]) / v["n"] - v["an"],
            "an": lambda v: (2 * v["S"]) / v["n"] - v["a1"],
        },
    )
)

ALGEBRA_FORMULAS.append(
    Formula(
        id="geometric-series-sum",
        name="Geometric Series Sum",
        category="Mathematics",
        subcategory="Algebra",
        equation="Sₙ = a₁(1 − rⁿ) / (1 − r)",
        description="Sums the first n terms of a geometric sequence (r ≠ 1).",
        variables=[
            Variable("S", "Sum of n terms", "dimensionless"),
            Variable("a1", "First term", "dimensionless"),
            Variable("r", "Common ratio", "dimensionless"),
            Variable("n", "Number of terms", "dimensionless"),
        ],
        keywords=["geometric series", "sum of sequence", "partial sum", "common ratio", "series"],
        solve={
            "S": lambda v: (v["a1"] * (1 - v["r"] ** v["n"])) / (1 - v["r"]),
            "a1": lambda v: (v["S"] * (1 - v["r"])) / (1 - v["r"] ** v["n"]),
        },
    )
)

ALGEBRA_FORMULAS.append(
    Formula(
        id="point-slope-form",
        name="Point-Slope Form of a Line",
        category="Mathematics",
        subcategory="Algebra",
        equation="y − y₁ = m(x − x₁)",
        description="Writes the equation of a line given its slope and one point on the line.",
        variables=[
            Variable("y", "y", "dimensionless"),
            Variable("y1", "y of known point", "dimensionless"),
            Variable("m", "Slope", "dimensionless"),
            Variable("x", "x", "dimensionless"),
            Variable("x1", "x of known point", "dimensionless"),
        ],
        keywords=["point slope form", "line equation", "linear equation", "slope"],
        solve={
            "y": lambda v: v["y1"] + v["m"] * (v["x"] - v["x1"]),
            "m": lambda v: (v["y"] - v["y1"]) / (v["x"] - v["x1"]),
            "y1": lambda v: v["y"] - v["m"] * (v["x"] - v["x1"]),
            "x1": lambda v: v["x"] - (v["y"] - v["y1"]) / v["m"],
            "x": lambda v: v["x1"] + (v["y"] - v["y1"]) / v["m"],
        },
    )
)

ALGEBRA_FORMULAS.append(
    Formula(
        id="percent-change",
        name="Percent Change",
        category="Mathematics",
        subcategory="Algebra",
        equation="%Δ = ((new − old) / old) × 100",
        description="Calculates the percentage increase or decrease from an old value to a new value.",
        variables=[
            Variable("percentChange", "Percent change", "%"),
            Variable("oldValue", "Old value", "dimensionless"),
            Variable("newValue", "New value", "dimensionless"),
        ],
        keywords=["percent change", "percentage increase", "percentage decrease", "percent difference"],
        solve={
            "percentChange": lambda v: ((v["newValue"] - v["oldValue"]) / v["oldValue"]) * 100,
            "newValue": lambda v: v["oldValue"] * (1 + v["percentChange"] / 100),
            "oldValue": lambda v: v["newValue"] / (1 + v["percentChange"] / 100),
        },
    )
)
