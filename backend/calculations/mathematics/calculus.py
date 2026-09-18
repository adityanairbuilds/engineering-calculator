"""Calculus formulas: derivatives, integrals, and rates of change."""

import math

from ...models.formula import Formula, Variable

CALCULUS_FORMULAS: list[Formula] = []

CALCULUS_FORMULAS.append(
    Formula(
        id="limit-definition-derivative",
        name="Derivative (Limit Definition)",
        category="Mathematics",
        subcategory="Calculus",
        equation="f'(x) = lim(h→0) [f(x+h) − f(x)] / h",
        description="Defines the derivative of f at x as the limit of its average rate of change as h approaches 0. Symbolic — plug in an explicit function to evaluate numerically.",
        variables=[
            Variable("fPrime", "f'(x) — derivative", "dimensionless"),
            Variable("fx", "f(x) — function value at x", "dimensionless"),
            Variable("h", "Δx — small change in x", "dimensionless"),
        ],
        keywords=["derivative", "limit definition", "difference quotient", "rate of change"],
        solve={},
    )
)

CALCULUS_FORMULAS.append(
    Formula(
        id="power-rule",
        name="Power Rule (Derivative)",
        category="Mathematics",
        subcategory="Calculus",
        equation="d/dx[xⁿ] = n·x^(n − 1)",
        description="Gives the derivative of xⁿ, evaluated at a specific point x.",
        variables=[
            Variable("derivative", "Derivative value at x", "dimensionless"),
            Variable("n", "Exponent", "dimensionless"),
            Variable("x", "Point of evaluation", "dimensionless"),
        ],
        keywords=["power rule", "derivative", "calculus"],
        solve={
            "derivative": lambda v: v["n"] * v["x"] ** (v["n"] - 1),
        },
    )
)

CALCULUS_FORMULAS.append(
    Formula(
        id="chain-rule",
        name="Chain Rule (Derivative)",
        category="Mathematics",
        subcategory="Calculus",
        equation="d/dx[f(g(x))] = f'(g(x)) · g'(x)",
        description="Derivative of a composite function, given the outer derivative evaluated at g(x) and the inner derivative.",
        variables=[
            Variable("result", "d/dx[f(g(x))]", "dimensionless"),
            Variable("fPrimeOfG", "f'(g(x)) — outer derivative at g(x)", "dimensionless"),
            Variable("gPrime", "g'(x) — inner derivative", "dimensionless"),
        ],
        keywords=["chain rule", "derivative", "calculus", "composite function"],
        solve={
            "result": lambda v: v["fPrimeOfG"] * v["gPrime"],
            "fPrimeOfG": lambda v: v["result"] / v["gPrime"],
            "gPrime": lambda v: v["result"] / v["fPrimeOfG"],
        },
    )
)

CALCULUS_FORMULAS.append(
    Formula(
        id="definite-integral",
        name="Fundamental Theorem of Calculus",
        category="Mathematics",
        subcategory="Calculus",
        equation="∫ₐᵇ f(x)dx = F(b) − F(a)",
        description="Evaluates a definite integral from an antiderivative F evaluated at the bounds.",
        variables=[
            Variable("integral", "Definite integral value", "dimensionless"),
            Variable("Fb", "F(b) — antiderivative at upper bound", "dimensionless"),
            Variable("Fa", "F(a) — antiderivative at lower bound", "dimensionless"),
        ],
        keywords=["fundamental theorem of calculus", "definite integral", "antiderivative"],
        solve={
            "integral": lambda v: v["Fb"] - v["Fa"],
            "Fb": lambda v: v["integral"] + v["Fa"],
            "Fa": lambda v: v["Fb"] - v["integral"],
        },
    )
)

CALCULUS_FORMULAS.append(
    Formula(
        id="product-rule",
        name="Product Rule (Derivative)",
        category="Mathematics",
        subcategory="Calculus",
        equation="(fg)' = f'g + fg'",
        description="Derivative of a product of two functions, given their values and derivatives at a point.",
        variables=[
            Variable("result", "(fg)' — derivative of the product", "dimensionless"),
            Variable("f", "f(x)", "dimensionless"),
            Variable("fPrime", "f'(x)", "dimensionless"),
            Variable("g", "g(x)", "dimensionless"),
            Variable("gPrime", "g'(x)", "dimensionless"),
        ],
        keywords=["product rule", "derivative", "calculus"],
        solve={
            "result": lambda v: v["fPrime"] * v["g"] + v["f"] * v["gPrime"],
            "fPrime": lambda v: (v["result"] - v["f"] * v["gPrime"]) / v["g"],
            "gPrime": lambda v: (v["result"] - v["fPrime"] * v["g"]) / v["f"],
        },
    )
)

CALCULUS_FORMULAS.append(
    Formula(
        id="quotient-rule",
        name="Quotient Rule (Derivative)",
        category="Mathematics",
        subcategory="Calculus",
        equation="(f/g)' = (f'g − fg') / g²",
        description="Derivative of a quotient of two functions, given their values and derivatives at a point.",
        variables=[
            Variable("result", "(f/g)' — derivative of the quotient", "dimensionless"),
            Variable("f", "f(x)", "dimensionless"),
            Variable("fPrime", "f'(x)", "dimensionless"),
            Variable("g", "g(x)", "dimensionless"),
            Variable("gPrime", "g'(x)", "dimensionless"),
        ],
        keywords=["quotient rule", "derivative", "calculus"],
        solve={
            "result": lambda v: (v["fPrime"] * v["g"] - v["f"] * v["gPrime"]) / v["g"] ** 2,
            "fPrime": lambda v: (v["result"] * v["g"] ** 2 + v["f"] * v["gPrime"]) / v["g"],
            "gPrime": lambda v: (v["fPrime"] * v["g"] - v["result"] * v["g"] ** 2) / v["f"],
        },
    )
)

