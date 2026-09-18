"""Work and energy formulas: work, kinetic/potential energy, power, efficiency."""

import math

from ...models.formula import Formula, Variable

WORK_ENERGY_FORMULAS: list[Formula] = []


def _work_theta(v: dict[str, float]) -> float:
    ratio = v["W"] / (v["F"] * v["d"])
    if ratio < -1 or ratio > 1:
        raise ValueError("W/(Fd) must be between -1 and 1.")
    return math.acos(ratio) * (180 / math.pi)


WORK_ENERGY_FORMULAS.append(
    Formula(
        id="work",
        name="Work",
        category="Physics",
        subcategory="Work and Energy",
        equation="W = Fd cos(θ)",
        description="Calculates the work done by a constant force applied at an angle to the displacement.",
        variables=[
            Variable("W", "Work", "J"),
            Variable("F", "Force", "N"),
            Variable("d", "Displacement", "m"),
            Variable("theta", "Angle between force and displacement", "°"),
        ],
        keywords=["work", "energy", "force", "displacement", "physics"],
        solve={
            "W": lambda v: v["F"] * v["d"] * math.cos((v["theta"] * math.pi) / 180),
            "F": lambda v: v["W"] / (v["d"] * math.cos((v["theta"] * math.pi) / 180)),
            "d": lambda v: v["W"] / (v["F"] * math.cos((v["theta"] * math.pi) / 180)),
            "theta": _work_theta,
        },
    )
)


def _kinetic_energy_v(v: dict[str, float]) -> float:
    sq = (2 * v["KE"]) / v["m"]
    if sq < 0:
        raise ValueError("2·KE/m is negative — no real velocity.")
    return math.sqrt(sq)


WORK_ENERGY_FORMULAS.append(
    Formula(
        id="kinetic-energy",
        name="Kinetic Energy",
        category="Physics",
        subcategory="Work and Energy",
        equation="KE = ½mv²",
        description="Calculates the kinetic energy of a moving object from its mass and speed.",
        variables=[
            Variable("KE", "Kinetic energy", "J"),
            Variable("m", "Mass", "kg"),
            Variable("v", "Velocity", "m/s"),
        ],
        keywords=["kinetic energy", "energy", "motion", "velocity", "mass", "speed"],
        solve={
            "KE": lambda v: 0.5 * v["m"] * v["v"] ** 2,
            "m": lambda v: (2 * v["KE"]) / v["v"] ** 2,
            "v": _kinetic_energy_v,
        },
    )
)

WORK_ENERGY_FORMULAS.append(
    Formula(
        id="potential-energy",
        name="Gravitational Potential Energy",
        category="Physics",
        subcategory="Work and Energy",
        equation="PE = mgh",
        description="Calculates gravitational potential energy near a planet's surface from mass, gravity, and height.",
        variables=[
            Variable("PE", "Potential energy", "J"),
            Variable("m", "Mass", "kg"),
            Variable("g", "Gravitational acceleration", "m/s²"),
            Variable("h", "Height", "m"),
        ],
        keywords=["potential energy", "energy", "gravity", "height", "mass"],
        solve={
            "PE": lambda v: v["m"] * v["g"] * v["h"],
            "m": lambda v: v["PE"] / (v["g"] * v["h"]),
            "g": lambda v: v["PE"] / (v["m"] * v["h"]),
            "h": lambda v: v["PE"] / (v["m"] * v["g"]),
        },
    )
)


def _elastic_potential_energy_x(v: dict[str, float]) -> float:
    sq = (2 * v["PE"]) / v["k"]
    if sq < 0:
        raise ValueError("2·PE/k is negative — no real displacement.")
    return math.sqrt(sq)


WORK_ENERGY_FORMULAS.append(
    Formula(
        id="elastic-potential-energy",
        name="Elastic Potential Energy",
        category="Physics",
        subcategory="Work and Energy",
        equation="PE = ½kx²",
        description="Calculates the energy stored in a stretched or compressed spring.",
        variables=[
            Variable("PE", "Elastic potential energy", "J"),
            Variable("k", "Spring constant", "N/m"),
            Variable("x", "Displacement from equilibrium", "m"),
        ],
        keywords=["elastic potential energy", "spring energy", "hooke", "spring constant", "energy"],
        solve={
            "PE": lambda v: 0.5 * v["k"] * v["x"] ** 2,
            "k": lambda v: (2 * v["PE"]) / v["x"] ** 2,
            "x": _elastic_potential_energy_x,
        },
    )
)

WORK_ENERGY_FORMULAS.append(
    Formula(
        id="power",
        name="Power (Work / Time)",
        category="Physics",
        subcategory="Work and Energy",
        equation="P = W / t",
        description="Calculates power as the rate at which work is done.",
        variables=[
            Variable("P", "Power", "W"),
            Variable("W", "Work", "J"),
            Variable("t", "Time", "s"),
        ],
        keywords=["power", "energy", "work", "time", "watts"],
        solve={
            "P": lambda v: v["W"] / v["t"],
            "W": lambda v: v["P"] * v["t"],
            "t": lambda v: v["W"] / v["P"],
        },
    )
)

WORK_ENERGY_FORMULAS.append(
    Formula(
        id="power-force-velocity",
        name="Power (Force & Velocity)",
        category="Physics",
        subcategory="Work and Energy",
        equation="P = Fv",
        description="Calculates the instantaneous power delivered by a force acting on an object moving at a given velocity.",
        variables=[
            Variable("P", "Power", "W"),
            Variable("F", "Force", "N"),
            Variable("v", "Velocity", "m/s"),
        ],
        keywords=["power", "force", "velocity", "watts", "instantaneous power"],
        solve={
            "P": lambda v: v["F"] * v["v"],
            "F": lambda v: v["P"] / v["v"],
            "v": lambda v: v["P"] / v["F"],
        },
    )
)

WORK_ENERGY_FORMULAS.append(
    Formula(
        id="efficiency",
        name="Efficiency",
        category="Physics",
        subcategory="Work and Energy",
        equation="η = (E_out / E_in) × 100%",
        description="Calculates the efficiency of a machine or process as a percentage of useful energy output over total energy input.",
        variables=[
            Variable("eta", "Efficiency", "%"),
            Variable("Eout", "Useful energy output", "J"),
            Variable("Ein", "Total energy input", "J"),
        ],
        keywords=["efficiency", "energy", "power", "output", "input", "percentage"],
        solve={
            "eta": lambda v: (v["Eout"] / v["Ein"]) * 100,
            "Eout": lambda v: (v["eta"] / 100) * v["Ein"],
            "Ein": lambda v: v["Eout"] / (v["eta"] / 100),
        },
    )
)
