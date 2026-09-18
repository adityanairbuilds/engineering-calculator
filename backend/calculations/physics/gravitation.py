"""Gravitation formulas: Newton's law of gravitation, orbits, Kepler's third law."""

import math

from ...models.formula import Formula, Variable

GRAVITATION_FORMULAS: list[Formula] = []


def _gravitational_force_r(v: dict[str, float]) -> float:
    sq = (v["G"] * v["m1"] * v["m2"]) / v["Fg"]
    if sq < 0:
        raise ValueError("Gm₁m₂/Fg is negative — no real distance.")
    return math.sqrt(sq)


GRAVITATION_FORMULAS.append(
    Formula(
        id="gravitational-force",
        name="Newton's Law of Gravitation",
        category="Physics",
        subcategory="Gravitation",
        equation="F_g = Gm₁m₂ / r²",
        description="Calculates the gravitational attraction between two masses.",
        variables=[
            Variable("Fg", "Gravitational force", "N"),
            Variable("G", "Gravitational constant (≈6.674×10⁻¹¹)", "N·m²/kg²"),
            Variable("m1", "Mass 1", "kg"),
            Variable("m2", "Mass 2", "kg"),
            Variable("r", "Distance between centers", "m"),
        ],
        keywords=["gravitation", "gravity", "force", "mass", "distance", "newton"],
        solve={
            "Fg": lambda v: (v["G"] * v["m1"] * v["m2"]) / v["r"] ** 2,
            "G": lambda v: (v["Fg"] * v["r"] ** 2) / (v["m1"] * v["m2"]),
            "m1": lambda v: (v["Fg"] * v["r"] ** 2) / (v["G"] * v["m2"]),
            "m2": lambda v: (v["Fg"] * v["r"] ** 2) / (v["G"] * v["m1"]),
            "r": _gravitational_force_r,
        },
    )
)


def _gravitational_field_strength_r(v: dict[str, float]) -> float:
    sq = (v["G"] * v["M"]) / v["g"]
    if sq < 0:
        raise ValueError("GM/g is negative — no real distance.")
    return math.sqrt(sq)


GRAVITATION_FORMULAS.append(
    Formula(
        id="gravitational-field-strength",
        name="Gravitational Field Strength",
        category="Physics",
        subcategory="Gravitation",
        equation="g = GM / r²",
        description="Calculates the gravitational field strength (acceleration due to gravity) at a distance from a central mass.",
        variables=[
            Variable("g", "Gravitational field strength", "m/s²"),
            Variable("G", "Gravitational constant (≈6.674×10⁻¹¹)", "N·m²/kg²"),
            Variable("M", "Mass of central body", "kg"),
            Variable("r", "Distance from center", "m"),
        ],
        keywords=["gravitational field", "surface gravity", "gravity", "acceleration"],
        solve={
            "g": lambda v: (v["G"] * v["M"]) / v["r"] ** 2,
            "G": lambda v: (v["g"] * v["r"] ** 2) / v["M"],
            "M": lambda v: (v["g"] * v["r"] ** 2) / v["G"],
            "r": _gravitational_field_strength_r,
        },
    )
)

GRAVITATION_FORMULAS.append(
    Formula(
        id="gravitational-potential-energy",
        name="Gravitational Potential Energy (General)",
        category="Physics",
        subcategory="Gravitation",
        equation="U = -GMm / r",
        description="Calculates gravitational potential energy between two masses, taking the potential at infinite separation as zero.",
        variables=[
            Variable("U", "Gravitational potential energy", "J"),
            Variable("G", "Gravitational constant (≈6.674×10⁻¹¹)", "N·m²/kg²"),
            Variable("M", "Mass of central body", "kg"),
            Variable("m", "Mass of orbiting/second body", "kg"),
            Variable("r", "Distance between centers", "m"),
        ],
        keywords=["gravitational potential energy", "gravity", "orbital energy", "escape"],
        solve={
            "U": lambda v: -(v["G"] * v["M"] * v["m"]) / v["r"],
            "G": lambda v: -(v["U"] * v["r"]) / (v["M"] * v["m"]),
            "M": lambda v: -(v["U"] * v["r"]) / (v["G"] * v["m"]),
            "m": lambda v: -(v["U"] * v["r"]) / (v["G"] * v["M"]),
            "r": lambda v: -(v["G"] * v["M"] * v["m"]) / v["U"],
        },
    )
)


