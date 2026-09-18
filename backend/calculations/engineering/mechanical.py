"""Mechanical engineering formulas: pulleys, inclined planes, shafts, gears, pumps."""

import math

from ...models.formula import Formula, Variable

MECHANICAL_FORMULAS: list[Formula] = []

MECHANICAL_FORMULAS.append(
    Formula(
        id="pulley-mechanical-advantage",
        name="Pulley Mechanical Advantage",
        category="Engineering",
        subcategory="Mechanical Engineering",
        equation="MA = n",
        description="The ideal mechanical advantage of a pulley system equals the number of rope segments supporting the load.",
        variables=[
            Variable("MA", "Mechanical advantage", "dimensionless"),
            Variable("n", "Number of supporting rope segments", "dimensionless"),
        ],
        keywords=["pulley", "mechanical advantage", "simple machines", "mechanical engineering"],
        solve={
            "MA": lambda v: v["n"],
            "n": lambda v: v["MA"],
        },
    )
)


def _incline_plane_force_theta(v: dict[str, float]) -> float:
    ratio = v["F"] / (v["m"] * v["g"])
    if ratio < -1 or ratio > 1:
        raise ValueError("No incline angle satisfies these force, mass, and gravity values.")
    return math.degrees(math.asin(ratio))


MECHANICAL_FORMULAS.append(
    Formula(
        id="incline-plane-force",
        name="Inclined Plane Force",
        category="Engineering",
        subcategory="Mechanical Engineering",
        equation="F = mg sin(θ)",
        description="Calculates the component of an object's weight acting along an inclined plane.",
        variables=[
            Variable("F", "Force along incline", "N"),
            Variable("m", "Mass", "kg"),
            Variable("g", "Gravitational acceleration", "m/s²"),
            Variable("theta", "Angle of incline", "°"),
        ],
        keywords=["inclined plane", "incline", "force", "mechanical engineering", "ramp"],
        solve={
            "F": lambda v: v["m"] * v["g"] * math.sin(math.radians(v["theta"])),
            "m": lambda v: v["F"] / (v["g"] * math.sin(math.radians(v["theta"]))),
            "g": lambda v: v["F"] / (v["m"] * math.sin(math.radians(v["theta"]))),
            "theta": _incline_plane_force_theta,
        },
    )
)

MECHANICAL_FORMULAS.append(
    Formula(
        id="shaft-power-transmission",
        name="Shaft Power Transmission",
        category="Engineering",
        subcategory="Mechanical Engineering",
        equation="P = τω",
        description="Calculates the power transmitted by a rotating shaft from torque and angular velocity.",
        variables=[
            Variable("P", "Power", "W"),
            Variable("tau", "Torque", "N·m"),
            Variable("omega", "Angular velocity", "rad/s"),
        ],
        keywords=["shaft power", "power transmission", "torque", "mechanical engineering"],
        solve={
            "P": lambda v: v["tau"] * v["omega"],
            "tau": lambda v: v["P"] / v["omega"],
            "omega": lambda v: v["P"] / v["tau"],
        },
    )
)

MECHANICAL_FORMULAS.append(
    Formula(
        id="pump-power",
        name="Pump Power",
        category="Engineering",
        subcategory="Mechanical Engineering",
        equation="P = ρgQh",
        description="Calculates the hydraulic power required to pump a fluid against a given height difference.",
        variables=[
            Variable("P", "Power", "W"),
            Variable("rho", "Fluid density", "kg/m³"),
            Variable("g", "Gravitational acceleration", "m/s²"),
            Variable("Q", "Volumetric flow rate", "m³/s"),
            Variable("h", "Height difference", "m"),
        ],
        keywords=["pump power", "fluid", "mechanical engineering", "hydraulic power"],
        solve={
            "P": lambda v: v["rho"] * v["g"] * v["Q"] * v["h"],
            "rho": lambda v: v["P"] / (v["g"] * v["Q"] * v["h"]),
            "g": lambda v: v["P"] / (v["rho"] * v["Q"] * v["h"]),
            "Q": lambda v: v["P"] / (v["rho"] * v["g"] * v["h"]),
            "h": lambda v: v["P"] / (v["rho"] * v["g"] * v["Q"]),
        },
    )
)

