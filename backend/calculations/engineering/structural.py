"""Structural engineering formulas: beam deflection, bending stress, buckling, pressure vessels."""

import math

from ...models.formula import Formula, Variable

STRUCTURAL_FORMULAS: list[Formula] = []


def _beam_deflection_L(v: dict[str, float]) -> float:
    val = (384 * v["E"] * v["I"] * v["deltaMax"]) / (5 * v["w"])
    if val < 0:
        raise ValueError("Beam length cannot be computed from a negative value under the fourth root.")
    return val**0.25


STRUCTURAL_FORMULAS.append(
    Formula(
        id="simply-supported-beam-deflection",
        name="Simply Supported Beam Deflection (Uniform Load)",
        category="Engineering",
        subcategory="Structural Engineering",
        equation="δ_max = 5wL⁴ / (384EI)",
        description="Calculates the maximum deflection of a simply supported beam under a uniformly distributed load.",
        variables=[
            Variable("deltaMax", "Maximum deflection", "m"),
            Variable("w", "Load per unit length", "N/m"),
            Variable("L", "Beam length", "m"),
            Variable("E", "Young's modulus", "Pa"),
            Variable("I", "Second moment of area", "m⁴"),
        ],
        keywords=["beam deflection", "bending", "simply supported beam", "structural engineering", "uniform load"],
        solve={
            "deltaMax": lambda v: (5 * v["w"] * v["L"] ** 4) / (384 * v["E"] * v["I"]),
            "w": lambda v: (384 * v["E"] * v["I"] * v["deltaMax"]) / (5 * v["L"] ** 4),
            "E": lambda v: (5 * v["w"] * v["L"] ** 4) / (384 * v["I"] * v["deltaMax"]),
            "I": lambda v: (5 * v["w"] * v["L"] ** 4) / (384 * v["E"] * v["deltaMax"]),
            "L": _beam_deflection_L,
        },
    )
)


def _cantilever_beam_deflection_L(v: dict[str, float]) -> float:
    val = (3 * v["E"] * v["I"] * v["delta"]) / v["P"]
    if val < 0:
        raise ValueError("Beam length cannot be computed from a negative value under the cube root.")
    return math.cbrt(val)


STRUCTURAL_FORMULAS.append(
    Formula(
        id="cantilever-beam-deflection",
        name="Cantilever Beam Deflection (End Load)",
        category="Engineering",
        subcategory="Structural Engineering",
        equation="δ = PL³ / (3EI)",
        description="Calculates the deflection at the free end of a cantilever beam under a point load at that end.",
        variables=[
            Variable("delta", "Deflection", "m"),
            Variable("P", "Point load at free end", "N"),
            Variable("L", "Beam length", "m"),
            Variable("E", "Young's modulus", "Pa"),
            Variable("I", "Second moment of area", "m⁴"),
        ],
        keywords=["cantilever beam", "beam deflection", "bending", "structural engineering", "end load"],
        solve={
            "delta": lambda v: (v["P"] * v["L"] ** 3) / (3 * v["E"] * v["I"]),
            "P": lambda v: (3 * v["E"] * v["I"] * v["delta"]) / v["L"] ** 3,
            "E": lambda v: (v["P"] * v["L"] ** 3) / (3 * v["I"] * v["delta"]),
            "I": lambda v: (v["P"] * v["L"] ** 3) / (3 * v["E"] * v["delta"]),
            "L": _cantilever_beam_deflection_L,
        },
    )
)

STRUCTURAL_FORMULAS.append(
    Formula(
        id="bending-stress",
        name="Bending Stress",
        category="Engineering",
        subcategory="Structural Engineering",
        equation="σ = My / I",
        description="Calculates the bending (flexural) stress at a distance from the neutral axis of a beam under a bending moment.",
        variables=[
            Variable("sigma", "Bending stress", "Pa"),
            Variable("M", "Bending moment", "N·m"),
            Variable("y", "Distance from neutral axis", "m"),
            Variable("I", "Second moment of area", "m⁴"),
        ],
        keywords=["bending stress", "flexural stress", "beam", "structural engineering", "neutral axis"],
        solve={
            "sigma": lambda v: (v["M"] * v["y"]) / v["I"],
            "M": lambda v: (v["sigma"] * v["I"]) / v["y"],
            "y": lambda v: (v["sigma"] * v["I"]) / v["M"],
            "I": lambda v: (v["M"] * v["y"]) / v["sigma"],
        },
    )
)


def _euler_buckling_L(v: dict[str, float]) -> float:
    val = (math.pi**2 * v["E"] * v["I"]) / v["Pcr"]
    if val < 0:
        raise ValueError("Cannot take the square root of a negative value for these inputs.")
    return math.sqrt(val) / v["K"]


def _euler_buckling_K(v: dict[str, float]) -> float:
    val = (math.pi**2 * v["E"] * v["I"]) / v["Pcr"]
    if val < 0:
        raise ValueError("Cannot take the square root of a negative value for these inputs.")
    return math.sqrt(val) / v["L"]


