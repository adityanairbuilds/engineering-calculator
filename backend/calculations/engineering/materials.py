"""Materials engineering formulas: density, elastic moduli, thermal strain."""

from ...models.formula import Formula, Variable

MATERIALS_FORMULAS: list[Formula] = []

MATERIALS_FORMULAS.append(
    Formula(
        id="density",
        name="Density",
        category="Engineering",
        subcategory="Materials",
        equation="ρ = m / V",
        description="Calculates density from mass and volume.",
        variables=[
            Variable("rho", "Density", "kg/m³"),
            Variable("m", "Mass", "kg"),
            Variable("V", "Volume", "m³"),
        ],
        keywords=["density", "mass", "volume", "materials", "engineering"],
        solve={
            "rho": lambda v: v["m"] / v["V"],
            "m": lambda v: v["rho"] * v["V"],
            "V": lambda v: v["m"] / v["rho"],
        },
    )
)

MATERIALS_FORMULAS.append(
    Formula(
        id="poisson-ratio",
        name="Poisson's Ratio",
        category="Engineering",
        subcategory="Materials",
        equation="ν = -ε_transverse / ε_longitudinal",
        description="Relates a material's transverse strain to its longitudinal strain under axial load.",
        variables=[
            Variable("nu", "Poisson's ratio", "dimensionless"),
            Variable("epsilonT", "Transverse strain", "dimensionless"),
            Variable("epsilonL", "Longitudinal strain", "dimensionless"),
        ],
        keywords=["poisson's ratio", "transverse strain", "longitudinal strain", "materials", "engineering"],
        solve={
            "nu": lambda v: -v["epsilonT"] / v["epsilonL"],
            "epsilonT": lambda v: -v["nu"] * v["epsilonL"],
            "epsilonL": lambda v: -v["epsilonT"] / v["nu"],
        },
    )
)

MATERIALS_FORMULAS.append(
    Formula(
        id="shear-modulus",
        name="Shear Modulus",
        category="Engineering",
        subcategory="Materials",
        equation="G = τ / γ",
        description="Calculates the shear modulus (modulus of rigidity) from shear stress and shear strain.",
        variables=[
            Variable("G", "Shear modulus", "Pa"),
            Variable("tau", "Shear stress", "Pa"),
            Variable("gamma", "Shear strain", "dimensionless"),
        ],
        keywords=["shear modulus", "modulus of rigidity", "shear stress", "shear strain", "materials"],
        solve={
            "G": lambda v: v["tau"] / v["gamma"],
            "tau": lambda v: v["G"] * v["gamma"],
            "gamma": lambda v: v["tau"] / v["G"],
        },
    )
)

MATERIALS_FORMULAS.append(
    Formula(
        id="bulk-modulus",
        name="Bulk Modulus",
        category="Engineering",
        subcategory="Materials",
        equation="K = -ΔP / (ΔV / V₀)",
        description="Calculates a material's resistance to uniform compression from a pressure change and the resulting volume change.",
        variables=[
            Variable("K", "Bulk modulus", "Pa"),
            Variable("deltaP", "Change in pressure", "Pa"),
            Variable("V0", "Original volume", "m³"),
            Variable("deltaV", "Change in volume", "m³"),
        ],
        keywords=["bulk modulus", "compression", "pressure", "volume", "materials", "engineering"],
        solve={
            "K": lambda v: (-v["deltaP"] * v["V0"]) / v["deltaV"],
            "deltaP": lambda v: (-v["K"] * v["deltaV"]) / v["V0"],
            "V0": lambda v: (-v["K"] * v["deltaV"]) / v["deltaP"],
            "deltaV": lambda v: (-v["deltaP"] * v["V0"]) / v["K"],
        },
    )
)

MATERIALS_FORMULAS.append(
    Formula(
        id="hookes-law",
        name="Hooke's Law",
        category="Engineering",
        subcategory="Materials",
        equation="F = -kx",
        description="Calculates the restoring force in a linear elastic spring proportional to its displacement from equilibrium.",
        variables=[
            Variable("F", "Restoring force", "N"),
            Variable("k", "Spring constant", "N/m"),
            Variable("x", "Displacement from equilibrium", "m"),
        ],
        keywords=["hooke's law", "spring", "spring constant", "force", "displacement", "materials"],
        solve={
            "F": lambda v: -v["k"] * v["x"],
            "k": lambda v: -v["F"] / v["x"],
            "x": lambda v: -v["F"] / v["k"],
        },
    )
)

MATERIALS_FORMULAS.append(
    Formula(
        id="specific-gravity",
        name="Specific Gravity",
        category="Engineering",
        subcategory="Materials",
        equation="SG = ρ / ρ_ref",
        description="Calculates specific gravity as the ratio of a material's density to a reference density (e.g. water at 1000 kg/m³).",
        variables=[
            Variable("SG", "Specific gravity", "dimensionless"),
            Variable("rho", "Material density", "kg/m³"),
            Variable("rhoRef", "Reference density", "kg/m³"),
        ],
        keywords=["specific gravity", "relative density", "density", "materials", "engineering"],
        solve={
            "SG": lambda v: v["rho"] / v["rhoRef"],
            "rho": lambda v: v["SG"] * v["rhoRef"],
            "rhoRef": lambda v: v["rho"] / v["SG"],
        },
    )
)

MATERIALS_FORMULAS.append(
    Formula(
        id="specific-weight",
        name="Specific Weight",
        category="Engineering",
        subcategory="Materials",
        equation="γ = ρg",
        description="Calculates specific weight (weight per unit volume) from density and gravitational acceleration.",
        variables=[
            Variable("gamma", "Specific weight", "N/m³"),
            Variable("rho", "Density", "kg/m³"),
            Variable("g", "Gravitational acceleration", "m/s²"),
        ],
        keywords=["specific weight", "unit weight", "density", "materials", "engineering"],
        solve={
            "gamma": lambda v: v["rho"] * v["g"],
            "rho": lambda v: v["gamma"] / v["g"],
            "g": lambda v: v["gamma"] / v["rho"],
        },
    )
)

MATERIALS_FORMULAS.append(
    Formula(
        id="thermal-strain",
        name="Thermal Strain",
        category="Engineering",
        subcategory="Materials",
        equation="ε = αΔT",
        description="Calculates the strain induced in a material by a temperature change, from its coefficient of thermal expansion.",
        variables=[
            Variable("epsilon", "Thermal strain", "dimensionless"),
            Variable("alpha", "Coefficient of thermal expansion", "1/K"),
            Variable("deltaT", "Temperature change", "K"),
        ],
        keywords=["thermal strain", "thermal expansion", "coefficient of thermal expansion", "materials", "temperature"],
        solve={
            "epsilon": lambda v: v["alpha"] * v["deltaT"],
            "alpha": lambda v: v["epsilon"] / v["deltaT"],
            "deltaT": lambda v: v["epsilon"] / v["alpha"],
        },
    )
)
