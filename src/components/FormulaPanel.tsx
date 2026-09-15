import { useState } from 'react';
import type { Formula, Variable } from '../types';
import { solveFormula } from '../utils/solveFormula';
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

export function FormulaPanel({ formula }: { formula: Formula }) {
  const solveTargets = Object.keys(formula.solve);
  const [target, setTarget] = useState(solveTargets[0]);
  const [values, setValues] = useState<Record<string, string>>({});

  const outcome = target ? solveFormula(formula, target, values) : null;

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
                    {outcome?.status === 'ok' ? formatResult(outcome.value) : '—'}
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

      {outcome?.status === 'error' && <p className="error-text">{outcome.message}</p>}
    </div>
  );
}
