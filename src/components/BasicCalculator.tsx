import { useMemo, useState } from 'react';
import { evaluateExpression } from '../utils/evaluateExpression';
import { formatResult } from '../utils/format';

const BUTTON_ROWS = [
  ['(', ')', '√', 'C'],
  ['7', '8', '9', '÷'],
  ['4', '5', '6', '×'],
  ['1', '2', '3', '−'],
  ['0', '.', '%', '+'],
  ['^', '⌫', '=', ''],
];

export function BasicCalculator() {
  const [expr, setExpr] = useState('');
  const [error, setError] = useState<string | null>(null);

  const preview = useMemo(() => {
    if (!expr.trim()) return null;
    try {
      return formatResult(evaluateExpression(expr));
    } catch {
      return null;
    }
  }, [expr]);

  function press(key: string) {
    setError(null);
    // The tokenizer reads '×' and '÷' natively, but the keypad's − (U+2212)
    // has to become the ASCII hyphen-minus it expects.
    setExpr((prev) => prev + (key === '−' ? '-' : key));
  }

  function clear() {
    setExpr('');
    setError(null);
  }

  function backspace() {
    setExpr((prev) => prev.slice(0, -1));
    setError(null);
  }

  function equals() {
    try {
      const result = evaluateExpression(expr);
      setExpr(formatResult(result));
      setError(null);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Invalid expression');
    }
  }

  function handleButton(key: string) {
    if (key === '') return;
    if (key === 'C') return clear();
    if (key === '⌫') return backspace();
    if (key === '=') return equals();
    press(key);
  }

  function handleKeyDown(e: React.KeyboardEvent<HTMLInputElement>) {
    if (e.key === 'Enter') {
      e.preventDefault();
      equals();
    } else if (e.key === 'Escape') {
      clear();
    }
  }

  return (
    <div className="card basic-calculator">
      <input
        className="calculator-display mono"
        value={expr}
        onChange={(e) => {
          setError(null);
          setExpr(e.target.value);
        }}
        onKeyDown={handleKeyDown}
        placeholder="0"
        aria-label="Calculator expression"
      />
      <div className="calculator-preview mono">{error ? '' : (preview ?? ' ')}</div>
      {error && <p className="error-text">{error}</p>}
      <div className="calculator-keypad">
        {BUTTON_ROWS.flat().map((key, i) =>
          key === '' ? (
            <span key={i} />
          ) : (
            <button
              key={i}
              type="button"
              className={`calculator-key mono${key === '=' ? ' equals' : ''}`}
              onClick={() => handleButton(key)}
            >
              {key}
            </button>
          ),
        )}
      </div>
    </div>
  );
}
