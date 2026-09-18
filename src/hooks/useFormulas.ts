import { useEffect, useState } from 'react';
import { fetchFormulas } from '../api/formulas';
import type { Formula } from '../types';

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

export type FormulasState =
  | { status: 'loading' }
  | { status: 'error'; message: string }
  | { status: 'ok'; formulas: Formula[]; categoryTree: CategoryTree[] };

/** Fetches the full formula list once (for Home's subject list and Library's default browse view). */
export function useFormulas(): FormulasState {
  const [state, setState] = useState<FormulasState>({ status: 'loading' });

  useEffect(() => {
    let cancelled = false;
    fetchFormulas()
      .then((formulas) => {
        if (!cancelled) setState({ status: 'ok', formulas, categoryTree: buildCategoryTree(formulas) });
      })
      .catch((err: unknown) => {
        if (!cancelled) setState({ status: 'error', message: err instanceof Error ? err.message : 'Could not load formulas.' });
      });
    return () => {
      cancelled = true;
    };
  }, []);

  return state;
}