STRUCTURAL_FORMULAS.append(
    Formula(
        id="euler-buckling-load",
        name="Euler Buckling Load",
        category="Engineering",
        subcategory="Structural Engineering",
        equation="P_cr = π²EI / (KL)²",
        description="Calculates the critical axial load at which a slender column buckles.",
        variables=[
            Variable("Pcr", "Critical buckling load", "N"),
            Variable("E", "Young's modulus", "Pa"),
            Variable("I", "Second moment of area", "m⁴"),
            Variable("K", "Column effective length factor", "dimensionless"),
            Variable("L", "Column length", "m"),
        ],
        keywords=["euler buckling", "column buckling", "critical load", "structural engineering", "columns"],
        solve={
            "Pcr": lambda v: (math.pi**2 * v["E"] * v["I"]) / (v["K"] * v["L"]) ** 2,
            "E": lambda v: (v["Pcr"] * (v["K"] * v["L"]) ** 2) / (math.pi**2 * v["I"]),
            "I": lambda v: (v["Pcr"] * (v["K"] * v["L"]) ** 2) / (math.pi**2 * v["E"]),
            "L": _euler_buckling_L,
            "K": _euler_buckling_K,
        },
    )
)

STRUCTURAL_FORMULAS.append(
    Formula(
        id="rectangular-moment-of-inertia",
        name="Second Moment of Area (Rectangular Section)",
        category="Engineering",
        subcategory="Structural Engineering",
        equation="I = bh³ / 12",
        description="Calculates the second moment of area of a rectangular cross-section about its centroidal axis.",
        variables=[
            Variable("I", "Second moment of area", "m⁴"),
            Variable("b", "Width", "m"),
            Variable("h", "Height (bending direction)", "m"),
        ],
        keywords=["second moment of area", "moment of inertia", "rectangular section", "structural engineering", "section properties"],
        solve={
            "I": lambda v: (v["b"] * v["h"] ** 3) / 12,
            "b": lambda v: (12 * v["I"]) / v["h"] ** 3,
            "h": lambda v: math.cbrt((12 * v["I"]) / v["b"]),
        },
    )
)

STRUCTURAL_FORMULAS.append(
    Formula(
        id="factor-of-safety",
        name="Factor of Safety",
        category="Engineering",
        subcategory="Structural Engineering",
        equation="FS = σ_ultimate / σ_allowable",
        description="Calculates the factor of safety as the ratio of a material's ultimate stress to the allowable (working) stress.",
        variables=[
            Variable("FS", "Factor of safety", "dimensionless"),
            Variable("sigmaUlt", "Ultimate stress", "Pa"),
            Variable("sigmaAllow", "Allowable stress", "Pa"),
        ],
        keywords=["factor of safety", "safety factor", "ultimate stress", "allowable stress", "structural engineering"],
        solve={
            "FS": lambda v: v["sigmaUlt"] / v["sigmaAllow"],
            "sigmaUlt": lambda v: v["FS"] * v["sigmaAllow"],
            "sigmaAllow": lambda v: v["sigmaUlt"] / v["FS"],
        },
    )
)

STRUCTURAL_FORMULAS.append(
    Formula(
        id="thin-wall-pressure-vessel-hoop-stress",
        name="Thin-Wall Pressure Vessel Hoop Stress",
        category="Engineering",
        subcategory="Structural Engineering",
        equation="σ_hoop = pr / t",
        description="Calculates the circumferential (hoop) stress in a thin-walled cylindrical pressure vessel.",
        variables=[
            Variable("sigmaHoop", "Hoop stress", "Pa"),
            Variable("p", "Internal pressure", "Pa"),
            Variable("r", "Inner radius", "m"),
            Variable("t", "Wall thickness", "m"),
        ],
        keywords=["hoop stress", "pressure vessel", "thin wall", "structural engineering", "circumferential stress"],
        solve={
            "sigmaHoop": lambda v: (v["p"] * v["r"]) / v["t"],
            "p": lambda v: (v["sigmaHoop"] * v["t"]) / v["r"],
            "r": lambda v: (v["sigmaHoop"] * v["t"]) / v["p"],
            "t": lambda v: (v["p"] * v["r"]) / v["sigmaHoop"],
        },
    )
)

STRUCTURAL_FORMULAS.append(
    Formula(
        id="thin-wall-pressure-vessel-longitudinal-stress",
        name="Thin-Wall Pressure Vessel Longitudinal Stress",
        category="Engineering",
        subcategory="Structural Engineering",
        equation="σ_long = pr / (2t)",
        description="Calculates the longitudinal (axial) stress in a thin-walled cylindrical pressure vessel.",
        variables=[
            Variable("sigmaLong", "Longitudinal stress", "Pa"),
            Variable("p", "Internal pressure", "Pa"),
            Variable("r", "Inner radius", "m"),
            Variable("t", "Wall thickness", "m"),
        ],
        keywords=["longitudinal stress", "pressure vessel", "thin wall", "structural engineering", "axial stress"],
        solve={
            "sigmaLong": lambda v: (v["p"] * v["r"]) / (2 * v["t"]),
            "p": lambda v: (2 * v["sigmaLong"] * v["t"]) / v["r"],
            "r": lambda v: (2 * v["sigmaLong"] * v["t"]) / v["p"],
            "t": lambda v: (v["p"] * v["r"]) / (2 * v["sigmaLong"]),
        },
    )
)

STRUCTURAL_FORMULAS.append(
    Formula(
        id="average-shear-stress",
        name="Average (Direct) Shear Stress",
        category="Engineering",
        subcategory="Structural Engineering",
        equation="τ = V / A",
        description="Calculates the average shear stress on a cross-section from the applied shear force and its area.",
        variables=[
            Variable("tau", "Average shear stress", "Pa"),
            Variable("V", "Shear force", "N"),
            Variable("A", "Cross-sectional area", "m²"),
        ],
        keywords=["shear stress", "direct shear", "structural engineering", "shear force"],
        solve={
            "tau": lambda v: v["V"] / v["A"],
            "V": lambda v: v["tau"] * v["A"],
            "A": lambda v: v["V"] / v["tau"],
        },
    )
)
