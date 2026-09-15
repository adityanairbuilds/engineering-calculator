import type { Formula } from '../types';

/** Lowercase, trim, and drop everything but letters/digits/= so "F = m × a" and "f=ma" line up. */
function normalizeEquation(s: string): string {
  return s.toLowerCase().replace(/[^a-z0-9=]/g, '');
}

function normalizeText(s: string): string {
  return s.toLowerCase().trim();
}

function scoreFormula(formula: Formula, query: string, normalizedEquationQuery: string): number {
  const name = normalizeText(formula.name);
  const category = normalizeText(formula.category);
  const subcategory = normalizeText(formula.subcategory);
  let score = 0;

  if (name === query) score += 100;
  else if (name.startsWith(query)) score += 60;
  else if (name.includes(query)) score += 40;

  for (const keyword of formula.keywords) {
    const k = normalizeText(keyword);
    if (k === query) score += 70;
    else if (k.includes(query)) score += 25;
  }

  if (normalizedEquationQuery.length > 1 && normalizeEquation(formula.equation).includes(normalizedEquationQuery)) {
    score += 50;
  }

  if (category.includes(query)) score += 15;
  if (subcategory.includes(query)) score += 15;

  for (const variable of formula.variables) {
    if (normalizeText(variable.name).includes(query)) score += 10;
  }

  // Multi-word queries: also reward matching on individual tokens so
  // "electric resistance" still finds "Ohm's Law" (keyword "resistance").
  const tokens = query.split(/\s+/).filter((t) => t.length > 2);
  if (tokens.length > 1) {
    for (const token of tokens) {
      if (name.includes(token)) score += 5;
      if (formula.keywords.some((k) => normalizeText(k).includes(token))) score += 8;
    }
  }

  return score;
}

export function searchFormulas(formulas: Formula[], rawQuery: string): Formula[] {
  const query = normalizeText(rawQuery);
  if (!query) return [];

  const normalizedEquationQuery = normalizeEquation(rawQuery);

  return formulas
    .map((formula) => ({ formula, score: scoreFormula(formula, query, normalizedEquationQuery) }))
    .filter((r) => r.score > 0)
    .sort((a, b) => b.score - a.score)
    .map((r) => r.formula);
}
