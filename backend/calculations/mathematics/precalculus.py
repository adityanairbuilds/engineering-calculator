"""Precalculus formulas: exponential growth/decay, logarithms, parabolas."""

import math

from ...models.formula import Formula, Variable

PRECALCULUS_FORMULAS: list[Formula] = []


def _exponential_growth_k(v: dict[str, float]) -> float:
    if v["A"] <= 0 or v["A0"] <= 0:
        raise ValueError("Amounts must be positive.")
    return math.log(v["A"] / v["A0"]) / v["t"]


def _exponential_growth_t(v: dict[str, float]) -> float:
    if v["A"] <= 0 or v["A0"] <= 0:
        raise ValueError("Amounts must be positive.")
    return math.log(v["A"] / v["A0"]) / v["k"]


PRECALCULUS_FORMULAS.append(
    Formula(
        id="exponential-growth",
        name="Exponential Growth/Decay",
        category="Mathematics",
        subcategory="Precalculus",
        equation="A = A₀e^(kt)",
        description="Models exponential growth (k > 0) or decay (k < 0) over time.",
        variables=[
            Variable("A", "Final amount", "dimensionless"),
            Variable("A0", "Initial amount", "dimensionless"),
            Variable("k", "Growth/decay constant", "per unit time"),
            Variable("t", "Time", "dimensionless"),
        ],
        keywords=["exponential growth", "exponential decay", "population growth", "half life"],
        solve={
            "A": lambda v: v["A0"] * math.exp(v["k"] * v["t"]),
            "A0": lambda v: v["A"] / math.exp(v["k"] * v["t"]),
            "k": _exponential_growth_k,
            "t": _exponential_growth_t,
        },
    )
)


def _logarithm_y(v: dict[str, float]) -> float:
    if v["x"] <= 0:
        raise ValueError("The argument x must be positive.")
    if v["b"] <= 0 or v["b"] == 1:
        raise ValueError("The base must be positive and not equal to 1.")
    return math.log(v["x"]) / math.log(v["b"])


def _logarithm_x(v: dict[str, float]) -> float:
    if v["b"] <= 0:
        raise ValueError("The base must be positive.")
    return v["b"] ** v["y"]


def _logarithm_b(v: dict[str, float]) -> float:
    if v["x"] <= 0:
        raise ValueError("The argument x must be positive.")
    if v["y"] == 0:
        raise ValueError("y cannot be 0 — the base cannot be determined.")
    return v["x"] ** (1 / v["y"])


PRECALCULUS_FORMULAS.append(
    Formula(
        id="logarithm",
        name="Logarithm (General Base)",
        category="Mathematics",
        subcategory="Precalculus",
        equation="y = log_b(x)  ⇔  b^y = x",
        description="Converts between exponential and logarithmic form for an arbitrary base b.",
        variables=[
            Variable("y", "Logarithm result", "dimensionless"),
            Variable("b", "Base", "dimensionless"),
            Variable("x", "Argument", "dimensionless"),
        ],
        keywords=["logarithm", "log base", "exponent inverse", "log rules"],
        solve={
            "y": _logarithm_y,
            "x": _logarithm_x,
            "b": _logarithm_b,
        },
    )
)


def _natural_logarithm_y(v: dict[str, float]) -> float:
    if v["x"] <= 0:
        raise ValueError("x must be positive.")
    return math.log(v["x"])


PRECALCULUS_FORMULAS.append(
    Formula(
        id="natural-logarithm",
        name="Natural Logarithm",
        category="Mathematics",
        subcategory="Precalculus",
        equation="y = ln(x)",
        description="Logarithm with base e (Euler’s number).",
        variables=[
            Variable("y", "ln(x)", "dimensionless"),
            Variable("x", "Input value", "dimensionless"),
        ],
        keywords=["natural logarithm", "ln", "e", "exponential", "inverse"],
        solve={
            "y": _natural_logarithm_y,
            "x": lambda v: math.exp(v["y"]),
        },
    )
)


def _vertex_form_x(v: dict[str, float]) -> float:
    ratio = (v["y"] - v["k"]) / v["a"]
    if ratio < 0:
        raise ValueError("No real solution — negative value under the square root.")
    return v["h"] + math.sqrt(ratio)


def _vertex_form_h(v: dict[str, float]) -> float:
    ratio = (v["y"] - v["k"]) / v["a"]
    if ratio < 0:
        raise ValueError("No real solution — negative value under the square root.")
    return v["x"] - math.sqrt(ratio)


PRECALCULUS_FORMULAS.append(
    Formula(
        id="vertex-form-parabola",
        name="Vertex Form of a Parabola",
        category="Mathematics",
        subcategory="Precalculus",
        equation="y = a(x − h)² + k",
        description="Describes a parabola from its vertex (h, k) and stretch factor a. Solving for x or h gives the principal (positive-offset) root.",
        variables=[
            Variable("y", "y", "dimensionless"),
            Variable("a", "Stretch/direction factor", "dimensionless"),
            Variable("h", "Vertex x-coordinate", "dimensionless"),
            Variable("k", "Vertex y-coordinate", "dimensionless"),
            Variable("x", "x", "dimensionless"),
        ],
        keywords=["vertex form", "parabola", "quadratic transformation", "function transformation"],
        solve={
            "y": lambda v: v["a"] * (v["x"] - v["h"]) ** 2 + v["k"],
            "a": lambda v: (v["y"] - v["k"]) / (v["x"] - v["h"]) ** 2,
            "k": lambda v: v["y"] - v["a"] * (v["x"] - v["h"]) ** 2,
            "x": _vertex_form_x,
            "h": _vertex_form_h,
        },
    )
)


def _continuous_growth_r(v: dict[str, float]) -> float:
    if v["A"] <= 0 or v["P"] <= 0:
        raise ValueError("Amounts must be positive.")
    return math.log(v["A"] / v["P"]) / v["t"]


def _continuous_growth_t(v: dict[str, float]) -> float:
    if v["A"] <= 0 or v["P"] <= 0:
        raise ValueError("Amounts must be positive.")
    return math.log(v["A"] / v["P"]) / v["r"]


PRECALCULUS_FORMULAS.append(
    Formula(
        id="continuous-compounding-growth",
        name="Continuous Exponential Growth",
        category="Mathematics",
        subcategory="Precalculus",
        equation="A = Pe^(rt)",
        description="Models continuous growth, such as interest compounded continuously.",
        variables=[
            Variable("A", "Final amount", "dimensionless"),
            Variable("P", "Initial amount", "dimensionless"),
            Variable("r", "Continuous growth rate", "per unit time"),
            Variable("t", "Time", "dimensionless"),
        ],
        keywords=[
            "continuous compounding",
            "exponential model",
            "continuous growth",
            "pert",
            "logarithmic model",
        ],
        solve={
            "A": lambda v: v["P"] * math.exp(v["r"] * v["t"]),
            "P": lambda v: v["A"] / math.exp(v["r"] * v["t"]),
            "r": _continuous_growth_r,
            "t": _continuous_growth_t,
        },
    )
)
