"""Aerospace engineering formulas: aerodynamic coefficients, wing loading, Mach number, rocket propulsion."""

import math

from ...models.formula import Formula, Variable

AEROSPACE_FORMULAS: list[Formula] = []


def _lift_coefficient_v(v: dict[str, float]) -> float:
    val = (2 * v["L"]) / (v["Cl"] * v["rho"] * v["S"])
    if val < 0:
        raise ValueError("Cannot take the square root of a negative value for these inputs.")
    return math.sqrt(val)


AEROSPACE_FORMULAS.append(
    Formula(
        id="lift-coefficient",
        name="Lift Coefficient",
        category="Engineering",
        subcategory="Aerospace Engineering",
        equation="C_l = L / (½ρv²S)",
        description="Dimensionless coefficient relating lift force to dynamic pressure and wing area.",
        variables=[
            Variable("Cl", "Lift coefficient", "dimensionless"),
            Variable("L", "Lift force", "N"),
            Variable("rho", "Air density", "kg/m³"),
            Variable("v", "Airspeed", "m/s"),
            Variable("S", "Wing area", "m²"),
        ],
        keywords=["lift coefficient", "aerodynamics", "aerospace engineering", "wing"],
        solve={
            "Cl": lambda v: v["L"] / (0.5 * v["rho"] * v["v"] ** 2 * v["S"]),
            "L": lambda v: v["Cl"] * 0.5 * v["rho"] * v["v"] ** 2 * v["S"],
            "rho": lambda v: (2 * v["L"]) / (v["Cl"] * v["v"] ** 2 * v["S"]),
            "v": _lift_coefficient_v,
            "S": lambda v: (2 * v["L"]) / (v["Cl"] * v["rho"] * v["v"] ** 2),
        },
    )
)


def _drag_coefficient_v(v: dict[str, float]) -> float:
    val = (2 * v["D"]) / (v["Cd"] * v["rho"] * v["S"])
    if val < 0:
        raise ValueError("Cannot take the square root of a negative value for these inputs.")
    return math.sqrt(val)


AEROSPACE_FORMULAS.append(
    Formula(
        id="drag-coefficient",
        name="Drag Coefficient",
        category="Engineering",
        subcategory="Aerospace Engineering",
        equation="C_d = D / (½ρv²S)",
        description="Dimensionless coefficient relating drag force to dynamic pressure and reference area.",
        variables=[
            Variable("Cd", "Drag coefficient", "dimensionless"),
            Variable("D", "Drag force", "N"),
            Variable("rho", "Air density", "kg/m³"),
            Variable("v", "Airspeed", "m/s"),
            Variable("S", "Reference area", "m²"),
        ],
        keywords=["drag coefficient", "aerodynamics", "aerospace engineering"],
        solve={
            "Cd": lambda v: v["D"] / (0.5 * v["rho"] * v["v"] ** 2 * v["S"]),
            "D": lambda v: v["Cd"] * 0.5 * v["rho"] * v["v"] ** 2 * v["S"],
            "rho": lambda v: (2 * v["D"]) / (v["Cd"] * v["v"] ** 2 * v["S"]),
            "v": _drag_coefficient_v,
            "S": lambda v: (2 * v["D"]) / (v["Cd"] * v["rho"] * v["v"] ** 2),
        },
    )
)

AEROSPACE_FORMULAS.append(
    Formula(
        id="wing-loading",
        name="Wing Loading",
        category="Engineering",
        subcategory="Aerospace Engineering",
        equation="WL = W / S",
        description="Calculates the weight supported per unit of wing area.",
        variables=[
            Variable("WL", "Wing loading", "N/m²"),
            Variable("W", "Aircraft weight", "N"),
            Variable("S", "Wing area", "m²"),
        ],
        keywords=["wing loading", "aerospace engineering", "aircraft weight"],
        solve={
            "WL": lambda v: v["W"] / v["S"],
            "W": lambda v: v["WL"] * v["S"],
            "S": lambda v: v["W"] / v["WL"],
        },
    )
)

AEROSPACE_FORMULAS.append(
    Formula(
        id="mach-number",
        name="Mach Number",
        category="Engineering",
        subcategory="Aerospace Engineering",
        equation="M = v / a",
        description="Calculates the ratio of an object's speed to the local speed of sound.",
        variables=[
            Variable("M", "Mach number", "dimensionless"),
            Variable("v", "Velocity", "m/s"),
            Variable("a", "Speed of sound", "m/s"),
        ],
        keywords=["mach number", "speed of sound", "supersonic", "aerospace engineering"],
        solve={
            "M": lambda v: v["v"] / v["a"],
            "v": lambda v: v["M"] * v["a"],
            "a": lambda v: v["v"] / v["M"],
        },
    )
)

