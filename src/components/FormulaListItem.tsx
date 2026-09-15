import type { Formula } from '../types';

export function FormulaListItem({
  formula,
  selected,
  onSelect,
}: {
  formula: Formula;
  selected: boolean;
  onSelect: () => void;
}) {
  return (
    <button type="button" className={`formula-list-item${selected ? ' selected' : ''}`} onClick={onSelect}>
      <span className="formula-list-item-main">
        <span className="formula-list-item-name">{formula.name}</span>
        <span className="formula-list-item-equation mono">{formula.equation}</span>
      </span>
      <span className="tag">{formula.subcategory}</span>
    </button>
  );
}
