"""Kinematics formulas: velocity, acceleration, projectile motion."""

import math

from ...models.formula import Formula, Variable

KINEMATICS_FORMULAS: list[Formula] = []

KINEMATICS_FORMULAS.append(
    Formula(
        id="velocity",
        name="Velocity",
        category="Physics",
        subcategory="Kinematics",
        equation="v = Δx / Δt",
        description="Calculates average velocity from displacement and time interval.",
        variables=[
            Variable("v", "Velocity", "m/s"),
            Variable("dx", "Displacement", "m"),
            Variable("dt", "Time interval", "s"),
        ],
        keywords=["velocity", "speed", "kinematics", "motion", "displacement"],
        solve={
            "v": lambda v: v["dx"] / v["dt"],
            "dx": lambda v: v["v"] * v["dt"],
            "dt": lambda v: v["dx"] / v["v"],
        },
    )
)

KINEMATICS_FORMULAS.append(
    Formula(
        id="acceleration",
        name="Acceleration",
        category="Physics",
        subcategory="Kinematics",
        equation="a = Δv / Δt",
        description="Calculates acceleration from a change in velocity over a time interval.",
        variables=[
            Variable("a", "Acceleration", "m/s²"),
            Variable("dv", "Change in velocity", "m/s"),
            Variable("dt", "Time interval", "s"),
        ],
        keywords=["acceleration", "kinematics", "motion", "velocity change", "speeding up"],
        solve={
            "a": lambda v: v["dv"] / v["dt"],
            "dv": lambda v: v["a"] * v["dt"],
            "dt": lambda v: v["dv"] / v["a"],
        },
    )
)

KINEMATICS_FORMULAS.append(
    Formula(
        id="kinematics-velocity-time",
        name="Kinematic Equation (v = u + at)",
        category="Physics",
        subcategory="Kinematics",
        equation="v = u + at",
        description="Relates final velocity to initial velocity, acceleration, and time for constant acceleration.",
        variables=[
            Variable("v", "Final velocity", "m/s"),
            Variable("u", "Initial velocity", "m/s"),
            Variable("a", "Acceleration", "m/s²"),
            Variable("t", "Time", "s"),
        ],
        keywords=["kinematics", "equation of motion", "final velocity", "initial velocity", "constant acceleration"],
        solve={
            "v": lambda v: v["u"] + v["a"] * v["t"],
            "u": lambda v: v["v"] - v["a"] * v["t"],
            "a": lambda v: (v["v"] - v["u"]) / v["t"],
            "t": lambda v: (v["v"] - v["u"]) / v["a"],
        },
    )
)


def _kinematics_velocity_squared_v(v: dict[str, float]) -> float:
    sq = v["u"] ** 2 + 2 * v["a"] * v["s"]
    if sq < 0:
        raise ValueError("u² + 2as is negative — no real velocity.")
    return math.sqrt(sq)


def _kinematics_velocity_squared_u(v: dict[str, float]) -> float:
    sq = v["v"] ** 2 - 2 * v["a"] * v["s"]
    if sq < 0:
        raise ValueError("v² - 2as is negative — no real velocity.")
    return math.sqrt(sq)


KINEMATICS_FORMULAS.append(
    Formula(
        id="kinematics-velocity-squared",
        name="Kinematic Equation (v² = u² + 2as)",
        category="Physics",
        subcategory="Kinematics",
        equation="v² = u² + 2as",
        description="Relates final velocity, initial velocity, acceleration, and displacement (no time needed).",
        variables=[
            Variable("v", "Final velocity", "m/s"),
            Variable("u", "Initial velocity", "m/s"),
            Variable("a", "Acceleration", "m/s²"),
            Variable("s", "Displacement", "m"),
        ],
        keywords=["kinematics", "equation of motion", "velocity", "acceleration", "displacement", "torricelli"],
        solve={
            "v": _kinematics_velocity_squared_v,
            "u": _kinematics_velocity_squared_u,
            "a": lambda v: (v["v"] ** 2 - v["u"] ** 2) / (2 * v["s"]),
            "s": lambda v: (v["v"] ** 2 - v["u"] ** 2) / (2 * v["a"]),
        },
    )
)


