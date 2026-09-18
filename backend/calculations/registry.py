"""Aggregates every domain's formula list into one lookup table — the
Python equivalent of the frontend's old src/data/formulas/index.ts.
"""

from ..models.formula import Formula
from .mathematics.algebra import ALGEBRA_FORMULAS
from .mathematics.geometry import GEOMETRY_FORMULAS
from .mathematics.trigonometry import TRIGONOMETRY_FORMULAS
from .mathematics.precalculus import PRECALCULUS_FORMULAS
from .mathematics.calculus import CALCULUS_FORMULAS
from .mathematics.statistics import STATISTICS_FORMULAS

from .physics.kinematics import KINEMATICS_FORMULAS
from .physics.dynamics import DYNAMICS_FORMULAS
from .physics.work_energy import WORK_ENERGY_FORMULAS
from .physics.momentum import MOMENTUM_FORMULAS
from .physics.circular_motion import CIRCULAR_MOTION_FORMULAS
from .physics.gravitation import GRAVITATION_FORMULAS
from .physics.waves import WAVES_FORMULAS
from .physics.fluids import FLUIDS_FORMULAS
from .physics.thermodynamics import THERMODYNAMICS_FORMULAS as PHYSICS_THERMODYNAMICS_FORMULAS
from .physics.electricity import ELECTRICITY_FORMULAS
from .physics.circuits import CIRCUITS_FORMULAS
from .physics.magnetism import MAGNETISM_FORMULAS

from .engineering.mechanics import MECHANICS_FORMULAS
from .engineering.statics import STATICS_FORMULAS
from .engineering.materials import MATERIALS_FORMULAS
from .engineering.structural import STRUCTURAL_FORMULAS
from .engineering.electrical import ELECTRICAL_FORMULAS
from .engineering.mechanical import MECHANICAL_FORMULAS
from .engineering.fluid_mechanics import FLUID_MECHANICS_FORMULAS
from .engineering.thermodynamics import THERMODYNAMICS_FORMULAS as ENGINEERING_THERMODYNAMICS_FORMULAS
from .engineering.aerospace import AEROSPACE_FORMULAS

ALL_FORMULAS: list[Formula] = [
    *ALGEBRA_FORMULAS,
    *GEOMETRY_FORMULAS,
    *TRIGONOMETRY_FORMULAS,
    *PRECALCULUS_FORMULAS,
    *CALCULUS_FORMULAS,
    *STATISTICS_FORMULAS,
    *KINEMATICS_FORMULAS,
    *DYNAMICS_FORMULAS,
    *WORK_ENERGY_FORMULAS,
    *MOMENTUM_FORMULAS,
    *CIRCULAR_MOTION_FORMULAS,
    *GRAVITATION_FORMULAS,
    *WAVES_FORMULAS,
    *FLUIDS_FORMULAS,
    *PHYSICS_THERMODYNAMICS_FORMULAS,
    *ELECTRICITY_FORMULAS,
    *CIRCUITS_FORMULAS,
    *MAGNETISM_FORMULAS,
    *MECHANICS_FORMULAS,
    *STATICS_FORMULAS,
    *MATERIALS_FORMULAS,
    *STRUCTURAL_FORMULAS,
    *ELECTRICAL_FORMULAS,
    *MECHANICAL_FORMULAS,
    *FLUID_MECHANICS_FORMULAS,
    *ENGINEERING_THERMODYNAMICS_FORMULAS,
    *AEROSPACE_FORMULAS,
]