def _orbital_velocity_v(v: dict[str, float]) -> float:
    sq = (v["G"] * v["M"]) / v["r"]
    if sq < 0:
        raise ValueError("GM/r is negative — no real orbital velocity.")
    return math.sqrt(sq)


GRAVITATION_FORMULAS.append(
    Formula(
        id="orbital-velocity",
        name="Orbital Velocity",
        category="Physics",
        subcategory="Gravitation",
        equation="v_orbit = √(GM / r)",
        description="Calculates the speed needed to maintain a stable circular orbit around a central mass.",
        variables=[
            Variable("vOrbit", "Orbital velocity", "m/s"),
            Variable("G", "Gravitational constant (≈6.674×10⁻¹¹)", "N·m²/kg²"),
            Variable("M", "Mass of central body", "kg"),
            Variable("r", "Orbital radius", "m"),
        ],
        keywords=["orbital velocity", "orbit", "gravity", "space", "satellite"],
        solve={
            "vOrbit": _orbital_velocity_v,
            "G": lambda v: (v["vOrbit"] ** 2 * v["r"]) / v["M"],
            "M": lambda v: (v["vOrbit"] ** 2 * v["r"]) / v["G"],
            "r": lambda v: (v["G"] * v["M"]) / v["vOrbit"] ** 2,
        },
    )
)


def _escape_velocity_v(v: dict[str, float]) -> float:
    sq = (2 * v["G"] * v["M"]) / v["r"]
    if sq < 0:
        raise ValueError("2GM/r is negative — no real escape velocity.")
    return math.sqrt(sq)


GRAVITATION_FORMULAS.append(
    Formula(
        id="escape-velocity",
        name="Escape Velocity",
        category="Physics",
        subcategory="Gravitation",
        equation="v_escape = √(2GM / r)",
        description="Calculates the minimum velocity needed to escape a gravitational field from a given distance.",
        variables=[
            Variable("vEscape", "Escape velocity", "m/s"),
            Variable("G", "Gravitational constant (≈6.674×10⁻¹¹)", "N·m²/kg²"),
            Variable("M", "Mass of central body", "kg"),
            Variable("r", "Distance from center", "m"),
        ],
        keywords=["escape velocity", "gravity", "space", "orbital mechanics", "rocket"],
        solve={
            "vEscape": _escape_velocity_v,
            "G": lambda v: (v["vEscape"] ** 2 * v["r"]) / (2 * v["M"]),
            "M": lambda v: (v["vEscape"] ** 2 * v["r"]) / (2 * v["G"]),
            "r": lambda v: (2 * v["G"] * v["M"]) / v["vEscape"] ** 2,
        },
    )
)


def _keplers_third_law_t(v: dict[str, float]) -> float:
    sq = (4 * math.pi ** 2 * v["r"] ** 3) / (v["G"] * v["M"])
    if sq < 0:
        raise ValueError("4π²r³/GM is negative — no real period.")
    return math.sqrt(sq)


GRAVITATION_FORMULAS.append(
    Formula(
        id="keplers-third-law",
        name="Kepler's Third Law",
        category="Physics",
        subcategory="Gravitation",
        equation="T² = (4π² / GM)r³",
        description="Relates the orbital period and orbital radius for a body in circular orbit around a much larger central mass.",
        variables=[
            Variable("T", "Orbital period", "s"),
            Variable("G", "Gravitational constant (≈6.674×10⁻¹¹)", "N·m²/kg²"),
            Variable("M", "Mass of central body", "kg"),
            Variable("r", "Orbital radius", "m"),
        ],
        keywords=["kepler", "orbital period", "radius", "gravity", "orbit", "kepler's third law"],
        solve={
            "T": _keplers_third_law_t,
            "G": lambda v: (4 * math.pi ** 2 * v["r"] ** 3) / (v["M"] * v["T"] ** 2),
            "M": lambda v: (4 * math.pi ** 2 * v["r"] ** 3) / (v["G"] * v["T"] ** 2),
            "r": lambda v: math.cbrt((v["T"] ** 2 * v["G"] * v["M"]) / (4 * math.pi ** 2)),
        },
    )
)
