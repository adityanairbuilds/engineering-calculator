"""Thermodynamics formulas: temperature, heat, gas law, entropy, heat engines."""

from ...models.formula import Formula, Variable

THERMODYNAMICS_FORMULAS: list[Formula] = []

THERMODYNAMICS_FORMULAS.append(
    Formula(
        id="temperature-conversion",
        name="Temperature Conversion (Celsius to Kelvin)",
        category="Physics",
        subcategory="Thermodynamics",
        equation="T(K) = T(°C) + 273.15",
        description="Converts a temperature between the Celsius and Kelvin scales.",
        variables=[
            Variable("TK", "Temperature in Kelvin", "K"),
            Variable("TC", "Temperature in Celsius", "°C"),
        ],
        keywords=["temperature", "conversion", "celsius", "kelvin", "thermodynamics"],
        solve={
            "TK": lambda v: v["TC"] + 273.15,
            "TC": lambda v: v["TK"] - 273.15,
        },
    )
)

THERMODYNAMICS_FORMULAS.append(
    Formula(
        id="heat-capacity",
        name="Heat Capacity (Specific Heat)",
        category="Physics",
        subcategory="Thermodynamics",
        equation="Q = mcΔT",
        description="Calculates the heat energy required to change the temperature of a substance.",
        variables=[
            Variable("Q", "Heat energy", "J"),
            Variable("m", "Mass", "kg"),
            Variable("c", "Specific heat capacity", "J/(kg·K)"),
            Variable("dT", "Temperature change", "K"),
        ],
        keywords=["heat capacity", "specific heat", "temperature", "energy", "thermal"],
        solve={
            "Q": lambda v: v["m"] * v["c"] * v["dT"],
            "m": lambda v: v["Q"] / (v["c"] * v["dT"]),
            "c": lambda v: v["Q"] / (v["m"] * v["dT"]),
            "dT": lambda v: v["Q"] / (v["m"] * v["c"]),
        },
    )
)

THERMODYNAMICS_FORMULAS.append(
    Formula(
        id="latent-heat",
        name="Latent Heat",
        category="Physics",
        subcategory="Thermodynamics",
        equation="Q = mL",
        description="Calculates the heat energy absorbed or released during a phase change at constant temperature.",
        variables=[
            Variable("Q", "Heat energy", "J"),
            Variable("m", "Mass", "kg"),
            Variable("L", "Latent heat of fusion/vaporization", "J/kg"),
        ],
        keywords=["latent heat", "phase change", "melting", "boiling", "vaporization", "fusion"],
        solve={
            "Q": lambda v: v["m"] * v["L"],
            "m": lambda v: v["Q"] / v["L"],
            "L": lambda v: v["Q"] / v["m"],
        },
    )
)

THERMODYNAMICS_FORMULAS.append(
    Formula(
        id="thermal-expansion",
        name="Linear Thermal Expansion",
        category="Physics",
        subcategory="Thermodynamics",
        equation="ΔL = L₀αΔT",
        description="Calculates the change in length of a material due to a change in temperature.",
        variables=[
            Variable("dL", "Change in length", "m"),
            Variable("L0", "Original length", "m"),
            Variable("alpha", "Coefficient of linear expansion", "1/K"),
            Variable("dT", "Temperature change", "K"),
        ],
        keywords=["thermal expansion", "temperature", "length", "expansion coefficient"],
        solve={
            "dL": lambda v: v["L0"] * v["alpha"] * v["dT"],
            "L0": lambda v: v["dL"] / (v["alpha"] * v["dT"]),
            "alpha": lambda v: v["dL"] / (v["L0"] * v["dT"]),
            "dT": lambda v: v["dL"] / (v["L0"] * v["alpha"]),
        },
    )
)

THERMODYNAMICS_FORMULAS.append(
    Formula(
        id="ideal-gas-law",
        name="Ideal Gas Law",
        category="Physics",
        subcategory="Thermodynamics",
        equation="PV = nRT",
        description="Relates pressure, volume, amount of substance, and temperature for an ideal gas.",
        variables=[
            Variable("P", "Pressure", "Pa"),
            Variable("V", "Volume", "m³"),
            Variable("n", "Number of moles", "mol"),
            Variable("R", "Gas constant (≈8.314)", "J/(mol·K)"),
            Variable("T", "Temperature", "K"),
        ],
        keywords=["ideal gas law", "pressure", "volume", "temperature", "moles", "gas constant"],
        solve={
            "P": lambda v: (v["n"] * v["R"] * v["T"]) / v["V"],
            "V": lambda v: (v["n"] * v["R"] * v["T"]) / v["P"],
            "n": lambda v: (v["P"] * v["V"]) / (v["R"] * v["T"]),
            "R": lambda v: (v["P"] * v["V"]) / (v["n"] * v["T"]),
            "T": lambda v: (v["P"] * v["V"]) / (v["n"] * v["R"]),
        },
    )
)

