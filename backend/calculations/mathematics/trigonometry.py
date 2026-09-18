"""Trigonometry formulas: right-triangle ratios, laws of sines/cosines, inverse trig."""

import math

from ...models.formula import Formula, Variable

TRIGONOMETRY_FORMULAS: list[Formula] = []

TRIGONOMETRY_FORMULAS.append(
    Formula(
        id="sine-ratio-right-triangle",
        name="Sine Ratio (Right Triangle)",
        category="Mathematics",
        subcategory="Trigonometry",
        equation="sin(θ) = opposite / hypotenuse",
        description="Defines the sine of an acute angle in a right triangle (SOH).",
        variables=[
            Variable("sinTheta", "sin(θ)", "dimensionless"),
            Variable("opposite", "Opposite side", "dimensionless"),
            Variable("hypotenuse", "Hypotenuse", "dimensionless"),
        ],
        keywords=["sine", "soh cah toa", "right triangle", "trig ratio"],
        solve={
            "sinTheta": lambda v: v["opposite"] / v["hypotenuse"],
            "opposite": lambda v: v["sinTheta"] * v["hypotenuse"],
            "hypotenuse": lambda v: v["opposite"] / v["sinTheta"],
        },
    )
)

TRIGONOMETRY_FORMULAS.append(
    Formula(
        id="cosine-ratio-right-triangle",
        name="Cosine Ratio (Right Triangle)",
        category="Mathematics",
        subcategory="Trigonometry",
        equation="cos(θ) = adjacent / hypotenuse",
        description="Defines the cosine of an acute angle in a right triangle (CAH).",
        variables=[
            Variable("cosTheta", "cos(θ)", "dimensionless"),
            Variable("adjacent", "Adjacent side", "dimensionless"),
            Variable("hypotenuse", "Hypotenuse", "dimensionless"),
        ],
        keywords=["cosine", "soh cah toa", "right triangle", "trig ratio"],
        solve={
            "cosTheta": lambda v: v["adjacent"] / v["hypotenuse"],
            "adjacent": lambda v: v["cosTheta"] * v["hypotenuse"],
            "hypotenuse": lambda v: v["adjacent"] / v["cosTheta"],
        },
    )
)

TRIGONOMETRY_FORMULAS.append(
    Formula(
        id="tangent-ratio-right-triangle",
        name="Tangent Ratio (Right Triangle)",
        category="Mathematics",
        subcategory="Trigonometry",
        equation="tan(θ) = opposite / adjacent",
        description="Defines the tangent of an acute angle in a right triangle (TOA).",
        variables=[
            Variable("tanTheta", "tan(θ)", "dimensionless"),
            Variable("opposite", "Opposite side", "dimensionless"),
            Variable("adjacent", "Adjacent side", "dimensionless"),
        ],
        keywords=["tangent", "soh cah toa", "right triangle", "trig ratio"],
        solve={
            "tanTheta": lambda v: v["opposite"] / v["adjacent"],
            "opposite": lambda v: v["tanTheta"] * v["adjacent"],
            "adjacent": lambda v: v["opposite"] / v["tanTheta"],
        },
    )
)


def _law_of_sines_A(v: dict[str, float]) -> float:
    s = (v["a"] * math.sin(math.radians(v["B"]))) / v["b"]
    if s < -1 or s > 1:
        raise ValueError("No valid angle exists for these inputs.")
    return math.degrees(math.asin(s))


def _law_of_sines_B(v: dict[str, float]) -> float:
    s = (v["b"] * math.sin(math.radians(v["A"]))) / v["a"]
    if s < -1 or s > 1:
        raise ValueError("No valid angle exists for these inputs.")
    return math.degrees(math.asin(s))


TRIGONOMETRY_FORMULAS.append(
    Formula(
        id="law-of-sines",
        name="Law of Sines",
        category="Mathematics",
        subcategory="Trigonometry",
        equation="a / sin(A) = b / sin(B)",
        description="Relates two side–angle pairs of any triangle. Angles are in degrees.",
        variables=[
            Variable("a", "Side a", "dimensionless"),
            Variable("A", "Angle opposite side a", "degrees"),
            Variable("b", "Side b", "dimensionless"),
            Variable("B", "Angle opposite side b", "degrees"),
        ],
        keywords=["law of sines", "triangle", "sine rule", "oblique triangle"],
        solve={
            "a": lambda v: (v["b"] * math.sin(math.radians(v["A"]))) / math.sin(math.radians(v["B"])),
            "b": lambda v: (v["a"] * math.sin(math.radians(v["B"]))) / math.sin(math.radians(v["A"])),
            "A": _law_of_sines_A,
            "B": _law_of_sines_B,
        },
    )
)


def _law_of_cosines_c(v: dict[str, float]) -> float:
    val = v["a"] ** 2 + v["b"] ** 2 - 2 * v["a"] * v["b"] * math.cos(math.radians(v["C"]))
    if val < 0:
        raise ValueError("No real solution — check that the inputs form a valid triangle.")
    return math.sqrt(val)


def _law_of_cosines_C(v: dict[str, float]) -> float:
    cos_c = (v["a"] ** 2 + v["b"] ** 2 - v["c"] ** 2) / (2 * v["a"] * v["b"])
    if cos_c < -1 or cos_c > 1:
        raise ValueError("These side lengths cannot form a triangle.")
    return math.degrees(math.acos(cos_c))


