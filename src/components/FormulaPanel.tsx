import { useEffect, useState } from 'react';
import type { Formula, Variable } from '../types';
import { calculate } from '../api/calculate';
import { useDebouncedValue } from '../hooks/useDebouncedValue';
import { formatResult } from '../utils/format';

function VariableLabel({ variable }: { variable: Variable }) {
  return (
    <span className="formula-field-label">
      <span className="mono">{variable.symbol}</span> — {variable.name}
      {variable.unit !== 'dimensionless' && variable.unit !== '' && (
        <span className="formula-field-unit"> ({variable.unit})</span>
      )}
    </span>
  );
}

type Outcome =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'ok'; value: number }
  | { status: 'error'; message: string };

export function FormulaPanel({ formula }: { formula: Formula }) {
  const solveTargets = formula.solveTargets;
  const [target, setTarget] = useState(solveTargets[0]);
  const [values, setValues] = useState<Record<string, string>>({});
  const [outcome, setOutcome] = useState<Outcome>({ status: 'idle' });
  const debouncedValues = useDebouncedValue(values, 150);

  // Stays quiet (idle) until every other field has a value, same as before —
  // only now the actual computation is a call to the Python backend.
  useEffect(() => {
    if (!target) {
      setOutcome({ status: 'idle' });
      return;
    }
    const required = formula.variables.filter((v) => v.symbol !== target).map((v) => v.symbol);
    const raw = required.map((symbol) => (debouncedValues[symbol] ?? '').trim());
    if (raw.some((r) => r === '')) {
      setOutcome({ status: 'idle' });
      return;
    }
    const numeric = raw.map(Number);
    // Number.isFinite (not isNaN) — an input like "1e400" parses to
    // Infinity, which JSON can't represent and would otherwise sail past
    // this check straight into a confusing 422 from the backend.
    const badIndex = numeric.findIndex((n) => !Number.isFinite(n));
    if (badIndex !== -1) {
      setOutcome({ status: 'error', message: `"${raw[badIndex]}" isn't a valid number for ${required[badIndex]}.` });
      return;
    }

    const payload = Object.fromEntries(required.map((symbol, i) => [symbol, numeric[i]]));
    let cancelled = false;
    setOutcome({ status: 'loading' });
    calculate(formula.id, target, payload)
      .then((value) => {
        if (!cancelled) setOutcome({ status: 'ok', value });
      })
      .catch((err: unknown) => {
        if (!cancelled) setOutcome({ status: 'error', message: err instanceof Error ? err.message : 'Calculation failed.' });
      });
    return () => {
      cancelled = true;
    };
  }, [formula, target, debouncedValues]);

  function setValue(symbol: string, raw: string) {
    setValues((prev) => ({ ...prev, [symbol]: raw }));
  }

  return (
    <div className="card formula-panel">
      <div className="formula-panel-head">
        <span className="tag">
          {formula.category} · {formula.subcategory}
        </span>
        <h3>{formula.name}</h3>
        <p className="formula-equation mono">{formula.equation}</p>
        <p>{formula.description}</p>
      </div>

      {solveTargets.length > 1 && (
        <div className="solve-target-row">
          <span className="solve-target-label">Solve for:</span>
          {solveTargets.map((symbol) => (
            <button
              key={symbol}
              type="button"
              className={`solve-target-btn mono${symbol === target ? ' active' : ''}`}
              onClick={() => setTarget(symbol)}
            >
              {symbol}
            </button>
          ))}
        </div>
      )}

      {solveTargets.length === 0 ? (
        <div className="formula-fields">
          {formula.variables.map((variable) => (
            <div key={variable.symbol} className="formula-field">
              <VariableLabel variable={variable} />
            </div>
          ))}
          <p className="library-hint">This formula is reference-only — it doesn't reduce to a single practical solve direction.</p>
        </div>
      ) : (
        <div className="formula-fields">
          {formula.variables.map((variable) => {
            const isTarget = variable.symbol === target;
            return (
              <label key={variable.symbol} className="formula-field">
                <VariableLabel variable={variable} />
                {isTarget ? (
                  <output className="formula-output mono">
                    {outcome.status === 'ok' ? formatResult(outcome.value) : outcome.status === 'loading' ? '…' : '—'}
                  </output>
                ) : (
                  <input
                    type="number"
                    inputMode="decimal"
                    className="formula-input"
                    value={values[variable.symbol] ?? ''}
                    onChange={(e) => setValue(variable.symbol, e.target.value)}
                    placeholder="0"
                  />
                )}
              </label>
            );
          })}
        </div>
      )}

      {outcome.status === 'error' && <p className="error-text">{outcome.message}</p>}
    </div>
  );
}
