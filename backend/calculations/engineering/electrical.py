"""Electrical engineering formulas: transformers, RC/RL circuits, AC power, reactance."""

import math

from ...models.formula import Formula, Variable

ELECTRICAL_FORMULAS: list[Formula] = []

ELECTRICAL_FORMULAS.append(
    Formula(
        id="transformer-voltage-ratio",
        name="Transformer Voltage Ratio",
        category="Engineering",
        subcategory="Electrical Engineering",
        equation="V_p / V_s = N_p / N_s",
        description="Relates the primary and secondary voltages of an ideal transformer to its turns ratio.",
        variables=[
            Variable("Vp", "Primary voltage", "V"),
            Variable("Vs", "Secondary voltage", "V"),
            Variable("Np", "Primary turns", "dimensionless"),
            Variable("Ns", "Secondary turns", "dimensionless"),
        ],
        keywords=["transformer", "voltage ratio", "turns ratio", "electrical engineering"],
        solve={
            "Vp": lambda v: (v["Vs"] * v["Np"]) / v["Ns"],
            "Vs": lambda v: (v["Vp"] * v["Ns"]) / v["Np"],
            "Np": lambda v: (v["Vp"] * v["Ns"]) / v["Vs"],
            "Ns": lambda v: (v["Vs"] * v["Np"]) / v["Vp"],
        },
    )
)

ELECTRICAL_FORMULAS.append(
    Formula(
        id="transformer-power",
        name="Transformer Power Balance",
        category="Engineering",
        subcategory="Electrical Engineering",
        equation="V_pI_p = V_sI_s",
        description="For an ideal transformer, input power equals output power.",
        variables=[
            Variable("Vp", "Primary voltage", "V"),
            Variable("Ip", "Primary current", "A"),
            Variable("Vs", "Secondary voltage", "V"),
            Variable("Is", "Secondary current", "A"),
        ],
        keywords=["transformer", "power balance", "ideal transformer", "electrical engineering"],
        solve={
            "Vp": lambda v: (v["Vs"] * v["Is"]) / v["Ip"],
            "Ip": lambda v: (v["Vs"] * v["Is"]) / v["Vp"],
            "Vs": lambda v: (v["Vp"] * v["Ip"]) / v["Is"],
            "Is": lambda v: (v["Vp"] * v["Ip"]) / v["Vs"],
        },
    )
)

ELECTRICAL_FORMULAS.append(
    Formula(
        id="rc-time-constant",
        name="RC Time Constant",
        category="Engineering",
        subcategory="Electrical Engineering",
        equation="τ = RC",
        description="Calculates the time constant of a resistor-capacitor circuit during charging or discharging.",
        variables=[
            Variable("tau", "Time constant", "s"),
            Variable("R", "Resistance", "Ω"),
            Variable("C", "Capacitance", "F"),
        ],
        keywords=["rc circuit", "time constant", "capacitor", "electrical engineering"],
        solve={
            "tau": lambda v: v["R"] * v["C"],
            "R": lambda v: v["tau"] / v["C"],
            "C": lambda v: v["tau"] / v["R"],
        },
    )
)

ELECTRICAL_FORMULAS.append(
    Formula(
        id="rl-time-constant",
        name="RL Time Constant",
        category="Engineering",
        subcategory="Electrical Engineering",
        equation="τ = L / R",
        description="Calculates the time constant of a resistor-inductor circuit.",
        variables=[
            Variable("tau", "Time constant", "s"),
            Variable("L", "Inductance", "H"),
            Variable("R", "Resistance", "Ω"),
        ],
        keywords=["rl circuit", "time constant", "inductor", "electrical engineering"],
        solve={
            "tau": lambda v: v["L"] / v["R"],
            "L": lambda v: v["tau"] * v["R"],
            "R": lambda v: v["L"] / v["tau"],
        },
    )
)

ELECTRICAL_FORMULAS.append(
    Formula(
        id="lc-resonant-frequency",
        name="Resonant Frequency (LC Circuit)",
        category="Engineering",
        subcategory="Electrical Engineering",
        equation="f = 1 / (2π√(LC))",
        description="Calculates the resonant frequency of an inductor-capacitor circuit.",
        variables=[
            Variable("f", "Resonant frequency", "Hz"),
            Variable("L", "Inductance", "H"),
            Variable("C", "Capacitance", "F"),
        ],
        keywords=["resonant frequency", "lc circuit", "electrical engineering", "resonance"],
        solve={
            "f": lambda v: 1 / (2 * math.pi * math.sqrt(v["L"] * v["C"])),
            "L": lambda v: 1 / (v["C"] * (2 * math.pi * v["f"]) ** 2),
            "C": lambda v: 1 / (v["L"] * (2 * math.pi * v["f"]) ** 2),
        },
    )
)

