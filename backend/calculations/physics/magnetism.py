"""Magnetism formulas: magnetic force, field, flux, induction, inductance."""

import math

from ...models.formula import Formula, Variable

MAGNETISM_FORMULAS: list[Formula] = []


def _magnetic_force_charge_theta(v: dict[str, float]) -> float:
    ratio = v["F"] / (v["q"] * v["v"] * v["B"])
    if ratio < -1 or ratio > 1:
        raise ValueError("F/(qvB) must be between -1 and 1.")
    return math.asin(ratio) * (180 / math.pi)


MAGNETISM_FORMULAS.append(
    Formula(
        id="magnetic-force-charge",
        name="Magnetic Force on a Moving Charge",
        category="Physics",
        subcategory="Magnetism",
        equation="F = qvB sin(θ)",
        description="Calculates the force on a charged particle moving through a magnetic field.",
        variables=[
            Variable("F", "Magnetic force", "N"),
            Variable("q", "Charge", "C"),
            Variable("v", "Velocity", "m/s"),
            Variable("B", "Magnetic field strength", "T"),
            Variable("theta", "Angle between velocity and field", "°"),
        ],
        keywords=["magnetic force", "lorentz force", "charge", "velocity", "magnetic field"],
        solve={
            "F": lambda v: v["q"] * v["v"] * v["B"] * math.sin((v["theta"] * math.pi) / 180),
            "q": lambda v: v["F"] / (v["v"] * v["B"] * math.sin((v["theta"] * math.pi) / 180)),
            "v": lambda v: v["F"] / (v["q"] * v["B"] * math.sin((v["theta"] * math.pi) / 180)),
            "B": lambda v: v["F"] / (v["q"] * v["v"] * math.sin((v["theta"] * math.pi) / 180)),
            "theta": _magnetic_force_charge_theta,
        },
    )
)


def _magnetic_force_current_theta(v: dict[str, float]) -> float:
    ratio = v["F"] / (v["I"] * v["L"] * v["B"])
    if ratio < -1 or ratio > 1:
        raise ValueError("F/(ILB) must be between -1 and 1.")
    return math.asin(ratio) * (180 / math.pi)


MAGNETISM_FORMULAS.append(
    Formula(
        id="magnetic-force-current",
        name="Magnetic Force on a Current-Carrying Wire",
        category="Physics",
        subcategory="Magnetism",
        equation="F = ILB sin(θ)",
        description="Calculates the force on a current-carrying conductor placed in a magnetic field.",
        variables=[
            Variable("F", "Magnetic force", "N"),
            Variable("I", "Current", "A"),
            Variable("L", "Length of conductor", "m"),
            Variable("B", "Magnetic field strength", "T"),
            Variable("theta", "Angle between conductor and field", "°"),
        ],
        keywords=["magnetic force", "current-carrying wire", "conductor", "magnetic field"],
        solve={
            "F": lambda v: v["I"] * v["L"] * v["B"] * math.sin((v["theta"] * math.pi) / 180),
            "I": lambda v: v["F"] / (v["L"] * v["B"] * math.sin((v["theta"] * math.pi) / 180)),
            "L": lambda v: v["F"] / (v["I"] * v["B"] * math.sin((v["theta"] * math.pi) / 180)),
            "B": lambda v: v["F"] / (v["I"] * v["L"] * math.sin((v["theta"] * math.pi) / 180)),
            "theta": _magnetic_force_current_theta,
        },
    )
)

MAGNETISM_FORMULAS.append(
    Formula(
        id="magnetic-field-wire",
        name="Magnetic Field Around a Straight Wire",
        category="Physics",
        subcategory="Magnetism",
        equation="B = μ₀I / (2πr)",
        description="Calculates the magnetic field strength at a distance from a long straight current-carrying wire.",
        variables=[
            Variable("B", "Magnetic field", "T"),
            Variable("mu0", "Permeability of free space (≈4π×10⁻⁷)", "T·m/A"),
            Variable("I", "Current", "A"),
            Variable("r", "Distance from wire", "m"),
        ],
        keywords=["magnetic field", "wire", "current", "permeability", "ampere"],
        solve={
            "B": lambda v: (v["mu0"] * v["I"]) / (2 * math.pi * v["r"]),
            "mu0": lambda v: (v["B"] * 2 * math.pi * v["r"]) / v["I"],
            "I": lambda v: (v["B"] * 2 * math.pi * v["r"]) / v["mu0"],
            "r": lambda v: (v["mu0"] * v["I"]) / (2 * math.pi * v["B"]),
        },
    )
)


def _magnetic_flux_theta(v: dict[str, float]) -> float:
    ratio = v["Phi"] / (v["B"] * v["A"])
    if ratio < -1 or ratio > 1:
        raise ValueError("Φ/(BA) must be between -1 and 1.")
    return math.acos(ratio) * (180 / math.pi)


