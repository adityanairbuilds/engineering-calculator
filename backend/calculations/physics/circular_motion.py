"""Circular motion and rotational motion formulas."""

import math

from ...models.formula import Formula, Variable

CIRCULAR_MOTION_FORMULAS: list[Formula] = []


def _centripetal_acceleration_v(v: dict[str, float]) -> float:
    sq = v["ac"] * v["r"]
    if sq < 0:
        raise ValueError("ac·r is negative — no real velocity.")
    return math.sqrt(sq)


CIRCULAR_MOTION_FORMULAS.append(
    Formula(
        id="centripetal-acceleration",
        name="Centripetal Acceleration",
        category="Physics",
        subcategory="Circular Motion",
        equation="a_c = v² / r",
        description="Calculates the centripetal acceleration of an object moving in a circular path.",
        variables=[
            Variable("ac", "Centripetal acceleration", "m/s²"),
            Variable("v", "Tangential velocity", "m/s"),
            Variable("r", "Radius of circular path", "m"),
        ],
        keywords=["centripetal", "acceleration", "circular motion", "velocity", "radius"],
        solve={
            "ac": lambda v: v["v"] ** 2 / v["r"],
            "v": _centripetal_acceleration_v,
            "r": lambda v: v["v"] ** 2 / v["ac"],
        },
    )
)


def _centripetal_force_v(v: dict[str, float]) -> float:
    sq = (v["Fc"] * v["r"]) / v["m"]
    if sq < 0:
        raise ValueError("Fc·r/m is negative — no real velocity.")
    return math.sqrt(sq)


CIRCULAR_MOTION_FORMULAS.append(
    Formula(
        id="centripetal-force",
        name="Centripetal Force",
        category="Physics",
        subcategory="Circular Motion",
        equation="F_c = mv² / r",
        description="Calculates the centripetal force needed to keep an object moving in a circular path.",
        variables=[
            Variable("Fc", "Centripetal force", "N"),
            Variable("m", "Mass", "kg"),
            Variable("v", "Tangential velocity", "m/s"),
            Variable("r", "Radius of circular path", "m"),
        ],
        keywords=["centripetal", "force", "circular motion", "mass", "velocity"],
        solve={
            "Fc": lambda v: (v["m"] * v["v"] ** 2) / v["r"],
            "m": lambda v: (v["Fc"] * v["r"]) / v["v"] ** 2,
            "v": _centripetal_force_v,
            "r": lambda v: (v["m"] * v["v"] ** 2) / v["Fc"],
        },
    )
)

CIRCULAR_MOTION_FORMULAS.append(
    Formula(
        id="angular-velocity",
        name="Angular Velocity",
        category="Physics",
        subcategory="Circular Motion",
        equation="ω = θ / t",
        description="Calculates angular velocity from angular displacement and time.",
        variables=[
            Variable("omega", "Angular velocity", "rad/s"),
            Variable("theta", "Angular displacement", "rad"),
            Variable("t", "Time", "s"),
        ],
        keywords=["angular velocity", "circular motion", "rotation", "angle", "time", "omega"],
        solve={
            "omega": lambda v: v["theta"] / v["t"],
            "theta": lambda v: v["omega"] * v["t"],
            "t": lambda v: v["theta"] / v["omega"],
        },
    )
)

CIRCULAR_MOTION_FORMULAS.append(
    Formula(
        id="angular-acceleration",
        name="Angular Acceleration",
        category="Physics",
        subcategory="Circular Motion",
        equation="α = Δω / Δt",
        description="Calculates angular acceleration from a change in angular velocity over a time interval.",
        variables=[
            Variable("alpha", "Angular acceleration", "rad/s²"),
            Variable("domega", "Change in angular velocity", "rad/s"),
            Variable("dt", "Time interval", "s"),
        ],
        keywords=["angular acceleration", "circular motion", "rotation", "angular velocity"],
        solve={
            "alpha": lambda v: v["domega"] / v["dt"],
            "domega": lambda v: v["alpha"] * v["dt"],
            "dt": lambda v: v["domega"] / v["alpha"],
        },
    )
)

CIRCULAR_MOTION_FORMULAS.append(
    Formula(
        id="period-frequency",
        name="Period and Frequency",
        category="Physics",
        subcategory="Circular Motion",
        equation="T = 1 / f",
        description="Relates the period and frequency of any repeating (periodic) motion, such as rotation or oscillation.",
        variables=[
            Variable("T", "Period", "s"),
            Variable("f", "Frequency", "Hz"),
        ],
        keywords=["period", "frequency", "circular motion", "rotation", "time", "cycle"],
        solve={
            "T": lambda v: 1 / v["f"],
            "f": lambda v: 1 / v["T"],
        },
    )
)

CIRCULAR_MOTION_FORMULAS.append(
    Formula(
        id="tangential-velocity",
        name="Tangential Velocity",
        category="Physics",
        subcategory="Circular Motion",
        equation="v = rω",
        description="Calculates the tangential (linear) speed of a point moving in a circle from the radius and angular velocity.",
        variables=[
            Variable("v", "Tangential velocity", "m/s"),
            Variable("r", "Radius", "m"),
            Variable("omega", "Angular velocity", "rad/s"),
        ],
        keywords=["tangential velocity", "linear velocity", "angular velocity", "circular motion", "rotation"],
        solve={
            "v": lambda v: v["r"] * v["omega"],
            "r": lambda v: v["v"] / v["omega"],
            "omega": lambda v: v["v"] / v["r"],
        },
    )
)


