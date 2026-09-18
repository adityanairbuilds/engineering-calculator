"""Circuit formulas: Ohm's law, resistance combinations, power, capacitance."""

import math

from ...models.formula import Formula, Variable

CIRCUITS_FORMULAS: list[Formula] = []

CIRCUITS_FORMULAS.append(
    Formula(
        id="ohms-law",
        name="Ohm's Law",
        category="Physics",
        subcategory="Circuits",
        equation="V = IR",
        description="Relates voltage, current, and resistance in a circuit.",
        variables=[
            Variable("V", "Voltage", "V"),
            Variable("I", "Current", "A"),
            Variable("R", "Resistance", "Ω"),
        ],
        keywords=["ohms law", "ohm's law", "voltage", "current", "resistance", "electric resistance", "v=ir"],
        solve={
            "V": lambda v: v["I"] * v["R"],
            "I": lambda v: v["V"] / v["R"],
            "R": lambda v: v["V"] / v["I"],
        },
    )
)

CIRCUITS_FORMULAS.append(
    Formula(
        id="electrical-power",
        name="Electrical Power",
        category="Physics",
        subcategory="Circuits",
        equation="P = IV",
        description="Calculates electrical power from current and voltage.",
        variables=[
            Variable("P", "Power", "W"),
            Variable("I", "Current", "A"),
            Variable("V", "Voltage", "V"),
        ],
        keywords=["electrical power", "power", "watts", "p=iv"],
        solve={
            "P": lambda v: v["I"] * v["V"],
            "I": lambda v: v["P"] / v["V"],
            "V": lambda v: v["P"] / v["I"],
        },
    )
)

CIRCUITS_FORMULAS.append(
    Formula(
        id="series-resistance",
        name="Series Resistance",
        category="Physics",
        subcategory="Circuits",
        equation="R_total = R₁ + R₂",
        description="Combines two resistors in series. Add more R terms by hand for additional resistors.",
        variables=[
            Variable("Rt", "Total resistance", "Ω"),
            Variable("R1", "Resistor 1", "Ω"),
            Variable("R2", "Resistor 2", "Ω"),
        ],
        keywords=["series resistance", "resistors in series", "total resistance"],
        solve={
            "Rt": lambda v: v["R1"] + v["R2"],
            "R1": lambda v: v["Rt"] - v["R2"],
            "R2": lambda v: v["Rt"] - v["R1"],
        },
    )
)


def _parallel_resistance_r1(v: dict[str, float]) -> float:
    if v["R2"] <= v["Rt"]:
        raise ValueError("R2 must be greater than the total resistance.")
    return (v["Rt"] * v["R2"]) / (v["R2"] - v["Rt"])


def _parallel_resistance_r2(v: dict[str, float]) -> float:
    if v["R1"] <= v["Rt"]:
        raise ValueError("R1 must be greater than the total resistance.")
    return (v["Rt"] * v["R1"]) / (v["R1"] - v["Rt"])


CIRCUITS_FORMULAS.append(
    Formula(
        id="parallel-resistance",
        name="Parallel Resistance",
        category="Physics",
        subcategory="Circuits",
        equation="1/R_total = 1/R₁ + 1/R₂",
        description="Combines two resistors in parallel.",
        variables=[
            Variable("Rt", "Total resistance", "Ω"),
            Variable("R1", "Resistor 1", "Ω"),
            Variable("R2", "Resistor 2", "Ω"),
        ],
        keywords=["parallel resistance", "resistors in parallel", "total resistance"],
        solve={
            "Rt": lambda v: (v["R1"] * v["R2"]) / (v["R1"] + v["R2"]),
            "R1": _parallel_resistance_r1,
            "R2": _parallel_resistance_r2,
        },
    )
)


def _power_current_resistance_i(v: dict[str, float]) -> float:
    sq = v["P"] / v["R"]
    if sq < 0:
        raise ValueError("P/R is negative — no real current.")
    return math.sqrt(sq)


CIRCUITS_FORMULAS.append(
    Formula(
        id="power-current-resistance",
        name="Electrical Power (Current & Resistance)",
        category="Physics",
        subcategory="Circuits",
        equation="P = I²R",
        description="Calculates electrical power dissipated from current and resistance.",
        variables=[
            Variable("P", "Power", "W"),
            Variable("I", "Current", "A"),
            Variable("R", "Resistance", "Ω"),
        ],
        keywords=["power", "current", "resistance", "watts", "dissipation", "i squared r"],
        solve={
            "P": lambda v: v["I"] ** 2 * v["R"],
            "I": _power_current_resistance_i,
            "R": lambda v: v["P"] / v["I"] ** 2,
        },
    )
)