MAGNETISM_FORMULAS.append(
    Formula(
        id="magnetic-flux",
        name="Magnetic Flux",
        category="Physics",
        subcategory="Magnetism",
        equation="Φ = BA cos(θ)",
        description="Calculates the magnetic flux through a flat surface in a uniform magnetic field.",
        variables=[
            Variable("Phi", "Magnetic flux", "Wb"),
            Variable("B", "Magnetic field strength", "T"),
            Variable("A", "Surface area", "m²"),
            Variable("theta", "Angle between field and surface normal", "°"),
        ],
        keywords=["magnetic flux", "weber", "magnetic field", "induction"],
        solve={
            "Phi": lambda v: v["B"] * v["A"] * math.cos((v["theta"] * math.pi) / 180),
            "B": lambda v: v["Phi"] / (v["A"] * math.cos((v["theta"] * math.pi) / 180)),
            "A": lambda v: v["Phi"] / (v["B"] * math.cos((v["theta"] * math.pi) / 180)),
            "theta": _magnetic_flux_theta,
        },
    )
)

MAGNETISM_FORMULAS.append(
    Formula(
        id="electromagnetic-induction",
        name="Faraday's Law of Induction",
        category="Physics",
        subcategory="Magnetism",
        equation="ε = N(ΔΦ / Δt)",
        description="Calculates the magnitude of the EMF induced in a coil by a changing magnetic flux (the direction, given by the minus sign, follows from Lenz's law).",
        variables=[
            Variable("emf", "Induced EMF", "V"),
            Variable("N", "Number of coil turns", "dimensionless"),
            Variable("dPhi", "Change in magnetic flux", "Wb"),
            Variable("dt", "Time interval", "s"),
        ],
        keywords=["faraday", "faraday's law", "electromagnetic induction", "emf", "flux", "lenz"],
        solve={
            "emf": lambda v: (v["N"] * v["dPhi"]) / v["dt"],
            "N": lambda v: (v["emf"] * v["dt"]) / v["dPhi"],
            "dPhi": lambda v: (v["emf"] * v["dt"]) / v["N"],
            "dt": lambda v: (v["N"] * v["dPhi"]) / v["emf"],
        },
    )
)

MAGNETISM_FORMULAS.append(
    Formula(
        id="inductance",
        name="Inductance",
        category="Physics",
        subcategory="Magnetism",
        equation="L = NΦ / I",
        description="Calculates the self-inductance of a coil from its flux linkage and current.",
        variables=[
            Variable("L", "Inductance", "H"),
            Variable("N", "Number of coil turns", "dimensionless"),
            Variable("Phi", "Magnetic flux", "Wb"),
            Variable("I", "Current", "A"),
        ],
        keywords=["inductance", "inductor", "magnetic flux", "coil", "henry"],
        solve={
            "L": lambda v: (v["N"] * v["Phi"]) / v["I"],
            "N": lambda v: (v["L"] * v["I"]) / v["Phi"],
            "Phi": lambda v: (v["L"] * v["I"]) / v["N"],
            "I": lambda v: (v["N"] * v["Phi"]) / v["L"],
        },
    )
)

MAGNETISM_FORMULAS.append(
    Formula(
        id="force-between-wires",
        name="Force Between Two Parallel Wires",
        category="Physics",
        subcategory="Magnetism",
        equation="F = μ₀I₁I₂L / (2πd)",
        description="Calculates the magnetic force between two long parallel current-carrying wires.",
        variables=[
            Variable("F", "Force", "N"),
            Variable("mu0", "Permeability of free space (≈4π×10⁻⁷)", "T·m/A"),
            Variable("I1", "Current in wire 1", "A"),
            Variable("I2", "Current in wire 2", "A"),
            Variable("L", "Length of wires", "m"),
            Variable("d", "Distance between wires", "m"),
        ],
        keywords=["force between wires", "parallel wires", "magnetic force", "ampere", "current"],
        solve={
            "F": lambda v: (v["mu0"] * v["I1"] * v["I2"] * v["L"]) / (2 * math.pi * v["d"]),
            "mu0": lambda v: (v["F"] * 2 * math.pi * v["d"]) / (v["I1"] * v["I2"] * v["L"]),
            "I1": lambda v: (v["F"] * 2 * math.pi * v["d"]) / (v["mu0"] * v["I2"] * v["L"]),
            "I2": lambda v: (v["F"] * 2 * math.pi * v["d"]) / (v["mu0"] * v["I1"] * v["L"]),
            "L": lambda v: (v["F"] * 2 * math.pi * v["d"]) / (v["mu0"] * v["I1"] * v["I2"]),
            "d": lambda v: (v["mu0"] * v["I1"] * v["I2"] * v["L"]) / (2 * math.pi * v["F"]),
        },
    )
)

MAGNETISM_FORMULAS.append(
    Formula(
        id="solenoid-field",
        name="Magnetic Field Inside a Solenoid",
        category="Physics",
        subcategory="Magnetism",
        equation="B = μ₀nI",
        description="Calculates the magnetic field strength inside a long, tightly-wound solenoid.",
        variables=[
            Variable("B", "Magnetic field", "T"),
            Variable("mu0", "Permeability of free space (≈4π×10⁻⁷)", "T·m/A"),
            Variable("n", "Turns per unit length", "1/m"),
            Variable("I", "Current", "A"),
        ],
        keywords=["solenoid", "magnetic field", "coil", "turns per length"],
        solve={
            "B": lambda v: v["mu0"] * v["n"] * v["I"],
            "mu0": lambda v: v["B"] / (v["n"] * v["I"]),
            "n": lambda v: v["B"] / (v["mu0"] * v["I"]),
            "I": lambda v: v["B"] / (v["mu0"] * v["n"]),
        },
    )
)