CALCULUS_FORMULAS.append(
    Formula(
        id="derivative-of-sine",
        name="Derivative of Sine",
        category="Mathematics",
        subcategory="Calculus",
        equation="d/dx[sin x] = cos x",
        description="Derivative of sin(x), evaluated at a point x (in radians).",
        variables=[
            Variable("derivative", "Derivative value at x", "dimensionless"),
            Variable("x", "Point of evaluation", "radians"),
        ],
        keywords=["derivative of sine", "d/dx sin x", "trig derivative", "common derivatives"],
        solve={
            "derivative": lambda v: math.cos(v["x"]),
        },
    )
)


def _derivative_of_exponential_x(v: dict[str, float]) -> float:
    if v["derivative"] <= 0:
        raise ValueError("The derivative of eˣ is always positive.")
    return math.log(v["derivative"])


CALCULUS_FORMULAS.append(
    Formula(
        id="derivative-of-exponential",
        name="Derivative of eˣ",
        category="Mathematics",
        subcategory="Calculus",
        equation="d/dx[eˣ] = eˣ",
        description="Derivative of the natural exponential function, evaluated at a point x.",
        variables=[
            Variable("derivative", "Derivative value at x", "dimensionless"),
            Variable("x", "Point of evaluation", "dimensionless"),
        ],
        keywords=["derivative of exponential", "d/dx e^x", "common derivatives"],
        solve={
            "derivative": lambda v: math.exp(v["x"]),
            "x": _derivative_of_exponential_x,
        },
    )
)


def _derivative_of_ln(v: dict[str, float]) -> float:
    if v["x"] <= 0:
        raise ValueError("x must be positive since ln(x) is only defined for x > 0.")
    return 1 / v["x"]


def _derivative_of_ln_x(v: dict[str, float]) -> float:
    if v["derivative"] <= 0:
        raise ValueError("The derivative of ln(x) is always positive since x > 0.")
    return 1 / v["derivative"]


CALCULUS_FORMULAS.append(
    Formula(
        id="derivative-of-natural-log",
        name="Derivative of ln(x)",
        category="Mathematics",
        subcategory="Calculus",
        equation="d/dx[ln x] = 1/x",
        description="Derivative of the natural logarithm, evaluated at a point x > 0.",
        variables=[
            Variable("derivative", "Derivative value at x", "dimensionless"),
            Variable("x", "Point of evaluation", "dimensionless"),
        ],
        keywords=["derivative of natural log", "d/dx ln x", "common derivatives"],
        solve={
            "derivative": _derivative_of_ln,
            "x": _derivative_of_ln_x,
        },
    )
)

CALCULUS_FORMULAS.append(
    Formula(
        id="integral-power-rule",
        name="Power Rule (Integral)",
        category="Mathematics",
        subcategory="Calculus",
        equation="∫xⁿ dx = x^(n+1)/(n+1) + C   (n ≠ −1)",
        description="Antiderivative of a power function. Symbolic — produces a function of x plus an arbitrary constant, not a single value.",
        variables=[
            Variable("n", "Exponent", "dimensionless"),
            Variable("x", "Variable", "dimensionless"),
        ],
        keywords=["integral power rule", "antiderivative", "indefinite integral", "common integrals"],
        solve={},
    )
)

CALCULUS_FORMULAS.append(
    Formula(
        id="integral-of-exponential",
        name="Integral of eˣ",
        category="Mathematics",
        subcategory="Calculus",
        equation="∫eˣ dx = eˣ + C",
        description="Antiderivative of the natural exponential function. Symbolic — produces a function plus an arbitrary constant.",
        variables=[Variable("x", "Variable", "dimensionless")],
        keywords=["integral of exponential", "antiderivative", "indefinite integral", "common integrals"],
        solve={},
    )
)

CALCULUS_FORMULAS.append(
    Formula(
        id="integral-of-reciprocal",
        name="Integral of 1/x",
        category="Mathematics",
        subcategory="Calculus",
        equation="∫(1/x) dx = ln|x| + C   (x ≠ 0)",
        description="Antiderivative of 1/x. Symbolic — produces a function plus an arbitrary constant.",
        variables=[Variable("x", "Variable", "dimensionless")],
        keywords=["integral of reciprocal", "antiderivative", "indefinite integral", "common integrals"],
        solve={},
    )
)

CALCULUS_FORMULAS.append(
    Formula(
        id="average-rate-of-change",
        name="Average Rate of Change",
        category="Mathematics",
        subcategory="Calculus",
        equation="(f(b) − f(a)) / (b − a)",
        description="Calculates the average rate of change of a function over an interval [a, b] (the slope of the secant line).",
        variables=[
            Variable("avgRate", "Average rate of change", "dimensionless"),
            Variable("fb", "f(b)", "dimensionless"),
            Variable("fa", "f(a)", "dimensionless"),
            Variable("a", "a", "dimensionless"),
            Variable("b", "b", "dimensionless"),
        ],
        keywords=["average rate of change", "secant slope", "difference quotient"],
        solve={
            "avgRate": lambda v: (v["fb"] - v["fa"]) / (v["b"] - v["a"]),
            "fb": lambda v: v["avgRate"] * (v["b"] - v["a"]) + v["fa"],
            "fa": lambda v: v["fb"] - v["avgRate"] * (v["b"] - v["a"]),
            "a": lambda v: v["b"] - (v["fb"] - v["fa"]) / v["avgRate"],
            "b": lambda v: v["a"] + (v["fb"] - v["fa"]) / v["avgRate"],
        },
    )
)
