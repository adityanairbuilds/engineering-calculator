import type { Formula } from '../../types';

import { algebraFormulas } from './math/algebra';
import { geometryFormulas } from './math/geometry';
import { trigonometryFormulas } from './math/trigonometry';
import { precalculusFormulas } from './math/precalculus';
import { calculusFormulas } from './math/calculus';
import { statisticsFormulas } from './math/statistics';

import { dynamicsFormulas } from './physics/dynamics';
import { circuitsFormulas } from './physics/circuits';
import { kinematicsFormulas } from './physics/kinematics';
import { workEnergyFormulas } from './physics/workEnergy';
import { momentumFormulas } from './physics/momentum';
import { circularMotionFormulas } from './physics/circularMotion';
import { gravitationFormulas } from './physics/gravitation';
import { wavesFormulas } from './physics/waves';
import { fluidsFormulas } from './physics/fluids';
import { thermodynamicsFormulas as physicsThermodynamicsFormulas } from './physics/thermodynamics';
import { electricityFormulas } from './physics/electricity';
import { magnetismFormulas } from './physics/magnetism';

import { mechanicsFormulas } from './engineering/mechanics';
import { staticsFormulas } from './engineering/statics';
import { materialsFormulas } from './engineering/materials';
import { structuralFormulas } from './engineering/structural';
import { electricalFormulas } from './engineering/electrical';
import { mechanicalFormulas } from './engineering/mechanical';
import { fluidMechanicsFormulas } from './engineering/fluidMechanics';
import { thermodynamicsFormulas as engineeringThermodynamicsFormulas } from './engineering/thermodynamics';
import { aerospaceFormulas } from './engineering/aerospace';

export const allFormulas: Formula[] = [
  ...algebraFormulas,
  ...geometryFormulas,
  ...trigonometryFormulas,
  ...precalculusFormulas,
  ...calculusFormulas,
  ...statisticsFormulas,

  ...dynamicsFormulas,
  ...circuitsFormulas,
  ...kinematicsFormulas,
  ...workEnergyFormulas,
  ...momentumFormulas,
  ...circularMotionFormulas,
  ...gravitationFormulas,
  ...wavesFormulas,
  ...fluidsFormulas,
  ...physicsThermodynamicsFormulas,
  ...electricityFormulas,
  ...magnetismFormulas,

  ...mechanicsFormulas,
  ...staticsFormulas,
  ...materialsFormulas,
  ...structuralFormulas,
  ...electricalFormulas,
  ...mechanicalFormulas,
  ...fluidMechanicsFormulas,
  ...engineeringThermodynamicsFormulas,
  ...aerospaceFormulas,
];

export interface CategoryTree {
  name: string;
  subcategories: string[];
}

function buildCategoryTree(formulas: Formula[]): CategoryTree[] {
  const map = new Map<string, Set<string>>();
  for (const formula of formulas) {
    if (!map.has(formula.category)) map.set(formula.category, new Set());
    map.get(formula.category)!.add(formula.subcategory);
  }
  return Array.from(map.entries()).map(([name, subcategories]) => ({
    name,
    subcategories: Array.from(subcategories).sort(),
  }));
}

/** The formula list is static, so the tree is built once at module load. */
export const categoryTree: CategoryTree[] = buildCategoryTree(allFormulas);