MECHANICAL_FORMULAS.append(
    Formula(
        id="gear-ratio",
        name="Gear Ratio",
        category="Engineering",
        subcategory="Mechanical Engineering",
        equation="GR = N_driven / N_driver",
        description="Calculates the gear ratio of a two-gear system from the number of teeth on the driven and driver gears.",
        variables=[
            Variable("GR", "Gear ratio", "dimensionless"),
            Variable("Ndriven", "Teeth on driven gear", "dimensionless"),
            Variable("Ndriver", "Teeth on driver gear", "dimensionless"),
        ],
        keywords=["gear ratio", "gears", "mechanical engineering", "teeth ratio", "speed reduction"],
        solve={
            "GR": lambda v: v["Ndriven"] / v["Ndriver"],
            "Ndriven": lambda v: v["GR"] * v["Ndriver"],
            "Ndriver": lambda v: v["Ndriven"] / v["GR"],
        },
    )
)

MECHANICAL_FORMULAS.append(
    Formula(
        id="belt-pulley-speed-ratio",
        name="Belt/Pulley Speed Ratio",
        category="Engineering",
        subcategory="Mechanical Engineering",
        equation="N₁d₁ = N₂d₂",
        description="Relates the rotational speeds and diameters of two pulleys connected by a belt.",
        variables=[
            Variable("N1", "Speed of pulley 1", "rpm"),
            Variable("d1", "Diameter of pulley 1", "m"),
            Variable("N2", "Speed of pulley 2", "rpm"),
            Variable("d2", "Diameter of pulley 2", "m"),
        ],
        keywords=["belt drive", "pulley", "speed ratio", "mechanical engineering"],
        solve={
            "N1": lambda v: (v["N2"] * v["d2"]) / v["d1"],
            "d1": lambda v: (v["N2"] * v["d2"]) / v["N1"],
            "N2": lambda v: (v["N1"] * v["d1"]) / v["d2"],
            "d2": lambda v: (v["N1"] * v["d1"]) / v["N2"],
        },
    )
)

MECHANICAL_FORMULAS.append(
    Formula(
        id="shaft-torsional-shear-stress",
        name="Torsional Shear Stress (Solid Circular Shaft)",
        category="Engineering",
        subcategory="Mechanical Engineering",
        equation="τ = 16T / (πD³)",
        description="Calculates the maximum shear stress at the surface of a solid circular shaft under torsion.",
        variables=[
            Variable("tau", "Shear stress", "Pa"),
            Variable("T", "Applied torque", "N·m"),
            Variable("D", "Shaft diameter", "m"),
        ],
        keywords=["torsion", "shear stress", "shaft", "mechanical engineering", "torque"],
        solve={
            "tau": lambda v: (16 * v["T"]) / (math.pi * v["D"] ** 3),
            "T": lambda v: (v["tau"] * math.pi * v["D"] ** 3) / 16,
            "D": lambda v: math.cbrt((16 * v["T"]) / (math.pi * v["tau"])),
        },
    )
)

MECHANICAL_FORMULAS.append(
    Formula(
        id="mechanical-efficiency",
        name="Mechanical Efficiency",
        category="Engineering",
        subcategory="Mechanical Engineering",
        equation="η = P_out / P_in",
        description="Calculates the efficiency of a mechanical system as the ratio of output power to input power.",
        variables=[
            Variable("eta", "Efficiency", "dimensionless"),
            Variable("Pout", "Output power", "W"),
            Variable("Pin", "Input power", "W"),
        ],
        keywords=["mechanical efficiency", "efficiency", "power", "mechanical engineering"],
        solve={
            "eta": lambda v: v["Pout"] / v["Pin"],
            "Pout": lambda v: v["eta"] * v["Pin"],
            "Pin": lambda v: v["Pout"] / v["eta"],
        },
    )
)

MECHANICAL_FORMULAS.append(
    Formula(
        id="angular-velocity-from-rpm",
        name="Angular Velocity from RPM",
        category="Engineering",
        subcategory="Mechanical Engineering",
        equation="ω = 2πN / 60",
        description="Converts a rotational speed in revolutions per minute to angular velocity in radians per second.",
        variables=[
            Variable("omega", "Angular velocity", "rad/s"),
            Variable("N", "Rotational speed", "rpm"),
        ],
        keywords=["angular velocity", "rpm", "rotational speed", "mechanical engineering", "conversion"],
        solve={
            "omega": lambda v: (2 * math.pi * v["N"]) / 60,
            "N": lambda v: (60 * v["omega"]) / (2 * math.pi),
        },
    )
)