def _kinematics_displacement_t(v: dict[str, float]) -> float:
    if v["a"] == 0:
        if v["u"] == 0:
            raise ValueError("Cannot solve for time when both initial velocity and acceleration are zero.")
        return v["s"] / v["u"]
    disc = v["u"] ** 2 + 2 * v["a"] * v["s"]
    if disc < 0:
        raise ValueError("No real solution for time with these values.")
    sqrt_disc = math.sqrt(disc)
    candidates = [t for t in [(-v["u"] + sqrt_disc) / v["a"], (-v["u"] - sqrt_disc) / v["a"]] if t >= 0]
    if not candidates:
        raise ValueError("No non-negative time solves these values.")
    return min(candidates)


KINEMATICS_FORMULAS.append(
    Formula(
        id="kinematics-displacement",
        name="Kinematic Equation (s = ut + ½at²)",
        category="Physics",
        subcategory="Kinematics",
        equation="s = ut + ½at²",
        description="Relates displacement, initial velocity, acceleration, and time for constant acceleration.",
        variables=[
            Variable("s", "Displacement", "m"),
            Variable("u", "Initial velocity", "m/s"),
            Variable("a", "Acceleration", "m/s²"),
            Variable("t", "Time", "s"),
        ],
        keywords=["kinematics", "equation of motion", "displacement", "time", "position"],
        solve={
            "s": lambda v: v["u"] * v["t"] + 0.5 * v["a"] * v["t"] ** 2,
            "u": lambda v: (v["s"] - 0.5 * v["a"] * v["t"] ** 2) / v["t"],
            "a": lambda v: (2 * (v["s"] - v["u"] * v["t"])) / v["t"] ** 2,
            "t": _kinematics_displacement_t,
        },
    )
)

KINEMATICS_FORMULAS.append(
    Formula(
        id="average-velocity",
        name="Average Velocity (Constant Acceleration)",
        category="Physics",
        subcategory="Kinematics",
        equation="v_avg = (u + v) / 2",
        description="Calculates the average velocity during constant acceleration from the initial and final velocities.",
        variables=[
            Variable("vavg", "Average velocity", "m/s"),
            Variable("u", "Initial velocity", "m/s"),
            Variable("v", "Final velocity", "m/s"),
        ],
        keywords=["average velocity", "kinematics", "mean velocity", "constant acceleration"],
        solve={
            "vavg": lambda v: (v["u"] + v["v"]) / 2,
            "u": lambda v: 2 * v["vavg"] - v["v"],
            "v": lambda v: 2 * v["vavg"] - v["u"],
        },
    )
)

KINEMATICS_FORMULAS.append(
    Formula(
        id="relative-velocity",
        name="Relative Velocity",
        category="Physics",
        subcategory="Kinematics",
        equation="v_rel = vA - vB",
        description="Calculates the velocity of object A relative to object B using signed velocities along one line of motion (opposite directions should have opposite signs).",
        variables=[
            Variable("vRel", "Relative velocity of A with respect to B", "m/s"),
            Variable("vA", "Velocity of A", "m/s"),
            Variable("vB", "Velocity of B", "m/s"),
        ],
        keywords=["relative velocity", "kinematics", "relative motion", "closing speed"],
        solve={
            "vRel": lambda v: v["vA"] - v["vB"],
            "vA": lambda v: v["vRel"] + v["vB"],
            "vB": lambda v: v["vA"] - v["vRel"],
        },
    )
)


def _free_fall_t(v: dict[str, float]) -> float:
    ratio = (2 * v["h"]) / v["g"]
    if ratio < 0:
        raise ValueError("2h/g is negative — no real time.")
    return math.sqrt(ratio)