AEROSPACE_FORMULAS.append(
    Formula(
        id="specific-fuel-consumption",
        name="Specific Fuel Consumption",
        category="Engineering",
        subcategory="Aerospace Engineering",
        equation="SFC = Fuel / (Thrust × Time)",
        description="Calculates fuel mass consumed per unit of thrust per unit of time.",
        variables=[
            Variable("SFC", "Specific fuel consumption", "kg/(N·s)"),
            Variable("Fuel", "Fuel mass consumed", "kg"),
            Variable("Thrust", "Engine thrust", "N"),
            Variable("Time", "Operating time", "s"),
        ],
        keywords=["specific fuel consumption", "sfc", "aerospace engineering", "engine performance"],
        solve={
            "SFC": lambda v: v["Fuel"] / (v["Thrust"] * v["Time"]),
            "Fuel": lambda v: v["SFC"] * v["Thrust"] * v["Time"],
            "Thrust": lambda v: v["Fuel"] / (v["SFC"] * v["Time"]),
            "Time": lambda v: v["Fuel"] / (v["SFC"] * v["Thrust"]),
        },
    )
)

AEROSPACE_FORMULAS.append(
    Formula(
        id="thrust-to-weight-ratio",
        name="Thrust-to-Weight Ratio",
        category="Engineering",
        subcategory="Aerospace Engineering",
        equation="TWR = T / W",
        description="Calculates the ratio of thrust to weight for an aircraft or rocket, a key measure of performance.",
        variables=[
            Variable("TWR", "Thrust-to-weight ratio", "dimensionless"),
            Variable("T", "Thrust", "N"),
            Variable("W", "Weight", "N"),
        ],
        keywords=["thrust to weight ratio", "twr", "aerospace engineering", "rocket", "aircraft performance"],
        solve={
            "TWR": lambda v: v["T"] / v["W"],
            "T": lambda v: v["TWR"] * v["W"],
            "W": lambda v: v["T"] / v["TWR"],
        },
    )
)


def _rocket_equation_deltaV(v: dict[str, float]) -> float:
    if v["m0"] <= 0 or v["mf"] <= 0:
        raise ValueError("Initial and final mass must be positive.")
    return v["Isp"] * v["g0"] * math.log(v["m0"] / v["mf"])


def _rocket_equation_Isp(v: dict[str, float]) -> float:
    if v["m0"] <= 0 or v["mf"] <= 0:
        raise ValueError("Initial and final mass must be positive.")
    return v["deltaV"] / (v["g0"] * math.log(v["m0"] / v["mf"]))


def _rocket_equation_g0(v: dict[str, float]) -> float:
    if v["m0"] <= 0 or v["mf"] <= 0:
        raise ValueError("Initial and final mass must be positive.")
    return v["deltaV"] / (v["Isp"] * math.log(v["m0"] / v["mf"]))


AEROSPACE_FORMULAS.append(
    Formula(
        id="ideal-rocket-equation",
        name="Ideal Rocket Equation (Tsiolkovsky)",
        category="Engineering",
        subcategory="Aerospace Engineering",
        equation="Δv = I_spg₀ln(m₀/m_f)",
        description="Calculates a rocket's change in velocity from its specific impulse and the ratio of initial to final mass.",
        variables=[
            Variable("deltaV", "Change in velocity", "m/s"),
            Variable("Isp", "Specific impulse", "s"),
            Variable("g0", "Standard gravity", "m/s²"),
            Variable("m0", "Initial (wet) mass", "kg"),
            Variable("mf", "Final (dry) mass", "kg"),
        ],
        keywords=["rocket equation", "tsiolkovsky", "delta-v", "specific impulse", "aerospace engineering"],
        solve={
            "deltaV": _rocket_equation_deltaV,
            "Isp": _rocket_equation_Isp,
            "g0": _rocket_equation_g0,
            "m0": lambda v: v["mf"] * math.exp(v["deltaV"] / (v["Isp"] * v["g0"])),
            "mf": lambda v: v["m0"] * math.exp(-v["deltaV"] / (v["Isp"] * v["g0"])),
        },
    )
)

AEROSPACE_FORMULAS.append(
    Formula(
        id="specific-impulse",
        name="Specific Impulse",
        category="Engineering",
        subcategory="Aerospace Engineering",
        equation="I_sp = F / (ṁg₀)",
        description="Calculates the specific impulse of a rocket engine from thrust and propellant mass flow rate.",
        variables=[
            Variable("Isp", "Specific impulse", "s"),
            Variable("F", "Thrust", "N"),
            Variable("mdot", "Propellant mass flow rate", "kg/s"),
            Variable("g0", "Standard gravity", "m/s²"),
        ],
        keywords=["specific impulse", "isp", "rocket engine", "thrust", "aerospace engineering"],
        solve={
            "Isp": lambda v: v["F"] / (v["mdot"] * v["g0"]),
            "F": lambda v: v["Isp"] * v["mdot"] * v["g0"],
            "mdot": lambda v: v["F"] / (v["Isp"] * v["g0"]),
            "g0": lambda v: v["F"] / (v["Isp"] * v["mdot"]),
        },
    )
)
