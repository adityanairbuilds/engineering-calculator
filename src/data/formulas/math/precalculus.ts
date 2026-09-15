import type { Formula } from '../../../types';

export const precalculusFormulas: Formula[] = [
  {
    id: 'exponential-growth',
    name: 'Exponential Growth/Decay',
    category: 'Mathematics',
    subcategory: 'Precalculus',
    equation: 'A = A₀e^(kt)',
    description: 'Models exponential growth (k > 0) or decay (k < 0) over time.',
    variables: [
      { symbol: 'A', name: 'Final amount', unit: 'dimensionless' },
      { symbol: 'A0', name: 'Initial amount', unit: 'dimensionless' },
      { symbol: 'k', name: 'Growth/decay constant', unit: 'per unit time' },
      { symbol: 't', name: 'Time', unit: 'dimensionless' },
    ],
    keywords: ['exponential growth', 'exponential decay', 'population growth', 'half life'],
    solve: {
      A: (v) => v.A0 * Math.exp(v.k * v.t),
      A0: (v) => v.A / Math.exp(v.k * v.t),
      k: (v) => {
        if (v.A <= 0 || v.A0 <= 0) throw new Error('Amounts must be positive.');
        return Math.log(v.A / v.A0) / v.t;
      },
      t: (v) => {
        if (v.A <= 0 || v.A0 <= 0) throw new Error('Amounts must be positive.');
        return Math.log(v.A / v.A0) / v.k;
      },
    },
  },
  {
    id: 'logarithm',
    name: 'Logarithm (General Base)',
    category: 'Mathematics',
    subcategory: 'Precalculus',
    equation: 'y = log_b(x)  ⇔  b^y = x',
    description: 'Converts between exponential and logarithmic form for an arbitrary base b.',
    variables: [
      { symbol: 'y', name: 'Logarithm result', unit: 'dimensionless' },
      { symbol: 'b', name: 'Base', unit: 'dimensionless' },
      { symbol: 'x', name: 'Argument', unit: 'dimensionless' },
    ],
    keywords: ['logarithm', 'log base', 'exponent inverse', 'log rules'],
    solve: {
      y: (v) => {
        if (v.x <= 0) throw new Error('The argument x must be positive.');
        if (v.b <= 0 || v.b === 1) throw new Error('The base must be positive and not equal to 1.');
        return Math.log(v.x) / Math.log(v.b);
      },
      x: (v) => {
        if (v.b <= 0) throw new Error('The base must be positive.');
        return v.b ** v.y;
      },
      b: (v) => {
        if (v.x <= 0) throw new Error('The argument x must be positive.');
        if (v.y === 0) throw new Error('y cannot be 0 — the base cannot be determined.');
        return v.x ** (1 / v.y);
      },
    },
  },
  {
    id: 'natural-logarithm',
    name: 'Natural Logarithm',
    category: 'Mathematics',
    subcategory: 'Precalculus',
    equation: 'y = ln(x)',
    description: 'Logarithm with base e (Euler’s number).',
    variables: [
      { symbol: 'y', name: 'ln(x)', unit: 'dimensionless' },
      { symbol: 'x', name: 'Input value', unit: 'dimensionless' },
    ],
    keywords: ['natural logarithm', 'ln', 'e', 'exponential', 'inverse'],
    solve: {
      y: (v) => {
        if (v.x <= 0) throw new Error('x must be positive.');
        return Math.log(v.x);
      },
      x: (v) => Math.exp(v.y),
    },
  },
  {
    id: 'vertex-form-parabola',
    name: 'Vertex Form of a Parabola',
    category: 'Mathematics',
    subcategory: 'Precalculus',
    equation: 'y = a(x − h)² + k',
    description: 'Describes a parabola from its vertex (h, k) and stretch factor a. Solving for x or h gives the principal (positive-offset) root.',
    variables: [
      { symbol: 'y', name: 'y', unit: 'dimensionless' },
      { symbol: 'a', name: 'Stretch/direction factor', unit: 'dimensionless' },
      { symbol: 'h', name: 'Vertex x-coordinate', unit: 'dimensionless' },
      { symbol: 'k', name: 'Vertex y-coordinate', unit: 'dimensionless' },
      { symbol: 'x', name: 'x', unit: 'dimensionless' },
    ],
    keywords: ['vertex form', 'parabola', 'quadratic transformation', 'function transformation'],
    solve: {
      y: (v) => v.a * (v.x - v.h) ** 2 + v.k,
      a: (v) => (v.y - v.k) / (v.x - v.h) ** 2,
      k: (v) => v.y - v.a * (v.x - v.h) ** 2,
      x: (v) => {
        const ratio = (v.y - v.k) / v.a;
        if (ratio < 0) throw new Error('No real solution — negative value under the square root.');
        return v.h + Math.sqrt(ratio);
      },
      h: (v) => {
        const ratio = (v.y - v.k) / v.a;
        if (ratio < 0) throw new Error('No real solution — negative value under the square root.');
        return v.x - Math.sqrt(ratio);
      },
    },
  },
  {
    id: 'continuous-compounding-growth',
    name: 'Continuous Exponential Growth',
    category: 'Mathematics',
    subcategory: 'Precalculus',
    equation: 'A = Pe^(rt)',
    description: 'Models continuous growth, such as interest compounded continuously.',
    variables: [
      { symbol: 'A', name: 'Final amount', unit: 'dimensionless' },
      { symbol: 'P', name: 'Initial amount', unit: 'dimensionless' },
      { symbol: 'r', name: 'Continuous growth rate', unit: 'per unit time' },
      { symbol: 't', name: 'Time', unit: 'dimensionless' },
    ],
    keywords: ['continuous compounding', 'exponential model', 'continuous growth', 'pert', 'logarithmic model'],
    solve: {
      A: (v) => v.P * Math.exp(v.r * v.t),
      P: (v) => v.A / Math.exp(v.r * v.t),
      r: (v) => {
        if (v.A <= 0 || v.P <= 0) throw new Error('Amounts must be positive.');
        return Math.log(v.A / v.P) / v.t;
      },
      t: (v) => {
        if (v.A <= 0 || v.P <= 0) throw new Error('Amounts must be positive.');
        return Math.log(v.A / v.P) / v.r;
      },
    },
  },
];
