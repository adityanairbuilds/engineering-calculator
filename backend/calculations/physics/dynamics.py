"""Dynamics formulas: force, weight, friction, tension."""

import math

from ...models.formula import Formula, Variable

DYNAMICS_FORMULAS: list[Formula] = []

DYNAMICS_FORMULAS.append(
    Formula(
        id="newtons-second-law",
        name="Newton's Second Law",
        category="Physics",
        subcategory="Dynamics",
        equation="F = ma",
        description="Calculates the net force on an object from its mass and acceleration.",
        variables=[
            Variable("F", "Force", "N"),
            Variable("m", "Mass", "kg"),
            Variable("a", "Acceleration", "m/s²"),
        ],
        keywords=["force", "mass", "acceleration", "newton", "newton's second law", "f=ma"],
        solve={
            "F": lambda v: v["m"] * v["a"],
            "m": lambda v: v["F"] / v["a"],
            "a": lambda v: v["F"] / v["m"],
        },
    )
)

DYNAMICS_FORMULAS.append(
    Formula(
        id="weight",
        name="Weight",
        category="Physics",
        subcategory="Dynamics",
        equation="W = mg",
        description="Calculates the gravitational force (weight) on a mass.",
        variables=[
            Variable("W", "Weight", "N"),
            Variable("m", "Mass", "kg"),
            Variable("g", "Gravitational acceleration", "m/s²"),
        ],
        keywords=["weight", "gravity", "gravitational force"],
        solve={
            "W": lambda v: v["m"] * v["g"],
            "m": lambda v: v["W"] / v["g"],
            "g": lambda v: v["W"] / v["m"],
        },
    )
)

DYNAMICS_FORMULAS.append(
    Formula(
        id="friction-force",
        name="Friction Force",
        category="Physics",
        subcategory="Dynamics",
        equation="f = μN",
        description="Calculates the friction force from the coefficient of friction and the normal force.",
        variables=[
            Variable("f", "Friction force", "N"),
            Variable("mu", "Coefficient of friction", "dimensionless"),
            Variable("N", "Normal force", "N"),
        ],
        keywords=["friction", "coefficient of friction", "normal force"],
        solve={
            "f": lambda v: v["mu"] * v["N"],
            "mu": lambda v: v["f"] / v["N"],
            "N": lambda v: v["f"] / v["mu"],
        },
    )
)

DYNAMICS_FORMULAS.append(
    Formula(
        id="force-components-horizontal",
        name="Force Component (Horizontal)",
        category="Physics",
        subcategory="Dynamics",
        equation="Fₓ = F cos(θ)",
        description="Finds the horizontal component of a force applied at an angle from horizontal.",
        variables=[
            Variable("Fx", "Horizontal component", "N"),
            Variable("F", "Force magnitude", "N"),
            Variable("theta", "Angle from horizontal", "°"),
        ],
        keywords=["force components", "horizontal force", "vector components"],
        solve={
            "Fx": lambda v: v["F"] * math.cos((v["theta"] * math.pi) / 180),
        },
    )
)

DYNAMICS_FORMULAS.append(
    Formula(
        id="tension-pulley",
        name="Tension in an Atwood Machine",
        category="Physics",
        subcategory="Dynamics",
        equation="T = 2m₁m₂g / (m₁ + m₂)",
        description="Calculates the string tension for two masses connected over a frictionless, massless pulley (Atwood machine).",
        variables=[
            Variable("T", "Tension", "N"),
            Variable("m1", "Mass 1", "kg"),
            Variable("m2", "Mass 2", "kg"),
            Variable("g", "Gravitational acceleration", "m/s²"),
        ],
        keywords=["tension", "pulley", "atwood machine", "dynamics", "force", "mass"],
        solve={
            "T": lambda v: (2 * v["m1"] * v["m2"] * v["g"]) / (v["m1"] + v["m2"]),
            "m1": lambda v: (v["T"] * v["m2"]) / (2 * v["m2"] * v["g"] - v["T"]),
            "m2": lambda v: (v["T"] * v["m1"]) / (2 * v["m1"] * v["g"] - v["T"]),
            "g": lambda v: (v["T"] * (v["m1"] + v["m2"])) / (2 * v["m1"] * v["m2"]),
        },
    )
)
