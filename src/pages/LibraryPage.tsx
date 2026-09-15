import { useState } from 'react';
import { FormulaListItem } from '../components/FormulaListItem';
import { FormulaPanel } from '../components/FormulaPanel';
import { allFormulas, categoryTree } from '../data/formulas';
import { searchFormulas } from '../utils/search';
import type { Formula } from '../types';

const ALL = 'All';

export function LibraryPage() {
  const [query, setQuery] = useState('');
  const [category, setCategory] = useState(ALL);
  const [subcategory, setSubcategory] = useState(ALL);
  const [selected, setSelected] = useState<Formula | null>(null);

  const subcategoryOptions =
    category === ALL ? [] : (categoryTree.find((c) => c.name === category)?.subcategories ?? []);

  const searched = query.trim() ? searchFormulas(allFormulas, query) : allFormulas;
  const results = searched.filter(
    (f) => (category === ALL || f.category === category) && (subcategory === ALL || f.subcategory === subcategory),
  );
  // Drop the open panel once its formula falls out of the filtered/searched results,
  // instead of leaving a stale calculator open for a formula the list no longer shows.
  const visibleSelected = selected && results.some((f) => f.id === selected.id) ? selected : null;

  function handleCategoryChange(next: string) {
    setCategory(next);
    setSubcategory(ALL);
  }

  return (
    <div className="library-page">
      <h1>Formula Library</h1>
      <p>Browse every formula, or search and filter to find what you need.</p>

      <div className="library-controls">
        <input
          type="text"
          className="search-input"
          placeholder="Search all formulas..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <div className="library-filters">
          <select value={category} onChange={(e) => handleCategoryChange(e.target.value)}>
            <option value={ALL}>All categories</option>
            {categoryTree.map((c) => (
              <option key={c.name} value={c.name}>
                {c.name}
              </option>
            ))}
          </select>
          <select value={subcategory} onChange={(e) => setSubcategory(e.target.value)} disabled={category === ALL}>
            <option value={ALL}>All subcategories</option>
            {subcategoryOptions.map((s) => (
              <option key={s} value={s}>
                {s}
              </option>
            ))}
          </select>
        </div>
      </div>

      <div className="library-body">
        <div className="library-results">
          <p className="library-count">
            {results.length} formula{results.length === 1 ? '' : 's'}
          </p>
          {results.map((formula) => (
            <FormulaListItem
              key={formula.id}
              formula={formula}
              selected={visibleSelected?.id === formula.id}
              onSelect={() => setSelected(formula)}
            />
          ))}
        </div>
        <div className="library-detail">
          {visibleSelected ? (
            <FormulaPanel key={visibleSelected.id} formula={visibleSelected} />
          ) : (
            <p className="library-hint">Select a formula to open its calculator.</p>
          )}
        </div>
      </div>
    </div>
  );
}