def _torque_theta(v: dict[str, float]) -> float:
    ratio = v["tau"] / (v["r"] * v["F"])
    if ratio < -1 or ratio > 1:
        raise ValueError("τ/(rF) must be between -1 and 1.")
    return math.asin(ratio) * (180 / math.pi)


CIRCULAR_MOTION_FORMULAS.append(
    Formula(
        id="torque",
        name="Torque",
        category="Physics",
        subcategory="Rotational Motion",
        equation="τ = rF sin(θ)",
        description="Calculates the torque produced by a force applied at a distance from a pivot point.",
        variables=[
            Variable("tau", "Torque", "N·m"),
            Variable("r", "Distance from pivot (lever arm)", "m"),
            Variable("F", "Applied force", "N"),
            Variable("theta", "Angle between force and lever arm", "°"),
        ],
        keywords=["torque", "moment", "rotation", "force", "lever arm", "rotational motion"],
        solve={
            "tau": lambda v: v["r"] * v["F"] * math.sin((v["theta"] * math.pi) / 180),
            "r": lambda v: v["tau"] / (v["F"] * math.sin((v["theta"] * math.pi) / 180)),
            "F": lambda v: v["tau"] / (v["r"] * math.sin((v["theta"] * math.pi) / 180)),
            "theta": _torque_theta,
        },
    )
)


def _moment_of_inertia_point_mass_r(v: dict[str, float]) -> float:
    sq = v["I"] / v["m"]
    if sq < 0:
        raise ValueError("I/m is negative — no real radius.")
    return math.sqrt(sq)


CIRCULAR_MOTION_FORMULAS.append(
    Formula(
        id="moment-of-inertia-point-mass",
        name="Moment of Inertia (Point Mass)",
        category="Physics",
        subcategory="Rotational Motion",
        equation="I = mr²",
        description="Calculates the moment of inertia of a point mass rotating about an axis at a fixed radius.",
        variables=[
            Variable("I", "Moment of inertia", "kg·m²"),
            Variable("m", "Mass", "kg"),
            Variable("r", "Distance from axis", "m"),
        ],
        keywords=["moment of inertia", "rotational inertia", "rotation", "point mass"],
        solve={
            "I": lambda v: v["m"] * v["r"] ** 2,
            "m": lambda v: v["I"] / v["r"] ** 2,
            "r": _moment_of_inertia_point_mass_r,
        },
    )
)

CIRCULAR_MOTION_FORMULAS.append(
    Formula(
        id="angular-momentum",
        name="Angular Momentum",
        category="Physics",
        subcategory="Rotational Motion",
        equation="L = Iω",
        description="Calculates the angular momentum of a rotating object from its moment of inertia and angular velocity.",
        variables=[
            Variable("L", "Angular momentum", "kg·m²/s"),
            Variable("I", "Moment of inertia", "kg·m²"),
            Variable("omega", "Angular velocity", "rad/s"),
        ],
        keywords=["angular momentum", "rotation", "moment of inertia", "spin"],
        solve={
            "L": lambda v: v["I"] * v["omega"],
            "I": lambda v: v["L"] / v["omega"],
            "omega": lambda v: v["L"] / v["I"],
        },
    )
)


def _rotational_kinetic_energy_omega(v: dict[str, float]) -> float:
    sq = (2 * v["KErot"]) / v["I"]
    if sq < 0:
        raise ValueError("2·KErot/I is negative — no real angular velocity.")
    return math.sqrt(sq)


CIRCULAR_MOTION_FORMULAS.append(
    Formula(
        id="rotational-kinetic-energy",
        name="Rotational Kinetic Energy",
        category="Physics",
        subcategory="Rotational Motion",
        equation="KE_rot = ½Iω²",
        description="Calculates the kinetic energy of a rotating object from its moment of inertia and angular velocity.",
        variables=[
            Variable("KErot", "Rotational kinetic energy", "J"),
            Variable("I", "Moment of inertia", "kg·m²"),
            Variable("omega", "Angular velocity", "rad/s"),
        ],
        keywords=["rotational kinetic energy", "rotation", "moment of inertia", "spinning energy"],
        solve={
            "KErot": lambda v: 0.5 * v["I"] * v["omega"] ** 2,
            "I": lambda v: (2 * v["KErot"]) / v["omega"] ** 2,
            "omega": _rotational_kinetic_energy_omega,
        },
    )
)

CIRCULAR_MOTION_FORMULAS.append(
    Formula(
        id="newtons-second-law-rotation",
        name="Newton's Second Law (Rotation)",
        category="Physics",
        subcategory="Rotational Motion",
        equation="τ = Iα",
        description="Relates net torque, moment of inertia, and angular acceleration — the rotational analogue of F = ma.",
        variables=[
            Variable("tau", "Net torque", "N·m"),
            Variable("I", "Moment of inertia", "kg·m²"),
            Variable("alpha", "Angular acceleration", "rad/s²"),
        ],
        keywords=["torque", "rotational newtons second law", "moment of inertia", "angular acceleration", "rotation"],
        solve={
            "tau": lambda v: v["I"] * v["alpha"],
            "I": lambda v: v["tau"] / v["alpha"],
            "alpha": lambda v: v["tau"] / v["I"],
        },
    )
)
