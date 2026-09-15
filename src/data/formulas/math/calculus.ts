import type { Formula } from '../../../types';

export const calculusFormulas: Formula[] = [
  {
    id: 'limit-definition-derivative',
    name: 'Derivative (Limit Definition)',
    category: 'Mathematics',
    subcategory: 'Calculus',
    equation: "f'(x) = lim(h→0) [f(x+h) − f(x)] / h",
    description: 'Defines the derivative of f at x as the limit of its average rate of change as h approaches 0. Symbolic — plug in an explicit function to evaluate numerically.',
    variables: [
      { symbol: 'fPrime', name: "f'(x) — derivative", unit: 'dimensionless' },
      { symbol: 'fx', name: 'f(x) — function value at x', unit: 'dimensionless' },
      { symbol: 'h', name: 'Δx — small change in x', unit: 'dimensionless' },
    ],
    keywords: ['derivative', 'limit definition', 'difference quotient', 'rate of change'],
    solve: {},
  },
  {
    id: 'power-rule',
    name: 'Power Rule (Derivative)',
    category: 'Mathematics',
    subcategory: 'Calculus',
    equation: 'd/dx[xⁿ] = n·x^(n − 1)',
    description: 'Gives the derivative of xⁿ, evaluated at a specific point x.',
    variables: [
      { symbol: 'derivative', name: 'Derivative value at x', unit: 'dimensionless' },
      { symbol: 'n', name: 'Exponent', unit: 'dimensionless' },
      { symbol: 'x', name: 'Point of evaluation', unit: 'dimensionless' },
    ],
    keywords: ['power rule', 'derivative', 'calculus'],
    solve: {
      derivative: (v) => v.n * v.x ** (v.n - 1),
    },
  },
  {
    id: 'chain-rule',
    name: 'Chain Rule (Derivative)',
    category: 'Mathematics',
    subcategory: 'Calculus',
    equation: "d/dx[f(g(x))] = f'(g(x)) · g'(x)",
    description: "Derivative of a composite function, given the outer derivative evaluated at g(x) and the inner derivative.",
    variables: [
      { symbol: 'result', name: 'd/dx[f(g(x))]', unit: 'dimensionless' },
      { symbol: 'fPrimeOfG', name: "f'(g(x)) — outer derivative at g(x)", unit: 'dimensionless' },
      { symbol: 'gPrime', name: "g'(x) — inner derivative", unit: 'dimensionless' },
    ],
    keywords: ['chain rule', 'derivative', 'calculus', 'composite function'],
    solve: {
      result: (v) => v.fPrimeOfG * v.gPrime,
      fPrimeOfG: (v) => v.result / v.gPrime,
      gPrime: (v) => v.result / v.fPrimeOfG,
    },
  },
  {
    id: 'definite-integral',
    name: 'Fundamental Theorem of Calculus',
    category: 'Mathematics',
    subcategory: 'Calculus',
    equation: '∫ₐᵇ f(x)dx = F(b) − F(a)',
    description: 'Evaluates a definite integral from an antiderivative F evaluated at the bounds.',
    variables: [
      { symbol: 'integral', name: 'Definite integral value', unit: 'dimensionless' },
      { symbol: 'Fb', name: 'F(b) — antiderivative at upper bound', unit: 'dimensionless' },
      { symbol: 'Fa', name: 'F(a) — antiderivative at lower bound', unit: 'dimensionless' },
    ],
    keywords: ['fundamental theorem of calculus', 'definite integral', 'antiderivative'],
    solve: {
      integral: (v) => v.Fb - v.Fa,
      Fb: (v) => v.integral + v.Fa,
      Fa: (v) => v.Fb - v.integral,
    },
  },
  {
    id: 'product-rule',
    name: 'Product Rule (Derivative)',
    category: 'Mathematics',
    subcategory: 'Calculus',
    equation: "(fg)' = f'g + fg'",
    description: 'Derivative of a product of two functions, given their values and derivatives at a point.',
    variables: [
      { symbol: 'result', name: "(fg)' — derivative of the product", unit: 'dimensionless' },
      { symbol: 'f', name: 'f(x)', unit: 'dimensionless' },
      { symbol: 'fPrime', name: "f'(x)", unit: 'dimensionless' },
      { symbol: 'g', name: 'g(x)', unit: 'dimensionless' },
      { symbol: 'gPrime', name: "g'(x)", unit: 'dimensionless' },
    ],
    keywords: ['product rule', 'derivative', 'calculus'],
    solve: {
      result: (v) => v.fPrime * v.g + v.f * v.gPrime,
      fPrime: (v) => (v.result - v.f * v.gPrime) / v.g,
      gPrime: (v) => (v.result - v.fPrime * v.g) / v.f,
    },
  },
  {
    id: 'quotient-rule',
    name: 'Quotient Rule (Derivative)',
    category: 'Mathematics',
    subcategory: 'Calculus',
    equation: "(f/g)' = (f'g − fg') / g²",
    description: 'Derivative of a quotient of two functions, given their values and derivatives at a point.',
    variables: [
      { symbol: 'result', name: "(f/g)' — derivative of the quotient", unit: 'dimensionless' },
      { symbol: 'f', name: 'f(x)', unit: 'dimensionless' },
      { symbol: 'fPrime', name: "f'(x)", unit: 'dimensionless' },
      { symbol: 'g', name: 'g(x)', unit: 'dimensionless' },
      { symbol: 'gPrime', name: "g'(x)", unit: 'dimensionless' },
    ],
    keywords: ['quotient rule', 'derivative', 'calculus'],
    solve: {
      result: (v) => (v.fPrime * v.g - v.f * v.gPrime) / v.g ** 2,
      fPrime: (v) => (v.result * v.g ** 2 + v.f * v.gPrime) / v.g,
      gPrime: (v) => (v.fPrime * v.g - v.result * v.g ** 2) / v.f,
    },
  },
  {
    id: 'derivative-of-sine',
    name: 'Derivative of Sine',
    category: 'Mathematics',
    subcategory: 'Calculus',
    equation: 'd/dx[sin x] = cos x',
    description: 'Derivative of sin(x), evaluated at a point x (in radians).',
    variables: [
      { symbol: 'derivative', name: 'Derivative value at x', unit: 'dimensionless' },
      { symbol: 'x', name: 'Point of evaluation', unit: 'radians' },
    ],
    keywords: ['derivative of sine', 'd/dx sin x', 'trig derivative', 'common derivatives'],
    solve: {
      derivative: (v) => Math.cos(v.x),
    },
  },
  {
    id: 'derivative-of-exponential',
    name: 'Derivative of eˣ',
    category: 'Mathematics',
    subcategory: 'Calculus',
    equation: 'd/dx[eˣ] = eˣ',
    description: 'Derivative of the natural exponential function, evaluated at a point x.',
    variables: [
      { symbol: 'derivative', name: 'Derivative value at x', unit: 'dimensionless' },
      { symbol: 'x', name: 'Point of evaluation', unit: 'dimensionless' },
    ],
    keywords: ['derivative of exponential', 'd/dx e^x', 'common derivatives'],
    solve: {
      derivative: (v) => Math.exp(v.x),
      x: (v) => {
        if (v.derivative <= 0) throw new Error('The derivative of eˣ is always positive.');
        return Math.log(v.derivative);
      },
    },
  },
  {
    id: 'derivative-of-natural-log',
    name: 'Derivative of ln(x)',
    category: 'Mathematics',
    subcategory: 'Calculus',
    equation: 'd/dx[ln x] = 1/x',
    description: 'Derivative of the natural logarithm, evaluated at a point x > 0.',
    variables: [
      { symbol: 'derivative', name: 'Derivative value at x', unit: 'dimensionless' },
      { symbol: 'x', name: 'Point of evaluation', unit: 'dimensionless' },
    ],
    keywords: ['derivative of natural log', 'd/dx ln x', 'common derivatives'],
    solve: {
      derivative: (v) => {
        if (v.x <= 0) throw new Error('x must be positive since ln(x) is only defined for x > 0.');
        return 1 / v.x;
      },
      x: (v) => {
        if (v.derivative <= 0) throw new Error('The derivative of ln(x) is always positive since x > 0.');
        return 1 / v.derivative;
      },
    },
  },
  {
    id: 'integral-power-rule',
    name: 'Power Rule (Integral)',
    category: 'Mathematics',
    subcategory: 'Calculus',
    equation: '∫xⁿ dx = x^(n+1)/(n+1) + C   (n ≠ −1)',
    description: 'Antiderivative of a power function. Symbolic — produces a function of x plus an arbitrary constant, not a single value.',
    variables: [
      { symbol: 'n', name: 'Exponent', unit: 'dimensionless' },
      { symbol: 'x', name: 'Variable', unit: 'dimensionless' },
    ],
    keywords: ['integral power rule', 'antiderivative', 'indefinite integral', 'common integrals'],
    solve: {},
  },
  {
    id: 'integral-of-exponential',
    name: 'Integral of eˣ',
    category: 'Mathematics',
    subcategory: 'Calculus',
    equation: '∫eˣ dx = eˣ + C',
    description: 'Antiderivative of the natural exponential function. Symbolic — produces a function plus an arbitrary constant.',
    variables: [{ symbol: 'x', name: 'Variable', unit: 'dimensionless' }],
    keywords: ['integral of exponential', 'antiderivative', 'indefinite integral', 'common integrals'],
    solve: {},
  },
  {
    id: 'integral-of-reciprocal',
    name: 'Integral of 1/x',
    category: 'Mathematics',
    subcategory: 'Calculus',
    equation: '∫(1/x) dx = ln|x| + C   (x ≠ 0)',
    description: 'Antiderivative of 1/x. Symbolic — produces a function plus an arbitrary constant.',
    variables: [{ symbol: 'x', name: 'Variable', unit: 'dimensionless' }],
    keywords: ['integral of reciprocal', 'antiderivative', 'indefinite integral', 'common integrals'],
    solve: {},
  },
  {
    id: 'average-rate-of-change',
    name: 'Average Rate of Change',
    category: 'Mathematics',
    subcategory: 'Calculus',
    equation: '(f(b) − f(a)) / (b − a)',
    description: 'Calculates the average rate of change of a function over an interval [a, b] (the slope of the secant line).',
    variables: [
      { symbol: 'avgRate', name: 'Average rate of change', unit: 'dimensionless' },
      { symbol: 'fb', name: 'f(b)', unit: 'dimensionless' },
      { symbol: 'fa', name: 'f(a)', unit: 'dimensionless' },
      { symbol: 'a', name: 'a', unit: 'dimensionless' },
      { symbol: 'b', name: 'b', unit: 'dimensionless' },
    ],
    keywords: ['average rate of change', 'secant slope', 'difference quotient'],
    solve: {
      avgRate: (v) => (v.fb - v.fa) / (v.b - v.a),
      fb: (v) => v.avgRate * (v.b - v.a) + v.fa,
      fa: (v) => v.fb - v.avgRate * (v.b - v.a),
      a: (v) => v.b - (v.fb - v.fa) / v.avgRate,
      b: (v) => v.a + (v.fb - v.fa) / v.avgRate,
    },
  },
];