THERMODYNAMICS_FORMULAS.append(
    Formula(
        id="first-law-thermodynamics",
        name="First Law of Thermodynamics",
        category="Physics",
        subcategory="Thermodynamics",
        equation="ΔU = Q - W",
        description="Relates the change in internal energy of a system to heat added and work done by the system.",
        variables=[
            Variable("dU", "Change in internal energy", "J"),
            Variable("Q", "Heat added to system", "J"),
            Variable("W", "Work done by system", "J"),
        ],
        keywords=["first law of thermodynamics", "internal energy", "heat", "work", "thermodynamics"],
        solve={
            "dU": lambda v: v["Q"] - v["W"],
            "Q": lambda v: v["dU"] + v["W"],
            "W": lambda v: v["Q"] - v["dU"],
        },
    )
)

THERMODYNAMICS_FORMULAS.append(
    Formula(
        id="entropy",
        name="Entropy Change",
        category="Physics",
        subcategory="Thermodynamics",
        equation="ΔS = Q / T",
        description="Calculates the change in entropy of a system for a reversible heat transfer at constant temperature.",
        variables=[
            Variable("dS", "Change in entropy", "J/K"),
            Variable("Q", "Heat transferred", "J"),
            Variable("T", "Temperature", "K"),
        ],
        keywords=["entropy", "thermodynamics", "disorder", "heat", "temperature"],
        solve={
            "dS": lambda v: v["Q"] / v["T"],
            "Q": lambda v: v["dS"] * v["T"],
            "T": lambda v: v["Q"] / v["dS"],
        },
    )
)

THERMODYNAMICS_FORMULAS.append(
    Formula(
        id="carnot-efficiency",
        name="Carnot Efficiency",
        category="Physics",
        subcategory="Thermodynamics",
        equation="η = 1 - T_c / T_h",
        description="Calculates the maximum possible efficiency of a heat engine operating between a hot and cold reservoir. Temperatures must be in Kelvin.",
        variables=[
            Variable("eta", "Carnot efficiency (0 to 1)", "dimensionless"),
            Variable("Tc", "Cold reservoir temperature", "K"),
            Variable("Th", "Hot reservoir temperature", "K"),
        ],
        keywords=["carnot efficiency", "heat engine", "thermodynamics", "efficiency", "carnot cycle"],
        solve={
            "eta": lambda v: 1 - v["Tc"] / v["Th"],
            "Tc": lambda v: v["Th"] * (1 - v["eta"]),
            "Th": lambda v: v["Tc"] / (1 - v["eta"]),
        },
    )
)

THERMODYNAMICS_FORMULAS.append(
    Formula(
        id="heat-conduction",
        name="Heat Conduction (Fourier's Law)",
        category="Physics",
        subcategory="Thermodynamics",
        equation="P = kAΔT / d",
        description="Calculates the steady-state rate of heat conduction through a slab of material.",
        variables=[
            Variable("P", "Heat transfer rate", "W"),
            Variable("k", "Thermal conductivity", "W/(m·K)"),
            Variable("A", "Cross-sectional area", "m²"),
            Variable("dT", "Temperature difference", "K"),
            Variable("d", "Thickness", "m"),
        ],
        keywords=["heat conduction", "fourier's law", "thermal conductivity", "heat transfer", "insulation"],
        solve={
            "P": lambda v: (v["k"] * v["A"] * v["dT"]) / v["d"],
            "k": lambda v: (v["P"] * v["d"]) / (v["A"] * v["dT"]),
            "A": lambda v: (v["P"] * v["d"]) / (v["k"] * v["dT"]),
            "dT": lambda v: (v["P"] * v["d"]) / (v["k"] * v["A"]),
            "d": lambda v: (v["k"] * v["A"] * v["dT"]) / v["P"],
        },
    )
)
