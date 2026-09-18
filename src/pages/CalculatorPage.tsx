import { useEffect, useState } from 'react';
import { BasicCalculator } from '../components/BasicCalculator';
import { FormulaListItem } from '../components/FormulaListItem';
import { FormulaPanel } from '../components/FormulaPanel';
import { searchFormulas } from '../api/formulas';
import { useDebouncedValue } from '../hooks/useDebouncedValue';
import type { Formula } from '../types';

export function CalculatorPage() {
  const [query, setQuery] = useState('');
  const [selected, setSelected] = useState<Formula | null>(null);
  const [results, setResults] = useState<Formula[]>([]);
  const [error, setError] = useState<string | null>(null);

  const debouncedQuery = useDebouncedValue(query, 150);

  useEffect(() => {
    if (!debouncedQuery.trim()) {
      setResults([]);
      setError(null);
      return;
    }
    let cancelled = false;
    searchFormulas(debouncedQuery)
      .then((found) => {
        if (!cancelled) {
          setResults(found.slice(0, 12));
          setError(null);
        }
      })
      .catch((err: unknown) => {
        if (!cancelled) setError(err instanceof Error ? err.message : 'Search failed.');
      });
    return () => {
      cancelled = true;
    };
  }, [debouncedQuery]);

  return (
    <div className="calculator-page">
      <section className="calculator-section">
        <h2>Basic Calculator</h2>
        <BasicCalculator />
      </section>

      <section className="calculator-section">
        <h2>Engineering Formula Search</h2>
        <input
          type="text"
          className="search-input"
          placeholder="Search formulas — try “velocity”, “Ohm's law”, or “F=ma”"
          value={query}
          onChange={(e) => {
            setQuery(e.target.value);
            setSelected(null);
          }}
        />

        {query.trim() && (
          <div className="search-results">
            {error ? (
              <p className="error-text">{error}</p>
            ) : results.length === 0 ? (
              <p className="search-empty">No formulas match "{query}".</p>
            ) : (
              results.map((formula) => (
                <FormulaListItem
                  key={formula.id}
                  formula={formula}
                  selected={selected?.id === formula.id}
                  onSelect={() => setSelected(formula)}
                />
              ))
            )}
          </div>
        )}

        {selected && <FormulaPanel key={selected.id} formula={selected} />}
      </section>
    </div>
  );
}
