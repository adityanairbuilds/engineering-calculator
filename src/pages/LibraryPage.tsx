import { useEffect, useState } from 'react';
import { FormulaListItem } from '../components/FormulaListItem';
import { FormulaPanel } from '../components/FormulaPanel';
import { searchFormulas } from '../api/formulas';
import { useDebouncedValue } from '../hooks/useDebouncedValue';
import type { CategoryTree } from '../hooks/useFormulas';
import type { Formula } from '../types';

const ALL = 'All';

export function LibraryPage({ formulas, categoryTree }: { formulas: Formula[]; categoryTree: CategoryTree[] }) {
  const [query, setQuery] = useState('');
  const [category, setCategory] = useState(ALL);
  const [subcategory, setSubcategory] = useState(ALL);
  const [selected, setSelected] = useState<Formula | null>(null);

  const debouncedQuery = useDebouncedValue(query, 150);
  // The plain "browse everything" view filters the already-fetched list locally
  // (instant, no network round trip). A real query hits the backend's search
  // endpoint, which owns the actual ranking/matching logic.
  const [searchResults, setSearchResults] = useState<Formula[] | null>(null);
  const [searching, setSearching] = useState(false);

  useEffect(() => {
    if (!debouncedQuery.trim()) {
      setSearchResults(null);
      setSearching(false);
      return;
    }
    let cancelled = false;
    // Clear the previous query's results immediately rather than leaving them
    // on screen under a "Searching…" label while a new (possibly differently
    // filtered) search is in flight.
    setSearchResults(null);
    setSearching(true);
    searchFormulas(debouncedQuery, {
      category: category === ALL ? undefined : category,
      subcategory: subcategory === ALL ? undefined : subcategory,
    })
      .then((results) => {
        if (!cancelled) {
          setSearchResults(results);
          setSearching(false);
        }
      })
      .catch(() => {
        if (!cancelled) {
          setSearchResults([]);
          setSearching(false);
        }
      });
    return () => {
      cancelled = true;
    };
  }, [debouncedQuery, category, subcategory]);

  const subcategoryOptions =
    category === ALL ? [] : (categoryTree.find((c) => c.name === category)?.subcategories ?? []);

  const results = query.trim()
    ? (searchResults ?? [])
    : formulas.filter(
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
            {searching ? 'Searching…' : `${results.length} formula${results.length === 1 ? '' : 's'}`}
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
