"""Thermodynamics formulas: COP, heat transfer (conduction, convection, radiation), heat capacity."""

from ...models.formula import Formula, Variable

THERMODYNAMICS_FORMULAS: list[Formula] = []

THERMODYNAMICS_FORMULAS.append(
    Formula(
        id="cop-refrigeration",
        name="Coefficient of Performance (Refrigeration)",
        category="Engineering",
        subcategory="Thermodynamics",
        equation="COP = Q_c / W",
        description="Measures the efficiency of a refrigeration cycle as heat removed per unit of work input.",
        variables=[
            Variable("COP", "Coefficient of performance", "dimensionless"),
            Variable("Qc", "Heat removed from cold space", "J"),
            Variable("W", "Work input", "J"),
        ],
        keywords=["coefficient of performance", "refrigeration", "cooling", "thermodynamics"],
        solve={
            "COP": lambda v: v["Qc"] / v["W"],
            "Qc": lambda v: v["COP"] * v["W"],
            "W": lambda v: v["Qc"] / v["COP"],
        },
    )
)

THERMODYNAMICS_FORMULAS.append(
    Formula(
        id="cop-heat-pump",
        name="Coefficient of Performance (Heat Pump)",
        category="Engineering",
        subcategory="Thermodynamics",
        equation="COP_hp = Q_h / W",
        description="Measures the efficiency of a heat pump as heat delivered per unit of work input.",
        variables=[
            Variable("COPhp", "Coefficient of performance (heat pump)", "dimensionless"),
            Variable("Qh", "Heat delivered to hot space", "J"),
            Variable("W", "Work input", "J"),
        ],
        keywords=["coefficient of performance", "heat pump", "heating", "thermodynamics"],
        solve={
            "COPhp": lambda v: v["Qh"] / v["W"],
            "Qh": lambda v: v["COPhp"] * v["W"],
            "W": lambda v: v["Qh"] / v["COPhp"],
        },
    )
)

THERMODYNAMICS_FORMULAS.append(
    Formula(
        id="heat-conduction-fourier",
        name="Fourier's Law of Heat Conduction",
        category="Engineering",
        subcategory="Thermodynamics",
        equation="Q = kA(ΔT) / d",
        description="Calculates the rate of heat transfer by conduction through a material.",
        variables=[
            Variable("Q", "Heat transfer rate", "W"),
            Variable("k", "Thermal conductivity", "W/(m·K)"),
            Variable("A", "Area", "m²"),
            Variable("deltaT", "Temperature difference", "K"),
            Variable("d", "Material thickness", "m"),
        ],
        keywords=["heat conduction", "fourier law", "thermal conductivity", "thermodynamics", "heat transfer"],
        solve={
            "Q": lambda v: (v["k"] * v["A"] * v["deltaT"]) / v["d"],
            "k": lambda v: (v["Q"] * v["d"]) / (v["A"] * v["deltaT"]),
            "A": lambda v: (v["Q"] * v["d"]) / (v["k"] * v["deltaT"]),
            "deltaT": lambda v: (v["Q"] * v["d"]) / (v["k"] * v["A"]),
            "d": lambda v: (v["k"] * v["A"] * v["deltaT"]) / v["Q"],
        },
    )
)

THERMODYNAMICS_FORMULAS.append(
    Formula(
        id="heat-convection-newton",
        name="Newton's Law of Cooling",
        category="Engineering",
        subcategory="Thermodynamics",
        equation="Q = hA(ΔT)",
        description="Calculates the rate of heat transfer by convection from a surface to a surrounding fluid.",
        variables=[
            Variable("Q", "Heat transfer rate", "W"),
            Variable("h", "Convection heat transfer coefficient", "W/(m²·K)"),
            Variable("A", "Surface area", "m²"),
            Variable("deltaT", "Temperature difference", "K"),
        ],
        keywords=["heat convection", "newton cooling", "thermodynamics", "heat transfer"],
        solve={
            "Q": lambda v: v["h"] * v["A"] * v["deltaT"],
            "h": lambda v: v["Q"] / (v["A"] * v["deltaT"]),
            "A": lambda v: v["Q"] / (v["h"] * v["deltaT"]),
            "deltaT": lambda v: v["Q"] / (v["h"] * v["A"]),
        },
    )
)


