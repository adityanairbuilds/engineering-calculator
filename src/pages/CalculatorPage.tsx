import { useMemo, useState } from 'react';
import { BasicCalculator } from '../components/BasicCalculator';
import { FormulaListItem } from '../components/FormulaListItem';
import { FormulaPanel } from '../components/FormulaPanel';
import { allFormulas } from '../data/formulas';
import { searchFormulas } from '../utils/search';
import type { Formula } from '../types';

export function CalculatorPage() {
  const [query, setQuery] = useState('');
  const [selected, setSelected] = useState<Formula | null>(null);

  const results = useMemo(() => searchFormulas(allFormulas, query).slice(0, 12), [query]);

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
            {results.length === 0 ? (
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
