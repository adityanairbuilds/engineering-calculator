import type { Formula } from '../types';
import { apiRequest } from './client';

/** The wire shape: identical to `Formula` except the backend spells `solveTargets` `solve_targets`. */
type FormulaDTO = Omit<Formula, 'solveTargets'> & { solve_targets: string[] };

function fromDTO({ solve_targets, ...rest }: FormulaDTO): Formula {
  return { ...rest, solveTargets: solve_targets };
}

interface CategoryFilter {
  category?: string;
  subcategory?: string;
}

function filterParams({ category, subcategory }: CategoryFilter): URLSearchParams {
  const params = new URLSearchParams();
  if (category) params.set('category', category);
  if (subcategory) params.set('subcategory', subcategory);
  return params;
}

export async function fetchFormulas(filter: CategoryFilter = {}): Promise<Formula[]> {
  const params = filterParams(filter);
  const suffix = params.toString() ? `?${params}` : '';
  const dtos = await apiRequest<FormulaDTO[]>(`/api/formulas${suffix}`);
  return dtos.map(fromDTO);
}

export async function fetchFormula(id: string): Promise<Formula> {
  const dto = await apiRequest<FormulaDTO>(`/api/formulas/${encodeURIComponent(id)}`);
  return fromDTO(dto);
}

export async function searchFormulas(query: string, filter: CategoryFilter = {}): Promise<Formula[]> {
  const params = filterParams(filter);
  params.set('q', query);
  const dtos = await apiRequest<FormulaDTO[]>(`/api/search?${params}`);
  return dtos.map(fromDTO);
}