KINEMATICS_FORMULAS.append(
    Formula(
        id="free-fall",
        name="Free Fall Distance",
        category="Physics",
        subcategory="Kinematics",
        equation="h = ½gt²",
        description="Calculates the distance fallen under gravity from rest.",
        variables=[
            Variable("h", "Height fallen", "m"),
            Variable("g", "Gravitational acceleration", "m/s²"),
            Variable("t", "Time", "s"),
        ],
        keywords=["free fall", "gravity", "kinematics", "motion", "height", "drop"],
        solve={
            "h": lambda v: 0.5 * v["g"] * v["t"] ** 2,
            "g": lambda v: (2 * v["h"]) / v["t"] ** 2,
            "t": _free_fall_t,
        },
    )
)


def _projectile_range_v0(v: dict[str, float]) -> float:
    sq = (v["R"] * v["g"]) / math.sin((2 * v["theta"] * math.pi) / 180)
    if sq < 0:
        raise ValueError("No real initial velocity for these values.")
    return math.sqrt(sq)


def _projectile_range_theta(v: dict[str, float]) -> float:
    ratio = (v["R"] * v["g"]) / v["v0"] ** 2
    if ratio < -1 or ratio > 1:
        raise ValueError("Rg/v₀² must be between -1 and 1.")
    return math.asin(ratio) * (90 / math.pi)


KINEMATICS_FORMULAS.append(
    Formula(
        id="projectile-range",
        name="Projectile Range",
        category="Physics",
        subcategory="Kinematics",
        equation="R = (v₀² sin(2θ)) / g",
        description="Calculates the horizontal distance traveled by a projectile launched and landing at the same height.",
        variables=[
            Variable("R", "Range", "m"),
            Variable("v0", "Initial velocity", "m/s"),
            Variable("theta", "Launch angle", "°"),
            Variable("g", "Gravitational acceleration", "m/s²"),
        ],
        keywords=["projectile", "range", "kinematics", "motion", "angle", "trajectory"],
        solve={
            "R": lambda v: (v["v0"] ** 2 * math.sin((2 * v["theta"] * math.pi) / 180)) / v["g"],
            "v0": _projectile_range_v0,
            "g": lambda v: (v["v0"] ** 2 * math.sin((2 * v["theta"] * math.pi) / 180)) / v["R"],
            "theta": _projectile_range_theta,
        },
    )
)


def _projectile_max_height_v0(v: dict[str, float]) -> float:
    sq = (2 * v["g"] * v["hmax"]) / math.sin((v["theta"] * math.pi) / 180) ** 2
    if sq < 0:
        raise ValueError("No real initial velocity for these values.")
    return math.sqrt(sq)


def _projectile_max_height_theta(v: dict[str, float]) -> float:
    sq = (2 * v["g"] * v["hmax"]) / v["v0"] ** 2
    if sq < 0 or sq > 1:
        raise ValueError("2ghmax/v₀² must be between 0 and 1.")
    return math.asin(math.sqrt(sq)) * (180 / math.pi)


KINEMATICS_FORMULAS.append(
    Formula(
        id="projectile-max-height",
        name="Projectile Maximum Height",
        category="Physics",
        subcategory="Kinematics",
        equation="h_max = (v₀² sin²(θ)) / (2g)",
        description="Calculates the maximum height reached by a projectile.",
        variables=[
            Variable("hmax", "Maximum height", "m"),
            Variable("v0", "Initial velocity", "m/s"),
            Variable("theta", "Launch angle", "°"),
            Variable("g", "Gravitational acceleration", "m/s²"),
        ],
        keywords=["projectile", "maximum height", "kinematics", "motion", "trajectory"],
        solve={
            "hmax": lambda v: (v["v0"] ** 2 * math.sin((v["theta"] * math.pi) / 180) ** 2) / (2 * v["g"]),
            "v0": _projectile_max_height_v0,
            "g": lambda v: (v["v0"] ** 2 * math.sin((v["theta"] * math.pi) / 180) ** 2) / (2 * v["hmax"]),
            "theta": _projectile_max_height_theta,
        },
    )
)