TRIGONOMETRY_FORMULAS.append(
    Formula(
        id="law-of-cosines",
        name="Law of Cosines",
        category="Mathematics",
        subcategory="Trigonometry",
        equation="c² = a² + b² − 2ab·cos(C)",
        description="Relates the three sides of a triangle to the angle opposite one of them. Angle is in degrees.",
        variables=[
            Variable("c", "Side c", "dimensionless"),
            Variable("a", "Side a", "dimensionless"),
            Variable("b", "Side b", "dimensionless"),
            Variable("C", "Angle opposite side c", "degrees"),
        ],
        keywords=["law of cosines", "triangle", "cosine rule", "oblique triangle"],
        solve={
            "c": _law_of_cosines_c,
            "C": _law_of_cosines_C,
        },
    )
)


def _arcsin_theta(v: dict[str, float]) -> float:
    if v["x"] < -1 or v["x"] > 1:
        raise ValueError("x must be between −1 and 1 for arcsine to be defined.")
    return math.degrees(math.asin(v["x"]))


TRIGONOMETRY_FORMULAS.append(
    Formula(
        id="inverse-sine-arcsin",
        name="Inverse Sine (Arcsine)",
        category="Mathematics",
        subcategory="Trigonometry",
        equation="θ = sin⁻¹(x)",
        description="Finds the angle whose sine is x (principal value, in degrees).",
        variables=[
            Variable("theta", "Angle θ", "degrees"),
            Variable("x", "Ratio (opposite/hypotenuse)", "dimensionless"),
        ],
        keywords=["arcsine", "inverse sine", "arcsin", "solve for angle"],
        solve={
            "theta": _arcsin_theta,
            "x": lambda v: math.sin(math.radians(v["theta"])),
        },
    )
)


def _arccos_theta(v: dict[str, float]) -> float:
    if v["x"] < -1 or v["x"] > 1:
        raise ValueError("x must be between −1 and 1 for arccosine to be defined.")
    return math.degrees(math.acos(v["x"]))


TRIGONOMETRY_FORMULAS.append(
    Formula(
        id="inverse-cosine-arccos",
        name="Inverse Cosine (Arccosine)",
        category="Mathematics",
        subcategory="Trigonometry",
        equation="θ = cos⁻¹(x)",
        description="Finds the angle whose cosine is x (principal value, in degrees).",
        variables=[
            Variable("theta", "Angle θ", "degrees"),
            Variable("x", "Ratio (adjacent/hypotenuse)", "dimensionless"),
        ],
        keywords=["arccosine", "inverse cosine", "arccos", "solve for angle"],
        solve={
            "theta": _arccos_theta,
            "x": lambda v: math.cos(math.radians(v["theta"])),
        },
    )
)

TRIGONOMETRY_FORMULAS.append(
    Formula(
        id="inverse-tangent-arctan",
        name="Inverse Tangent (Arctangent)",
        category="Mathematics",
        subcategory="Trigonometry",
        equation="θ = tan⁻¹(x)",
        description="Finds the angle whose tangent is x (principal value, in degrees).",
        variables=[
            Variable("theta", "Angle θ", "degrees"),
            Variable("x", "Ratio (opposite/adjacent)", "dimensionless"),
        ],
        keywords=["arctangent", "inverse tangent", "arctan", "solve for angle"],
        solve={
            "theta": lambda v: math.degrees(math.atan(v["x"])),
            "x": lambda v: math.tan(math.radians(v["theta"])),
        },
    )
)

TRIGONOMETRY_FORMULAS.append(
    Formula(
        id="degrees-radians-conversion",
        name="Degrees–Radians Conversion",
        category="Mathematics",
        subcategory="Trigonometry",
        equation="rad = deg × (π / 180)",
        description="Converts an angle between degrees and radians.",
        variables=[
            Variable("rad", "Angle in radians", "radians"),
            Variable("deg", "Angle in degrees", "degrees"),
        ],
        keywords=["degrees to radians", "radians to degrees", "angle conversion", "radian measure"],
        solve={
            "rad": lambda v: math.radians(v["deg"]),
            "deg": lambda v: math.degrees(v["rad"]),
        },
    )
)


def _pythagorean_identity_sin(v: dict[str, float]) -> float:
    if v["cosTheta"] < -1 or v["cosTheta"] > 1:
        raise ValueError("cos(θ) must be between −1 and 1.")
    return math.sqrt(1 - v["cosTheta"] ** 2)


def _pythagorean_identity_cos(v: dict[str, float]) -> float:
    if v["sinTheta"] < -1 or v["sinTheta"] > 1:
        raise ValueError("sin(θ) must be between −1 and 1.")
    return math.sqrt(1 - v["sinTheta"] ** 2)


TRIGONOMETRY_FORMULAS.append(
    Formula(
        id="pythagorean-trig-identity",
        name="Pythagorean Identity",
        category="Mathematics",
        subcategory="Trigonometry",
        equation="sin²θ + cos²θ = 1",
        description="Fundamental trig identity relating the sine and cosine of the same angle (principal, non-negative root shown).",
        variables=[
            Variable("sinTheta", "sin(θ)", "dimensionless"),
            Variable("cosTheta", "cos(θ)", "dimensionless"),
        ],
        keywords=["pythagorean identity", "trig identity", "sin squared cos squared", "unit circle"],
        solve={
            "sinTheta": _pythagorean_identity_sin,
            "cosTheta": _pythagorean_identity_cos,
        },
    )
)
