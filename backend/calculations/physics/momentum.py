"""Momentum formulas: momentum, impulse, collisions."""

from ...models.formula import Formula, Variable

MOMENTUM_FORMULAS: list[Formula] = []

MOMENTUM_FORMULAS.append(
    Formula(
        id="momentum",
        name="Momentum",
        category="Physics",
        subcategory="Momentum",
        equation="p = mv",
        description="Calculates linear momentum from mass and velocity.",
        variables=[
            Variable("p", "Momentum", "kg·m/s"),
            Variable("m", "Mass", "kg"),
            Variable("v", "Velocity", "m/s"),
        ],
        keywords=["momentum", "mass", "velocity", "collision", "physics"],
        solve={
            "p": lambda v: v["m"] * v["v"],
            "m": lambda v: v["p"] / v["v"],
            "v": lambda v: v["p"] / v["m"],
        },
    )
)

MOMENTUM_FORMULAS.append(
    Formula(
        id="impulse",
        name="Impulse",
        category="Physics",
        subcategory="Momentum",
        equation="J = FΔt",
        description="Calculates impulse from a force applied over a time interval. Impulse equals the resulting change in momentum.",
        variables=[
            Variable("J", "Impulse", "N·s"),
            Variable("F", "Force", "N"),
            Variable("dt", "Time interval", "s"),
        ],
        keywords=["impulse", "momentum", "force", "time", "collision", "change in momentum"],
        solve={
            "J": lambda v: v["F"] * v["dt"],
            "F": lambda v: v["J"] / v["dt"],
            "dt": lambda v: v["J"] / v["F"],
        },
    )
)

MOMENTUM_FORMULAS.append(
    Formula(
        id="conservation-momentum",
        name="Conservation of Momentum (Perfectly Inelastic Collision)",
        category="Physics",
        subcategory="Momentum",
        equation="m₁v₁ + m₂v₂ = (m₁ + m₂)v_f",
        description="Models a perfectly inelastic collision where two objects stick together and move with a common final velocity.",
        variables=[
            Variable("m1", "Mass 1", "kg"),
            Variable("m2", "Mass 2", "kg"),
            Variable("v1", "Initial velocity of mass 1", "m/s"),
            Variable("v2", "Initial velocity of mass 2", "m/s"),
            Variable("vf", "Common final velocity", "m/s"),
        ],
        keywords=["conservation of momentum", "momentum", "collision", "inelastic", "sticking collision"],
        solve={
            "vf": lambda v: (v["m1"] * v["v1"] + v["m2"] * v["v2"]) / (v["m1"] + v["m2"]),
            "m1": lambda v: (v["m2"] * (v["vf"] - v["v2"])) / (v["v1"] - v["vf"]),
            "m2": lambda v: (v["m1"] * (v["vf"] - v["v1"])) / (v["v2"] - v["vf"]),
            "v1": lambda v: ((v["m1"] + v["m2"]) * v["vf"] - v["m2"] * v["v2"]) / v["m1"],
            "v2": lambda v: ((v["m1"] + v["m2"]) * v["vf"] - v["m1"] * v["v1"]) / v["m2"],
        },
    )
)

MOMENTUM_FORMULAS.append(
    Formula(
        id="elastic-collision-1d",
        name="Elastic Collision (1D)",
        category="Physics",
        subcategory="Momentum",
        equation="v₁' = ((m₁-m₂)v₁ + 2m₂v₂)/(m₁+m₂)  ,  v₂' = ((m₂-m₁)v₂ + 2m₁v₁)/(m₁+m₂)",
        description="Calculates the final velocities of two objects after a perfectly elastic head-on collision (kinetic energy conserved).",
        variables=[
            Variable("m1", "Mass 1", "kg"),
            Variable("m2", "Mass 2", "kg"),
            Variable("v1", "Initial velocity of mass 1", "m/s"),
            Variable("v2", "Initial velocity of mass 2", "m/s"),
            Variable("v1f", "Final velocity of mass 1", "m/s"),
            Variable("v2f", "Final velocity of mass 2", "m/s"),
        ],
        keywords=["elastic collision", "momentum", "kinetic energy", "collision", "final velocity"],
        solve={
            "v1f": lambda v: ((v["m1"] - v["m2"]) * v["v1"] + 2 * v["m2"] * v["v2"]) / (v["m1"] + v["m2"]),
            "v2f": lambda v: ((v["m2"] - v["m1"]) * v["v2"] + 2 * v["m1"] * v["v1"]) / (v["m1"] + v["m2"]),
        },
    )
)

MOMENTUM_FORMULAS.append(
    Formula(
        id="coefficient-of-restitution",
        name="Coefficient of Restitution",
        category="Physics",
        subcategory="Momentum",
        equation="e = (v₂f - v₁f) / (v₁ - v₂)",
        description="Calculates the coefficient of restitution, the ratio of relative separation speed to relative approach speed for a collision (1 = perfectly elastic, 0 = perfectly inelastic).",
        variables=[
            Variable("e", "Coefficient of restitution", "dimensionless"),
            Variable("v1", "Initial velocity of object 1", "m/s"),
            Variable("v2", "Initial velocity of object 2", "m/s"),
            Variable("v1f", "Final velocity of object 1", "m/s"),
            Variable("v2f", "Final velocity of object 2", "m/s"),
        ],
        keywords=["coefficient of restitution", "collision", "elastic", "inelastic", "bounce"],
        solve={
            "e": lambda v: (v["v2f"] - v["v1f"]) / (v["v1"] - v["v2"]),
            "v1f": lambda v: v["v2f"] - v["e"] * (v["v1"] - v["v2"]),
            "v2f": lambda v: v["v1f"] + v["e"] * (v["v1"] - v["v2"]),
            "v1": lambda v: v["v2"] + (v["v2f"] - v["v1f"]) / v["e"],
            "v2": lambda v: v["v1"] - (v["v2f"] - v["v1f"]) / v["e"],
        },
    )
)