def _stefan_boltzmann_T(v: dict[str, float]) -> float:
    val = v["Q"] / (v["epsilon"] * v["sigma"] * v["A"])
    if val < 0:
        raise ValueError("Cannot take the fourth root of a negative value for these inputs.")
    return val**0.25


THERMODYNAMICS_FORMULAS.append(
    Formula(
        id="heat-radiation-stefan-boltzmann",
        name="Stefan-Boltzmann Law",
        category="Engineering",
        subcategory="Thermodynamics",
        equation="Q = εσAT⁴",
        description="Calculates the rate of heat transfer by radiation from a surface.",
        variables=[
            Variable("Q", "Radiant heat transfer rate", "W"),
            Variable("epsilon", "Emissivity", "dimensionless"),
            Variable("sigma", "Stefan-Boltzmann constant", "W/(m²·K⁴)"),
            Variable("A", "Surface area", "m²"),
            Variable("T", "Absolute temperature", "K"),
        ],
        keywords=["stefan-boltzmann law", "heat radiation", "thermodynamics", "heat transfer", "emissivity"],
        solve={
            "Q": lambda v: v["epsilon"] * v["sigma"] * v["A"] * v["T"] ** 4,
            "epsilon": lambda v: v["Q"] / (v["sigma"] * v["A"] * v["T"] ** 4),
            "sigma": lambda v: v["Q"] / (v["epsilon"] * v["A"] * v["T"] ** 4),
            "A": lambda v: v["Q"] / (v["epsilon"] * v["sigma"] * v["T"] ** 4),
            "T": _stefan_boltzmann_T,
        },
    )
)

THERMODYNAMICS_FORMULAS.append(
    Formula(
        id="thermal-efficiency-heat-engine",
        name="Thermal Efficiency (Heat Engine)",
        category="Engineering",
        subcategory="Thermodynamics",
        equation="η = W / Q_h",
        description="Calculates the actual thermal efficiency of a heat engine as net work output over heat input.",
        variables=[
            Variable("eta", "Thermal efficiency", "dimensionless"),
            Variable("W", "Net work output", "J"),
            Variable("Qh", "Heat input", "J"),
        ],
        keywords=["thermal efficiency", "heat engine", "thermodynamics", "work output"],
        solve={
            "eta": lambda v: v["W"] / v["Qh"],
            "W": lambda v: v["eta"] * v["Qh"],
            "Qh": lambda v: v["W"] / v["eta"],
        },
    )
)

THERMODYNAMICS_FORMULAS.append(
    Formula(
        id="specific-heat-capacity",
        name="Specific Heat Capacity",
        category="Engineering",
        subcategory="Thermodynamics",
        equation="Q = mcΔT",
        description="Calculates the heat energy required to change the temperature of a mass of material.",
        variables=[
            Variable("Q", "Heat energy", "J"),
            Variable("m", "Mass", "kg"),
            Variable("c", "Specific heat capacity", "J/(kg·K)"),
            Variable("deltaT", "Temperature change", "K"),
        ],
        keywords=["specific heat", "heat capacity", "thermodynamics", "heat energy", "temperature change"],
        solve={
            "Q": lambda v: v["m"] * v["c"] * v["deltaT"],
            "m": lambda v: v["Q"] / (v["c"] * v["deltaT"]),
            "c": lambda v: v["Q"] / (v["m"] * v["deltaT"]),
            "deltaT": lambda v: v["Q"] / (v["m"] * v["c"]),
        },
    )
)
