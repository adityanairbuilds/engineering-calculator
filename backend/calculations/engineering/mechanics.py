"""Engineering mechanics formulas: stress, strain, moments of inertia, levers."""

from ...models.formula import Formula, Variable

MECHANICS_FORMULAS: list[Formula] = []

MECHANICS_FORMULAS.append(
    Formula(
        id="stress",
        name="Stress",
        category="Engineering",
        subcategory="Mechanics",
        equation="σ = F / A",
        description="Calculates mechanical (normal) stress from applied force and cross-sectional area.",
        variables=[
            Variable("sigma", "Stress", "Pa"),
            Variable("F", "Applied force", "N"),
            Variable("A", "Cross-sectional area", "m²"),
        ],
        keywords=["stress", "mechanics", "force", "engineering", "normal stress"],
        solve={
            "sigma": lambda v: v["F"] / v["A"],
            "F": lambda v: v["sigma"] * v["A"],
            "A": lambda v: v["F"] / v["sigma"],
        },
    )
)

MECHANICS_FORMULAS.append(
    Formula(
        id="strain",
        name="Strain",
        category="Engineering",
        subcategory="Mechanics",
        equation="ε = ΔL / L₀",
        description="Calculates engineering strain from the change in length relative to original length.",
        variables=[
            Variable("epsilon", "Strain", "dimensionless"),
            Variable("deltaL", "Change in length", "m"),
            Variable("L0", "Original length", "m"),
        ],
        keywords=["strain", "deformation", "mechanics", "engineering", "elongation"],
        solve={
            "epsilon": lambda v: v["deltaL"] / v["L0"],
            "deltaL": lambda v: v["epsilon"] * v["L0"],
            "L0": lambda v: v["deltaL"] / v["epsilon"],
        },
    )
)

MECHANICS_FORMULAS.append(
    Formula(
        id="youngs-modulus",
        name="Young's Modulus",
        category="Engineering",
        subcategory="Mechanics",
        equation="E = σ / ε",
        description="Calculates the modulus of elasticity from stress and strain in the linear-elastic range.",
        variables=[
            Variable("E", "Young's modulus", "Pa"),
            Variable("sigma", "Stress", "Pa"),
            Variable("epsilon", "Strain", "dimensionless"),
        ],
        keywords=["young's modulus", "elasticity", "stress", "strain", "mechanics", "elastic modulus"],
        solve={
            "E": lambda v: v["sigma"] / v["epsilon"],
            "sigma": lambda v: v["E"] * v["epsilon"],
            "epsilon": lambda v: v["sigma"] / v["E"],
        },
    )
)


def _moment_inertia_cylinder_r(v: dict[str, float]) -> float:
    val = (2 * v["I"]) / v["m"]
    if val < 0:
        raise ValueError("Radius squared cannot be negative for these inputs.")
    return val**0.5


MECHANICS_FORMULAS.append(
    Formula(
        id="moment-inertia-cylinder",
        name="Moment of Inertia (Solid Cylinder)",
        category="Engineering",
        subcategory="Mechanics",
        equation="I = ½mr²",
        description="Mass moment of inertia of a solid cylinder about its central longitudinal axis.",
        variables=[
            Variable("I", "Moment of inertia", "kg·m²"),
            Variable("m", "Mass", "kg"),
            Variable("r", "Radius", "m"),
        ],
        keywords=["moment of inertia", "cylinder", "rotational", "mechanics", "engineering"],
        solve={
            "I": lambda v: 0.5 * v["m"] * v["r"] ** 2,
            "m": lambda v: (2 * v["I"]) / v["r"] ** 2,
            "r": _moment_inertia_cylinder_r,
        },
    )
)


def _moment_inertia_sphere_r(v: dict[str, float]) -> float:
    val = v["I"] / ((2 / 5) * v["m"])
    if val < 0:
        raise ValueError("Radius squared cannot be negative for these inputs.")
    return val**0.5


