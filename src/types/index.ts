export interface Variable {
  symbol: string;
  name: string;
  unit: string;
}

/**
 * A formula as served by the backend. The actual solve logic runs in
 * Python (see backend/calculations/) — `solveTargets` just lists which
 * variable symbols the API can compute POST /api/calculate/{id} for.
 */
export interface Formula {
  id: string;
  name: string;
  category: string;
  subcategory: string;
  equation: string;
  description: string;
  variables: Variable[];
  keywords: string[];
  solveTargets: string[];
}