def _power_voltage_resistance_v(v: dict[str, float]) -> float:
    sq = v["P"] * v["R"]
    if sq < 0:
        raise ValueError("P·R is negative — no real voltage.")
    return math.sqrt(sq)


CIRCUITS_FORMULAS.append(
    Formula(
        id="power-voltage-resistance",
        name="Electrical Power (Voltage & Resistance)",
        category="Physics",
        subcategory="Circuits",
        equation="P = V²/R",
        description="Calculates electrical power dissipated from voltage and resistance.",
        variables=[
            Variable("P", "Power", "W"),
            Variable("V", "Voltage", "V"),
            Variable("R", "Resistance", "Ω"),
        ],
        keywords=["power", "voltage", "resistance", "watts", "dissipation", "v squared over r"],
        solve={
            "P": lambda v: v["V"] ** 2 / v["R"],
            "V": _power_voltage_resistance_v,
            "R": lambda v: v["V"] ** 2 / v["P"],
        },
    )
)

CIRCUITS_FORMULAS.append(
    Formula(
        id="resistivity",
        name="Resistivity",
        category="Physics",
        subcategory="Circuits",
        equation="R = ρL / A",
        description="Calculates the resistance of a conductor from its resistivity, length, and cross-sectional area.",
        variables=[
            Variable("R", "Resistance", "Ω"),
            Variable("rho", "Resistivity", "Ω·m"),
            Variable("L", "Length of conductor", "m"),
            Variable("A", "Cross-sectional area", "m²"),
        ],
        keywords=["resistivity", "resistance", "conductor", "circuit", "wire"],
        solve={
            "R": lambda v: (v["rho"] * v["L"]) / v["A"],
            "rho": lambda v: (v["R"] * v["A"]) / v["L"],
            "L": lambda v: (v["R"] * v["A"]) / v["rho"],
            "A": lambda v: (v["rho"] * v["L"]) / v["R"],
        },
    )
)

CIRCUITS_FORMULAS.append(
    Formula(
        id="capacitance",
        name="Capacitance",
        category="Physics",
        subcategory="Circuits",
        equation="C = Q / V",
        description="Calculates capacitance from stored charge and voltage.",
        variables=[
            Variable("C", "Capacitance", "F"),
            Variable("Q", "Charge", "C"),
            Variable("V", "Voltage", "V"),
        ],
        keywords=["capacitance", "capacitor", "charge", "voltage", "circuit"],
        solve={
            "C": lambda v: v["Q"] / v["V"],
            "Q": lambda v: v["C"] * v["V"],
            "V": lambda v: v["Q"] / v["C"],
        },
    )
)

CIRCUITS_FORMULAS.append(
    Formula(
        id="parallel-plate-capacitor",
        name="Parallel Plate Capacitor",
        category="Physics",
        subcategory="Circuits",
        equation="C = ε₀εᵣA / d",
        description="Calculates the capacitance of a parallel plate capacitor from plate area, separation, and the dielectric.",
        variables=[
            Variable("C", "Capacitance", "F"),
            Variable("eps0", "Permittivity of free space (≈8.854×10⁻¹²)", "F/m"),
            Variable("epsR", "Relative permittivity of dielectric", "dimensionless"),
            Variable("A", "Plate area", "m²"),
            Variable("d", "Plate separation", "m"),
        ],
        keywords=["parallel plate", "capacitor", "capacitance", "circuit", "dielectric"],
        solve={
            "C": lambda v: (v["eps0"] * v["epsR"] * v["A"]) / v["d"],
            "eps0": lambda v: (v["C"] * v["d"]) / (v["epsR"] * v["A"]),
            "epsR": lambda v: (v["C"] * v["d"]) / (v["eps0"] * v["A"]),
            "A": lambda v: (v["C"] * v["d"]) / (v["eps0"] * v["epsR"]),
            "d": lambda v: (v["eps0"] * v["epsR"] * v["A"]) / v["C"],
        },
    )
)
