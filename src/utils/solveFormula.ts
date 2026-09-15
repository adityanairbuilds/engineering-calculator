import type { Formula } from '../types';

export type SolveOutcome =
  | { status: 'incomplete' }
  | { status: 'error'; message: string }
  | { status: 'ok'; value: number };

/**
 * Computes `target` from the other variables' raw string inputs.
 * Returns 'incomplete' (not an error) until every other field has a value,
 * so the UI can stay quiet while the student is still typing.
 */
export function solveFormula(
  formula: Formula,
  target: string,
  rawValues: Record<string, string>,
): SolveOutcome {
  const solver = formula.solve[target];
  if (!solver) {
    return { status: 'error', message: `This formula can't be solved for ${target} directly.` };
  }

  const numericValues: Record<string, number> = {};

  for (const { symbol } of formula.variables) {
    if (symbol === target) continue;

    const raw = (rawValues[symbol] ?? '').trim();
    if (raw === '') return { status: 'incomplete' };

    const value = Number(raw);
    if (Number.isNaN(value)) {
      return { status: 'error', message: `"${raw}" isn't a valid number for ${symbol}.` };
    }
    numericValues[symbol] = value;
  }

  try {
    const result = solver(numericValues);
    if (!Number.isFinite(result)) {
      return { status: 'error', message: 'Result is undefined — check for division by zero.' };
    }
    return { status: 'ok', value: result };
  } catch (err) {
    const message = err instanceof Error ? err.message : 'Could not compute a result for these inputs.';
    return { status: 'error', message };
  }
}