ELECTRICAL_FORMULAS.append(
    Formula(
        id="ac-rms-voltage",
        name="AC RMS Voltage",
        category="Engineering",
        subcategory="Electrical Engineering",
        equation="V_rms = V_peak / √2",
        description="Calculates the root-mean-square voltage of a sinusoidal AC signal from its peak voltage.",
        variables=[
            Variable("Vrms", "RMS voltage", "V"),
            Variable("Vpeak", "Peak voltage", "V"),
        ],
        keywords=["rms voltage", "ac circuits", "peak voltage", "electrical engineering", "alternating current"],
        solve={
            "Vrms": lambda v: v["Vpeak"] / math.sqrt(2),
            "Vpeak": lambda v: v["Vrms"] * math.sqrt(2),
        },
    )
)

ELECTRICAL_FORMULAS.append(
    Formula(
        id="power-factor",
        name="Power Factor",
        category="Engineering",
        subcategory="Electrical Engineering",
        equation="PF = P / S",
        description="Calculates the power factor of an AC circuit as the ratio of real power to apparent power.",
        variables=[
            Variable("PF", "Power factor", "dimensionless"),
            Variable("P", "Real power", "W"),
            Variable("S", "Apparent power", "VA"),
        ],
        keywords=["power factor", "ac circuits", "real power", "apparent power", "electrical engineering"],
        solve={
            "PF": lambda v: v["P"] / v["S"],
            "P": lambda v: v["PF"] * v["S"],
            "S": lambda v: v["P"] / v["PF"],
        },
    )
)


def _ac_real_power_theta(v: dict[str, float]) -> float:
    ratio = v["P"] / (v["Vrms"] * v["Irms"])
    if ratio < -1 or ratio > 1:
        raise ValueError("No phase angle satisfies these power, voltage, and current values.")
    return math.degrees(math.acos(ratio))


ELECTRICAL_FORMULAS.append(
    Formula(
        id="ac-real-power",
        name="AC Real Power",
        category="Engineering",
        subcategory="Electrical Engineering",
        equation="P = V_rmsI_rms cos(θ)",
        description="Calculates the real power delivered in an AC circuit from RMS voltage, RMS current, and the phase angle.",
        variables=[
            Variable("P", "Real power", "W"),
            Variable("Vrms", "RMS voltage", "V"),
            Variable("Irms", "RMS current", "A"),
            Variable("theta", "Phase angle", "°"),
        ],
        keywords=["ac power", "real power", "phase angle", "electrical engineering", "alternating current"],
        solve={
            "P": lambda v: v["Vrms"] * v["Irms"] * math.cos(math.radians(v["theta"])),
            "Vrms": lambda v: v["P"] / (v["Irms"] * math.cos(math.radians(v["theta"]))),
            "Irms": lambda v: v["P"] / (v["Vrms"] * math.cos(math.radians(v["theta"]))),
            "theta": _ac_real_power_theta,
        },
    )
)

ELECTRICAL_FORMULAS.append(
    Formula(
        id="capacitive-reactance",
        name="Capacitive Reactance",
        category="Engineering",
        subcategory="Electrical Engineering",
        equation="X_c = 1 / (2πfC)",
        description="Calculates the opposition a capacitor presents to AC current at a given frequency.",
        variables=[
            Variable("Xc", "Capacitive reactance", "Ω"),
            Variable("f", "Frequency", "Hz"),
            Variable("C", "Capacitance", "F"),
        ],
        keywords=["capacitive reactance", "capacitor", "ac circuits", "electrical engineering", "reactance"],
        solve={
            "Xc": lambda v: 1 / (2 * math.pi * v["f"] * v["C"]),
            "f": lambda v: 1 / (2 * math.pi * v["C"] * v["Xc"]),
            "C": lambda v: 1 / (2 * math.pi * v["f"] * v["Xc"]),
        },
    )
)

ELECTRICAL_FORMULAS.append(
    Formula(
        id="inductive-reactance",
        name="Inductive Reactance",
        category="Engineering",
        subcategory="Electrical Engineering",
        equation="X_L = 2πfL",
        description="Calculates the opposition an inductor presents to AC current at a given frequency.",
        variables=[
            Variable("XL", "Inductive reactance", "Ω"),
            Variable("f", "Frequency", "Hz"),
            Variable("L", "Inductance", "H"),
        ],
        keywords=["inductive reactance", "inductor", "ac circuits", "electrical engineering", "reactance"],
        solve={
            "XL": lambda v: 2 * math.pi * v["f"] * v["L"],
            "f": lambda v: v["XL"] / (2 * math.pi * v["L"]),
            "L": lambda v: v["XL"] / (2 * math.pi * v["f"]),
        },
    )
)
