"""Engineering statics formulas: equilibrium, moments, friction, beam reactions."""

import math

from ...models.formula import Formula, Variable

STATICS_FORMULAS: list[Formula] = []

STATICS_FORMULAS.append(
    Formula(
        id="equilibrium-force",
        name="Force Equilibrium",
        category="Engineering",
        subcategory="Statics",
        equation="ΣF = 0",
        description="The net force on a body in static equilibrium is zero. Reference relation — sum each force component by hand.",
        variables=[Variable("sumF", "Sum of all forces", "N")],
        keywords=["equilibrium", "statics", "force", "net force", "engineering", "sum of forces"],
        solve={},
    )
)

STATICS_FORMULAS.append(
    Formula(
        id="equilibrium-torque",
        name="Torque (Moment) Equilibrium",
        category="Engineering",
        subcategory="Statics",
        equation="ΣM = 0",
        description="The net moment on a body in static equilibrium is zero. Reference relation — sum each moment by hand.",
        variables=[Variable("sumM", "Sum of all moments", "N·m")],
        keywords=["equilibrium", "statics", "torque", "moment", "rotational", "engineering"],
        solve={},
    )
)


def _center_of_mass_m1(v: dict[str, float]) -> float:
    if v["xcm"] == v["x1"]:
        raise ValueError("x_cm cannot equal x1 when solving for m1.")
    return (v["m2"] * (v["x2"] - v["xcm"])) / (v["xcm"] - v["x1"])


def _center_of_mass_m2(v: dict[str, float]) -> float:
    if v["xcm"] == v["x2"]:
        raise ValueError("x_cm cannot equal x2 when solving for m2.")
    return (v["m1"] * (v["x1"] - v["xcm"])) / (v["xcm"] - v["x2"])


def _center_of_mass_x1(v: dict[str, float]) -> float:
    if v["m1"] == 0:
        raise ValueError("m1 cannot be zero when solving for x1.")
    return (v["xcm"] * (v["m1"] + v["m2"]) - v["m2"] * v["x2"]) / v["m1"]


def _center_of_mass_x2(v: dict[str, float]) -> float:
    if v["m2"] == 0:
        raise ValueError("m2 cannot be zero when solving for x2.")
    return (v["xcm"] * (v["m1"] + v["m2"]) - v["m1"] * v["x1"]) / v["m2"]


STATICS_FORMULAS.append(
    Formula(
        id="center-of-mass-two-point",
        name="Center of Mass (Two Point Masses)",
        category="Engineering",
        subcategory="Statics",
        equation="x_cm = (m₁x₁ + m₂x₂) / (m₁ + m₂)",
        description="Calculates the center of mass position for a system of two point masses.",
        variables=[
            Variable("xcm", "Center of mass position", "m"),
            Variable("m1", "Mass 1", "kg"),
            Variable("x1", "Position of mass 1", "m"),
            Variable("m2", "Mass 2", "kg"),
            Variable("x2", "Position of mass 2", "m"),
        ],
        keywords=["center of mass", "centroid", "statics", "equilibrium", "center of gravity"],
        solve={
            "xcm": lambda v: (v["m1"] * v["x1"] + v["m2"] * v["x2"]) / (v["m1"] + v["m2"]),
            "m1": _center_of_mass_m1,
            "m2": _center_of_mass_m2,
            "x1": _center_of_mass_x1,
            "x2": _center_of_mass_x2,
        },
    )
)

STATICS_FORMULAS.append(
    Formula(
        id="moment-of-force",
        name="Moment of a Force",
        category="Engineering",
        subcategory="Statics",
        equation="M = Fd",
        description="Calculates the moment (turning effect) of a force about a point from the force and its perpendicular distance.",
        variables=[
            Variable("M", "Moment", "N·m"),
            Variable("F", "Force", "N"),
            Variable("d", "Perpendicular distance to point", "m"),
        ],
        keywords=["moment", "force", "statics", "torque", "lever arm"],
        solve={
            "M": lambda v: v["F"] * v["d"],
            "F": lambda v: v["M"] / v["d"],
            "d": lambda v: v["M"] / v["F"],
        },
    )
)

STATICS_FORMULAS.append(
    Formula(
        id="static-friction-force",
        name="Maximum Static Friction Force",
        category="Engineering",
        subcategory="Statics",
        equation="f = μN",
        description="Calculates the maximum static friction force from the coefficient of static friction and the normal force.",
        variables=[
            Variable("f", "Friction force", "N"),
            Variable("mu", "Coefficient of static friction", "dimensionless"),
            Variable("N", "Normal force", "N"),
        ],
        keywords=["friction", "static friction", "coefficient of friction", "statics", "normal force"],
        solve={
            "f": lambda v: v["mu"] * v["N"],
            "mu": lambda v: v["f"] / v["N"],
            "N": lambda v: v["f"] / v["mu"],
        },
    )
)

