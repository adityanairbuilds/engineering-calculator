"""Electricity formulas: Coulomb's law, electric fields, potential, flux, current."""

import math

from ...models.formula import Formula, Variable

ELECTRICITY_FORMULAS: list[Formula] = []


def _coulombs_law_r(v: dict[str, float]) -> float:
    sq = (v["k"] * v["q1"] * v["q2"]) / v["F"]
    if sq < 0:
        raise ValueError("kq₁q₂/F is negative — no real distance.")
    return math.sqrt(sq)


ELECTRICITY_FORMULAS.append(
    Formula(
        id="coulombs-law",
        name="Coulomb's Law",
        category="Physics",
        subcategory="Electricity",
        equation="F = kq₁q₂ / r²",
        description="Calculates the electric force between two point charges.",
        variables=[
            Variable("F", "Electric force", "N"),
            Variable("k", "Coulomb constant (≈8.99×10⁹)", "N·m²/C²"),
            Variable("q1", "Charge 1", "C"),
            Variable("q2", "Charge 2", "C"),
            Variable("r", "Distance between charges", "m"),
        ],
        keywords=["coulomb", "coulomb's law", "electric force", "charge", "electricity"],
        solve={
            "F": lambda v: (v["k"] * v["q1"] * v["q2"]) / v["r"] ** 2,
            "k": lambda v: (v["F"] * v["r"] ** 2) / (v["q1"] * v["q2"]),
            "q1": lambda v: (v["F"] * v["r"] ** 2) / (v["k"] * v["q2"]),
            "q2": lambda v: (v["F"] * v["r"] ** 2) / (v["k"] * v["q1"]),
            "r": _coulombs_law_r,
        },
    )
)

ELECTRICITY_FORMULAS.append(
    Formula(
        id="electric-field",
        name="Electric Field",
        category="Physics",
        subcategory="Electricity",
        equation="E = F / q",
        description="Calculates the electric field from the force it exerts on a test charge.",
        variables=[
            Variable("E", "Electric field", "N/C"),
            Variable("F", "Electric force", "N"),
            Variable("q", "Test charge", "C"),
        ],
        keywords=["electric field", "electricity", "charge", "force"],
        solve={
            "E": lambda v: v["F"] / v["q"],
            "F": lambda v: v["E"] * v["q"],
            "q": lambda v: v["F"] / v["E"],
        },
    )
)

ELECTRICITY_FORMULAS.append(
    Formula(
        id="electric-potential",
        name="Electric Potential",
        category="Physics",
        subcategory="Electricity",
        equation="V = W / q",
        description="Calculates electric potential (voltage) from the work done moving a charge.",
        variables=[
            Variable("V", "Electric potential", "V"),
            Variable("W", "Work done on charge", "J"),
            Variable("q", "Charge", "C"),
        ],
        keywords=["electric potential", "voltage", "electricity", "charge"],
        solve={
            "V": lambda v: v["W"] / v["q"],
            "W": lambda v: v["V"] * v["q"],
            "q": lambda v: v["W"] / v["V"],
        },
    )
)

ELECTRICITY_FORMULAS.append(
    Formula(
        id="electric-potential-energy",
        name="Electric Potential Energy",
        category="Physics",
        subcategory="Electricity",
        equation="U = kq₁q₂ / r",
        description="Calculates the electric potential energy between two point charges.",
        variables=[
            Variable("U", "Potential energy", "J"),
            Variable("k", "Coulomb constant (≈8.99×10⁹)", "N·m²/C²"),
            Variable("q1", "Charge 1", "C"),
            Variable("q2", "Charge 2", "C"),
            Variable("r", "Distance between charges", "m"),
        ],
        keywords=["electric potential energy", "charge", "electricity"],
        solve={
            "U": lambda v: (v["k"] * v["q1"] * v["q2"]) / v["r"],
            "k": lambda v: (v["U"] * v["r"]) / (v["q1"] * v["q2"]),
            "q1": lambda v: (v["U"] * v["r"]) / (v["k"] * v["q2"]),
            "q2": lambda v: (v["U"] * v["r"]) / (v["k"] * v["q1"]),
            "r": lambda v: (v["k"] * v["q1"] * v["q2"]) / v["U"],
        },
    )
)


def _electric_flux_theta(v: dict[str, float]) -> float:
    ratio = v["Phi"] / (v["E"] * v["A"])
    if ratio < -1 or ratio > 1:
        raise ValueError("Φ/(EA) must be between -1 and 1.")
    return math.acos(ratio) * (180 / math.pi)


ELECTRICITY_FORMULAS.append(
    Formula(
        id="electric-flux",
        name="Gauss's Law (Electric Flux)",
        category="Physics",
        subcategory="Electricity",
        equation="Φ = EA cos(θ)",
        description="Calculates the electric flux through a flat surface in a uniform electric field.",
        variables=[
            Variable("Phi", "Electric flux", "N·m²/C"),
            Variable("E", "Electric field", "N/C"),
            Variable("A", "Surface area", "m²"),
            Variable("theta", "Angle between field and surface normal", "°"),
        ],
        keywords=["electric flux", "gauss", "gauss's law", "electric field", "electricity"],
        solve={
            "Phi": lambda v: v["E"] * v["A"] * math.cos((v["theta"] * math.pi) / 180),
            "E": lambda v: v["Phi"] / (v["A"] * math.cos((v["theta"] * math.pi) / 180)),
            "A": lambda v: v["Phi"] / (v["E"] * math.cos((v["theta"] * math.pi) / 180)),
            "theta": _electric_flux_theta,
        },
    )
)

ELECTRICITY_FORMULAS.append(
    Formula(
        id="electric-current",
        name="Electric Current",
        category="Physics",
        subcategory="Electricity",
        equation="I = Q / t",
        description="Calculates the average electric current from the charge that flows past a point over time.",
        variables=[
            Variable("I", "Current", "A"),
            Variable("Q", "Charge", "C"),
            Variable("t", "Time", "s"),
        ],
        keywords=["electric current", "current", "charge", "amperes", "electricity"],
        solve={
            "I": lambda v: v["Q"] / v["t"],
            "Q": lambda v: v["I"] * v["t"],
            "t": lambda v: v["Q"] / v["I"],
        },
    )
)


def _capacitor_energy_v(v: dict[str, float]) -> float:
    sq = (2 * v["U"]) / v["C"]
    if sq < 0:
        raise ValueError("2U/C is negative — no real voltage.")
    return math.sqrt(sq)


ELECTRICITY_FORMULAS.append(
    Formula(
        id="capacitor-energy",
        name="Energy Stored in a Capacitor",
        category="Physics",
        subcategory="Electricity",
        equation="U = ½CV²",
        description="Calculates the electrical energy stored in a charged capacitor.",
        variables=[
            Variable("U", "Stored energy", "J"),
            Variable("C", "Capacitance", "F"),
            Variable("V", "Voltage", "V"),
        ],
        keywords=["capacitor energy", "stored energy", "capacitance", "voltage", "electricity"],
        solve={
            "U": lambda v: 0.5 * v["C"] * v["V"] ** 2,
            "C": lambda v: (2 * v["U"]) / v["V"] ** 2,
            "V": _capacitor_energy_v,
        },
    )
)