MECHANICS_FORMULAS.append(
    Formula(
        id="moment-inertia-sphere",
        name="Moment of Inertia (Solid Sphere)",
        category="Engineering",
        subcategory="Mechanics",
        equation="I = (2/5)mr²",
        description="Mass moment of inertia of a solid sphere about an axis through its center.",
        variables=[
            Variable("I", "Moment of inertia", "kg·m²"),
            Variable("m", "Mass", "kg"),
            Variable("r", "Radius", "m"),
        ],
        keywords=["moment of inertia", "sphere", "rotational", "mechanics", "engineering"],
        solve={
            "I": lambda v: (2 / 5) * v["m"] * v["r"] ** 2,
            "m": lambda v: v["I"] / ((2 / 5) * v["r"] ** 2),
            "r": _moment_inertia_sphere_r,
        },
    )
)


def _moment_inertia_rod_center_L(v: dict[str, float]) -> float:
    val = v["I"] / ((1 / 12) * v["m"])
    if val < 0:
        raise ValueError("Length squared cannot be negative for these inputs.")
    return val**0.5


MECHANICS_FORMULAS.append(
    Formula(
        id="moment-inertia-rod-center",
        name="Moment of Inertia (Slender Rod, Center)",
        category="Engineering",
        subcategory="Mechanics",
        equation="I = (1/12)mL²",
        description="Mass moment of inertia of a slender rod about an axis through its center, perpendicular to its length.",
        variables=[
            Variable("I", "Moment of inertia", "kg·m²"),
            Variable("m", "Mass", "kg"),
            Variable("L", "Rod length", "m"),
        ],
        keywords=["moment of inertia", "rod", "rotational", "mechanics", "engineering"],
        solve={
            "I": lambda v: (1 / 12) * v["m"] * v["L"] ** 2,
            "m": lambda v: v["I"] / ((1 / 12) * v["L"] ** 2),
            "L": _moment_inertia_rod_center_L,
        },
    )
)


def _parallel_axis_theorem_d(v: dict[str, float]) -> float:
    val = (v["I"] - v["Icm"]) / v["m"]
    if val < 0:
        raise ValueError("Distance squared cannot be negative for these inputs.")
    return val**0.5


MECHANICS_FORMULAS.append(
    Formula(
        id="parallel-axis-theorem",
        name="Parallel Axis Theorem",
        category="Engineering",
        subcategory="Mechanics",
        equation="I = I_cm + md²",
        description="Relates the moment of inertia about any axis to the moment of inertia about a parallel axis through the center of mass.",
        variables=[
            Variable("I", "Moment of inertia about new axis", "kg·m²"),
            Variable("Icm", "Moment of inertia about center of mass", "kg·m²"),
            Variable("m", "Mass", "kg"),
            Variable("d", "Distance between axes", "m"),
        ],
        keywords=["parallel axis theorem", "moment of inertia", "mechanics", "engineering"],
        solve={
            "I": lambda v: v["Icm"] + v["m"] * v["d"] ** 2,
            "Icm": lambda v: v["I"] - v["m"] * v["d"] ** 2,
            "m": lambda v: (v["I"] - v["Icm"]) / v["d"] ** 2,
            "d": _parallel_axis_theorem_d,
        },
    )
)

MECHANICS_FORMULAS.append(
    Formula(
        id="mechanical-advantage-lever",
        name="Mechanical Advantage (Lever)",
        category="Engineering",
        subcategory="Mechanics",
        equation="MA = F_out / F_in",
        description="Calculates the mechanical advantage of a lever from output and input forces.",
        variables=[
            Variable("MA", "Mechanical advantage", "dimensionless"),
            Variable("Fout", "Output force", "N"),
            Variable("Fin", "Input force", "N"),
        ],
        keywords=["mechanical advantage", "lever", "simple machines", "engineering"],
        solve={
            "MA": lambda v: v["Fout"] / v["Fin"],
            "Fout": lambda v: v["MA"] * v["Fin"],
            "Fin": lambda v: v["Fout"] / v["MA"],
        },
    )
)