STATICS_FORMULAS.append(
    Formula(
        id="friction-angle",
        name="Angle of Friction",
        category="Engineering",
        subcategory="Statics",
        equation="φ = tan⁻¹(μ)",
        description="Calculates the friction angle at which a body just begins to slide, from the coefficient of friction.",
        variables=[
            Variable("phi", "Friction angle", "°"),
            Variable("mu", "Coefficient of friction", "dimensionless"),
        ],
        keywords=["friction angle", "angle of repose", "coefficient of friction", "statics"],
        solve={
            "phi": lambda v: math.degrees(math.atan(v["mu"])),
            "mu": lambda v: math.tan(math.radians(v["phi"])),
        },
    )
)

STATICS_FORMULAS.append(
    Formula(
        id="resultant-force-two-perpendicular",
        name="Resultant of Two Perpendicular Forces",
        category="Engineering",
        subcategory="Statics",
        equation="R = √(Fx² + Fy²), θ = tan⁻¹(Fy/Fx)",
        description="Calculates the magnitude and direction of the resultant of two perpendicular force components.",
        variables=[
            Variable("R", "Resultant force magnitude", "N"),
            Variable("Fx", "Force component (x)", "N"),
            Variable("Fy", "Force component (y)", "N"),
            Variable("theta", "Direction of resultant", "°"),
        ],
        keywords=["resultant force", "force components", "statics", "vector addition", "resultant"],
        solve={
            "R": lambda v: math.sqrt(v["Fx"] ** 2 + v["Fy"] ** 2),
            "theta": lambda v: math.degrees(math.atan2(v["Fy"], v["Fx"])),
            "Fx": lambda v: v["R"] * math.cos(math.radians(v["theta"])),
            "Fy": lambda v: v["R"] * math.sin(math.radians(v["theta"])),
        },
    )
)


def _beam_reaction_left_b(v: dict[str, float]) -> float:
    if v["P"] == v["R1"]:
        raise ValueError("P cannot equal R1 when solving for b.")
    return (v["R1"] * v["a"]) / (v["P"] - v["R1"])


STATICS_FORMULAS.append(
    Formula(
        id="simply-supported-beam-reaction-left",
        name="Simply Supported Beam Reaction — Left Support",
        category="Engineering",
        subcategory="Statics",
        equation="R₁ = Pb / (a + b)",
        description="Calculates the reaction at the left support of a simply supported beam carrying a single point load.",
        variables=[
            Variable("R1", "Reaction at left support", "N"),
            Variable("P", "Point load", "N"),
            Variable("a", "Distance from left support to load", "m"),
            Variable("b", "Distance from load to right support", "m"),
        ],
        keywords=["beam reactions", "simply supported beam", "statics", "point load", "support reactions"],
        solve={
            "R1": lambda v: (v["P"] * v["b"]) / (v["a"] + v["b"]),
            "P": lambda v: (v["R1"] * (v["a"] + v["b"])) / v["b"],
            "a": lambda v: (v["P"] * v["b"]) / v["R1"] - v["b"],
            "b": _beam_reaction_left_b,
        },
    )
)


def _beam_reaction_right_a(v: dict[str, float]) -> float:
    if v["P"] == v["R2"]:
        raise ValueError("P cannot equal R2 when solving for a.")
    return (v["R2"] * v["b"]) / (v["P"] - v["R2"])


STATICS_FORMULAS.append(
    Formula(
        id="simply-supported-beam-reaction-right",
        name="Simply Supported Beam Reaction — Right Support",
        category="Engineering",
        subcategory="Statics",
        equation="R₂ = Pa / (a + b)",
        description="Calculates the reaction at the right support of a simply supported beam carrying a single point load.",
        variables=[
            Variable("R2", "Reaction at right support", "N"),
            Variable("P", "Point load", "N"),
            Variable("a", "Distance from left support to load", "m"),
            Variable("b", "Distance from load to right support", "m"),
        ],
        keywords=["beam reactions", "simply supported beam", "statics", "point load", "support reactions"],
        solve={
            "R2": lambda v: (v["P"] * v["a"]) / (v["a"] + v["b"]),
            "P": lambda v: (v["R2"] * (v["a"] + v["b"])) / v["a"],
            "b": lambda v: (v["P"] * v["a"]) / v["R2"] - v["a"],
            "a": _beam_reaction_right_a,
        },
    )
)
