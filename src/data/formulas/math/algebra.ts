import type { Formula } from '../../../types';

export const algebraFormulas: Formula[] = [
  {
    id: 'slope-between-two-points',
    name: 'Slope',
    category: 'Mathematics',
    subcategory: 'Algebra',
    equation: 'm = (y₂ − y₁) / (x₂ − x₁)',
    description: 'Finds the slope of a line through two points.',
    variables: [
      { symbol: 'm', name: 'Slope', unit: 'dimensionless' },
      { symbol: 'x1', name: 'x of point 1', unit: 'dimensionless' },
      { symbol: 'y1', name: 'y of point 1', unit: 'dimensionless' },
      { symbol: 'x2', name: 'x of point 2', unit: 'dimensionless' },
      { symbol: 'y2', name: 'y of point 2', unit: 'dimensionless' },
    ],
    keywords: ['slope', 'gradient', 'line', 'rise over run'],
    solve: {
      m: (v) => {
        if (v.x2 === v.x1) throw new Error('The line is vertical — slope is undefined.');
        return (v.y2 - v.y1) / (v.x2 - v.x1);
      },
    },
  },
  {
    id: 'distance-formula-2d',
    name: 'Distance Formula',
    category: 'Mathematics',
    subcategory: 'Algebra',
    equation: 'd = √((x₂ − x₁)² + (y₂ − y₁)²)',
    description: 'Finds the straight-line distance between two points on a plane.',
    variables: [
      { symbol: 'd', name: 'Distance', unit: 'dimensionless' },
      { symbol: 'x1', name: 'x of point 1', unit: 'dimensionless' },
      { symbol: 'y1', name: 'y of point 1', unit: 'dimensionless' },
      { symbol: 'x2', name: 'x of point 2', unit: 'dimensionless' },
      { symbol: 'y2', name: 'y of point 2', unit: 'dimensionless' },
    ],
    keywords: ['distance', 'two points', 'coordinate geometry'],
    solve: {
      d: (v) => Math.sqrt((v.x2 - v.x1) ** 2 + (v.y2 - v.y1) ** 2),
    },
  },
  {
    id: 'midpoint-formula',
    name: 'Midpoint Formula',
    category: 'Mathematics',
    subcategory: 'Algebra',
    equation: 'M = ((x₁ + x₂) / 2, (y₁ + y₂) / 2)',
    description: "Finds the x-coordinate of the midpoint between two points (solve again with x and y swapped for Mᵧ).",
    variables: [
      { symbol: 'Mx', name: 'Midpoint x', unit: 'dimensionless' },
      { symbol: 'x1', name: 'x of point 1', unit: 'dimensionless' },
      { symbol: 'x2', name: 'x of point 2', unit: 'dimensionless' },
    ],
    keywords: ['midpoint', 'coordinate geometry', 'center point'],
    solve: {
      Mx: (v) => (v.x1 + v.x2) / 2,
    },
  },
  {
    id: 'quadratic-formula',
    name: 'Quadratic Formula',
    category: 'Mathematics',
    subcategory: 'Algebra',
    equation: 'x = (−b + √(b² − 4ac)) / 2a',
    description: 'Solves ax² + bx + c = 0 for the larger root. For the second root, flip the sign in front of the square root by hand.',
    variables: [
      { symbol: 'x', name: 'Root', unit: 'dimensionless' },
      { symbol: 'a', name: 'Quadratic coefficient', unit: 'dimensionless' },
      { symbol: 'b', name: 'Linear coefficient', unit: 'dimensionless' },
      { symbol: 'c', name: 'Constant term', unit: 'dimensionless' },
    ],
    keywords: ['quadratic', 'roots', 'parabola', 'ax^2+bx+c'],
    solve: {
      x: (v) => {
        if (v.a === 0) throw new Error('a cannot be 0 — this would not be a quadratic equation.');
        const discriminant = v.b ** 2 - 4 * v.a * v.c;
        if (discriminant < 0) throw new Error('Negative discriminant — no real roots.');
        return (-v.b + Math.sqrt(discriminant)) / (2 * v.a);
      },
    },
  },
  {
    id: 'arithmetic-sequence-nth-term',
    name: 'Arithmetic Sequence (nth Term)',
    category: 'Mathematics',
    subcategory: 'Algebra',
    equation: 'aₙ = a₁ + (n − 1)d',
    description: 'Finds the nth term of an arithmetic sequence.',
    variables: [
      { symbol: 'an', name: 'nth term', unit: 'dimensionless' },
      { symbol: 'a1', name: 'First term', unit: 'dimensionless' },
      { symbol: 'n', name: 'Term number', unit: 'dimensionless' },
      { symbol: 'd', name: 'Common difference', unit: 'dimensionless' },
    ],
    keywords: ['arithmetic sequence', 'nth term', 'common difference'],
    solve: {
      an: (v) => v.a1 + (v.n - 1) * v.d,
    },
  },
  {
    id: 'geometric-sequence-nth-term',
    name: 'Geometric Sequence (nth Term)',
    category: 'Mathematics',
    subcategory: 'Algebra',
    equation: 'aₙ = a₁ · r^(n − 1)',
    description: 'Finds the nth term of a geometric sequence.',
    variables: [
      { symbol: 'an', name: 'nth term', unit: 'dimensionless' },
      { symbol: 'a1', name: 'First term', unit: 'dimensionless' },
      { symbol: 'r', name: 'Common ratio', unit: 'dimensionless' },
      { symbol: 'n', name: 'Term number', unit: 'dimensionless' },
    ],
    keywords: ['geometric sequence', 'nth term', 'common ratio'],
    solve: {
      an: (v) => v.a1 * v.r ** (v.n - 1),
    },
  },
  {
    id: 'compound-interest',
    name: 'Compound Interest',
    category: 'Mathematics',
    subcategory: 'Algebra',
    equation: 'A = P(1 + r/n)^(nt)',
    description: 'Calculates the future value of an investment earning compound interest.',
    variables: [
      { symbol: 'A', name: 'Final amount', unit: '$' },
      { symbol: 'P', name: 'Principal (initial amount)', unit: '$' },
      { symbol: 'r', name: 'Annual interest rate (decimal, e.g. 0.05 for 5%)', unit: 'dimensionless' },
      { symbol: 'n', name: 'Compounding periods per year', unit: 'dimensionless' },
      { symbol: 't', name: 'Time', unit: 'years' },
    ],
    keywords: ['compound interest', 'investment', 'finance', 'future value', 'principal'],
    solve: {
      A: (v) => v.P * (1 + v.r / v.n) ** (v.n * v.t),
      P: (v) => v.A / (1 + v.r / v.n) ** (v.n * v.t),
      t: (v) => {
        if (v.P <= 0 || v.A <= 0) throw new Error('Amounts must be positive.');
        return Math.log(v.A / v.P) / (v.n * Math.log(1 + v.r / v.n));
      },
      r: (v) => {
        if (v.P <= 0 || v.A <= 0) throw new Error('Amounts must be positive.');
        return v.n * ((v.A / v.P) ** (1 / (v.n * v.t)) - 1);
      },
    },
  },
  {
    id: 'exponent-product-rule',
    name: 'Product of Powers Rule',
    category: 'Mathematics',
    subcategory: 'Algebra',
    equation: 'aᵐ · aⁿ = a^(m + n)',
    description: 'Multiplies two powers with the same base by adding their exponents.',
    variables: [
      { symbol: 'result', name: 'Product, a^(m+n)', unit: 'dimensionless' },
      { symbol: 'a', name: 'Base', unit: 'dimensionless' },
      { symbol: 'm', name: 'First exponent', unit: 'dimensionless' },
      { symbol: 'n', name: 'Second exponent', unit: 'dimensionless' },
    ],
    keywords: ['exponent rules', 'product of powers', 'multiplying exponents', 'laws of exponents'],
    solve: {
      result: (v) => v.a ** (v.m + v.n),
    },
  },
  {
    id: 'exponent-power-rule',
    name: 'Power of a Power Rule',
    category: 'Mathematics',
    subcategory: 'Algebra',
    equation: '(aᵐ)ⁿ = a^(mn)',
    description: 'Raises a power to another power by multiplying the exponents.',
    variables: [
      { symbol: 'result', name: 'Result, a^(mn)', unit: 'dimensionless' },
      { symbol: 'a', name: 'Base', unit: 'dimensionless' },
      { symbol: 'm', name: 'Inner exponent', unit: 'dimensionless' },
      { symbol: 'n', name: 'Outer exponent', unit: 'dimensionless' },
    ],
    keywords: ['exponent rules', 'power of a power', 'laws of exponents'],
    solve: {
      result: (v) => (v.a ** v.m) ** v.n,
    },
  },
  {
    id: 'exponent-quotient-rule',
    name: 'Quotient of Powers Rule',
    category: 'Mathematics',
    subcategory: 'Algebra',
    equation: 'aᵐ / aⁿ = a^(m − n)',
    description: 'Divides two powers with the same base by subtracting their exponents.',
    variables: [
      { symbol: 'result', name: 'Quotient, a^(m−n)', unit: 'dimensionless' },
      { symbol: 'a', name: 'Base', unit: 'dimensionless' },
      { symbol: 'm', name: 'Numerator exponent', unit: 'dimensionless' },
      { symbol: 'n', name: 'Denominator exponent', unit: 'dimensionless' },
    ],
    keywords: ['exponent rules', 'quotient of powers', 'dividing exponents', 'laws of exponents'],
    solve: {
      result: (v) => v.a ** v.m / v.a ** v.n,
    },
  },
  {
    id: 'arithmetic-series-sum',
    name: 'Arithmetic Series Sum',
    category: 'Mathematics',
    subcategory: 'Algebra',
    equation: 'Sₙ = n(a₁ + aₙ) / 2',
    description: 'Sums the first n terms of an arithmetic sequence.',
    variables: [
      { symbol: 'S', name: 'Sum of n terms', unit: 'dimensionless' },
      { symbol: 'n', name: 'Number of terms', unit: 'dimensionless' },
      { symbol: 'a1', name: 'First term', unit: 'dimensionless' },
      { symbol: 'an', name: 'Last (nth) term', unit: 'dimensionless' },
    ],
    keywords: ['arithmetic series', 'sum of sequence', 'partial sum', 'series'],
    solve: {
      S: (v) => (v.n * (v.a1 + v.an)) / 2,
      n: (v) => (2 * v.S) / (v.a1 + v.an),
      a1: (v) => (2 * v.S) / v.n - v.an,
      an: (v) => (2 * v.S) / v.n - v.a1,
    },
  },
  {
    id: 'geometric-series-sum',
    name: 'Geometric Series Sum',
    category: 'Mathematics',
    subcategory: 'Algebra',
    equation: 'Sₙ = a₁(1 − rⁿ) / (1 − r)',
    description: 'Sums the first n terms of a geometric sequence (r ≠ 1).',
    variables: [
      { symbol: 'S', name: 'Sum of n terms', unit: 'dimensionless' },
      { symbol: 'a1', name: 'First term', unit: 'dimensionless' },
      { symbol: 'r', name: 'Common ratio', unit: 'dimensionless' },
      { symbol: 'n', name: 'Number of terms', unit: 'dimensionless' },
    ],
    keywords: ['geometric series', 'sum of sequence', 'partial sum', 'common ratio', 'series'],
    solve: {
      S: (v) => (v.a1 * (1 - v.r ** v.n)) / (1 - v.r),
      a1: (v) => (v.S * (1 - v.r)) / (1 - v.r ** v.n),
    },
  },
  {
    id: 'point-slope-form',
    name: 'Point-Slope Form of a Line',
    category: 'Mathematics',
    subcategory: 'Algebra',
    equation: 'y − y₁ = m(x − x₁)',
    description: 'Writes the equation of a line given its slope and one point on the line.',
    variables: [
      { symbol: 'y', name: 'y', unit: 'dimensionless' },
      { symbol: 'y1', name: 'y of known point', unit: 'dimensionless' },
      { symbol: 'm', name: 'Slope', unit: 'dimensionless' },
      { symbol: 'x', name: 'x', unit: 'dimensionless' },
      { symbol: 'x1', name: 'x of known point', unit: 'dimensionless' },
    ],
    keywords: ['point slope form', 'line equation', 'linear equation', 'slope'],
    solve: {
      y: (v) => v.y1 + v.m * (v.x - v.x1),
      m: (v) => (v.y - v.y1) / (v.x - v.x1),
      y1: (v) => v.y - v.m * (v.x - v.x1),
      x1: (v) => v.x - (v.y - v.y1) / v.m,
      x: (v) => v.x1 + (v.y - v.y1) / v.m,
    },
  },
  {
    id: 'percent-change',
    name: 'Percent Change',
    category: 'Mathematics',
    subcategory: 'Algebra',
    equation: '%Δ = ((new − old) / old) × 100',
    description: 'Calculates the percentage increase or decrease from an old value to a new value.',
    variables: [
      { symbol: 'percentChange', name: 'Percent change', unit: '%' },
      { symbol: 'oldValue', name: 'Old value', unit: 'dimensionless' },
      { symbol: 'newValue', name: 'New value', unit: 'dimensionless' },
    ],
    keywords: ['percent change', 'percentage increase', 'percentage decrease', 'percent difference'],
    solve: {
      percentChange: (v) => ((v.newValue - v.oldValue) / v.oldValue) * 100,
      newValue: (v) => v.oldValue * (1 + v.percentChange / 100),
      oldValue: (v) => v.newValue / (1 + v.percentChange / 100),
    },
  },
];
