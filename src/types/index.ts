export interface Variable {
  symbol: string;
  name: string;
  unit: string;
}

/**
 * Maps a variable symbol to a function that computes it from the other
 * variables' numeric values. Only symbols with a practical closed-form
 * solution are included — this is not a symbolic algebra system.
 * Solve functions may throw an Error (with a user-facing message) when
 * the inputs are outside the formula's valid domain.
 */
export type SolveMap = Partial<Record<string, (values: Record<string, number>) => number>>;

export interface Formula {
  id: string;
  name: string;
  category: string;
  subcategory: string;
  equation: string;
  description: string;
  variables: Variable[];
  keywords: string[];
  solve: SolveMap;
}
