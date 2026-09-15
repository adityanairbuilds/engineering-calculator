import type { Formula } from '../../../types';

const factorial = (num: number): number => {
  if (num < 0 || !Number.isInteger(num)) throw new Error('Factorial is only defined for non-negative whole numbers.');
  let result = 1;
  for (let i = 2; i <= num; i++) result *= i;
  return result;
};

export const statisticsFormulas: Formula[] = [
  {
    id: 'probability',
    name: 'Probability (Classical)',
    category: 'Mathematics',
    subcategory: 'Statistics',
    equation: 'P(A) = favorable / total',
    description: 'Calculates the probability of an event from its favorable and total outcomes.',
    variables: [
      { symbol: 'PA', name: 'Probability of event A', unit: 'dimensionless' },
      { symbol: 'favorable', name: 'Favorable outcomes', unit: 'dimensionless' },
      { symbol: 'total', name: 'Total possible outcomes', unit: 'dimensionless' },
    ],
    keywords: ['probability', 'odds', 'likelihood', 'chance'],
    solve: {
      PA: (v) => v.favorable / v.total,
      favorable: (v) => v.PA * v.total,
      total: (v) => v.favorable / v.PA,
    },
  },
  {
    id: 'z-score',
    name: 'Z-Score',
    category: 'Mathematics',
    subcategory: 'Statistics',
    equation: 'z = (x − μ) / σ',
    description: 'Standardizes a value relative to the mean and standard deviation of its distribution.',
    variables: [
      { symbol: 'z', name: 'Z-score', unit: 'dimensionless' },
      { symbol: 'x', name: 'Data value', unit: 'dimensionless' },
      { symbol: 'mu', name: 'Mean', unit: 'dimensionless' },
      { symbol: 'sigma', name: 'Standard deviation', unit: 'dimensionless' },
    ],
    keywords: ['z-score', 'standard score', 'normal distribution', 'standardize'],
    solve: {
      z: (v) => (v.x - v.mu) / v.sigma,
      x: (v) => v.mu + v.z * v.sigma,
      mu: (v) => v.x - v.z * v.sigma,
      sigma: (v) => (v.x - v.mu) / v.z,
    },
  },
  {
    id: 'permutations',
    name: 'Permutations',
    category: 'Mathematics',
    subcategory: 'Statistics',
    equation: 'P(n,r) = n! / (n − r)!',
    description: 'Counts the number of ordered arrangements of r items chosen from n items.',
    variables: [
      { symbol: 'Pnr', name: 'Number of permutations', unit: 'dimensionless' },
      { symbol: 'n', name: 'Total items', unit: 'dimensionless' },
      { symbol: 'r', name: 'Items arranged', unit: 'dimensionless' },
    ],
    keywords: ['permutations', 'arrangements', 'combinatorics', 'counting'],
    solve: {
      Pnr: (v) => {
        if (v.r > v.n) throw new Error('r cannot be greater than n.');
        return factorial(v.n) / factorial(v.n - v.r);
      },
    },
  },
  {
    id: 'combinations',
    name: 'Combinations',
    category: 'Mathematics',
    subcategory: 'Statistics',
    equation: 'C(n,r) = n! / (r!(n − r)!)',
    description: 'Counts the number of ways to choose r items from n items, order not mattering.',
    variables: [
      { symbol: 'Cnr', name: 'Number of combinations', unit: 'dimensionless' },
      { symbol: 'n', name: 'Total items', unit: 'dimensionless' },
      { symbol: 'r', name: 'Items chosen', unit: 'dimensionless' },
    ],
    keywords: ['combinations', 'choose', 'binomial coefficient', 'combinatorics'],
    solve: {
      Cnr: (v) => {
        if (v.r > v.n) throw new Error('r cannot be greater than n.');
        return factorial(v.n) / (factorial(v.r) * factorial(v.n - v.r));
      },
    },
  },
  {
    id: 'mean',
    name: 'Mean (from Sum)',
    category: 'Mathematics',
    subcategory: 'Statistics',
    equation: 'μ = Σx / n',
    description: 'Calculates the arithmetic mean from the sum of all data values and the count. Add up your data by hand first.',
    variables: [
      { symbol: 'mu', name: 'Mean', unit: 'dimensionless' },
      { symbol: 'sumX', name: 'Sum of all values (Σx)', unit: 'dimensionless' },
      { symbol: 'n', name: 'Number of values', unit: 'dimensionless' },
    ],
    keywords: ['mean', 'average', 'central tendency', 'arithmetic mean'],
    solve: {
      mu: (v) => v.sumX / v.n,
      sumX: (v) => v.mu * v.n,
      n: (v) => v.sumX / v.mu,
    },
  },
  {
    id: 'standard-deviation',
    name: 'Standard Deviation (Population)',
    category: 'Mathematics',
    subcategory: 'Statistics',
    equation: 'σ = √(Σ(x − μ)² / n)',
    description: 'Calculates population standard deviation from the sum of squared deviations from the mean. Compute Σ(x − μ)² by hand first.',
    variables: [
      { symbol: 'sigma', name: 'Standard deviation', unit: 'dimensionless' },
      { symbol: 'sumSqDev', name: 'Sum of squared deviations, Σ(x−μ)²', unit: 'dimensionless' },
      { symbol: 'n', name: 'Number of values', unit: 'dimensionless' },
    ],
    keywords: ['standard deviation', 'spread', 'population standard deviation', 'dispersion'],
    solve: {
      sigma: (v) => {
        if (v.sumSqDev < 0) throw new Error('Sum of squared deviations cannot be negative.');
        return Math.sqrt(v.sumSqDev / v.n);
      },
      sumSqDev: (v) => v.sigma ** 2 * v.n,
      n: (v) => v.sumSqDev / v.sigma ** 2,
    },
  },
  {
    id: 'population-variance',
    name: 'Variance (Population)',
    category: 'Mathematics',
    subcategory: 'Statistics',
    equation: 'σ² = Σ(x − μ)² / n',
    description: 'Calculates population variance from the sum of squared deviations from the mean. Compute Σ(x − μ)² by hand first.',
    variables: [
      { symbol: 'sigma2', name: 'Variance', unit: 'dimensionless' },
      { symbol: 'sumSqDev', name: 'Sum of squared deviations, Σ(x−μ)²', unit: 'dimensionless' },
      { symbol: 'n', name: 'Number of values', unit: 'dimensionless' },
    ],
    keywords: ['variance', 'population variance', 'spread', 'dispersion'],
    solve: {
      sigma2: (v) => v.sumSqDev / v.n,
      sumSqDev: (v) => v.sigma2 * v.n,
      n: (v) => v.sumSqDev / v.sigma2,
    },
  },
  {
    id: 'weighted-mean',
    name: 'Weighted Mean',
    category: 'Mathematics',
    subcategory: 'Statistics',
    equation: 'x̄ = Σ(w·x) / Σw',
    description: 'Calculates a weighted average from the sum of weight×value products and the sum of weights. Compute both sums by hand first.',
    variables: [
      { symbol: 'xbar', name: 'Weighted mean', unit: 'dimensionless' },
      { symbol: 'sumWX', name: 'Sum of weight×value products, Σ(wx)', unit: 'dimensionless' },
      { symbol: 'sumW', name: 'Sum of weights, Σw', unit: 'dimensionless' },
    ],
    keywords: ['weighted mean', 'weighted average'],
    solve: {
      xbar: (v) => v.sumWX / v.sumW,
      sumWX: (v) => v.xbar * v.sumW,
      sumW: (v) => v.sumWX / v.xbar,
    },
  },
  {
    id: 'expected-value-discrete',
    name: 'Expected Value (Discrete, Two Outcomes)',
    category: 'Mathematics',
    subcategory: 'Statistics',
    equation: 'E(X) = x₁P(x₁) + x₂P(x₂)',
    description: 'Calculates the expected value of a discrete random variable with two possible outcomes; extend the same pattern by hand for more outcomes.',
    variables: [
      { symbol: 'Ex', name: 'Expected value', unit: 'dimensionless' },
      { symbol: 'x1', name: 'Outcome 1 value', unit: 'dimensionless' },
      { symbol: 'p1', name: 'Probability of outcome 1', unit: 'dimensionless' },
      { symbol: 'x2', name: 'Outcome 2 value', unit: 'dimensionless' },
      { symbol: 'p2', name: 'Probability of outcome 2', unit: 'dimensionless' },
    ],
    keywords: ['expected value', 'discrete random variable', 'probability distribution'],
    solve: {
      Ex: (v) => v.x1 * v.p1 + v.x2 * v.p2,
      x1: (v) => (v.Ex - v.x2 * v.p2) / v.p1,
      x2: (v) => (v.Ex - v.x1 * v.p1) / v.p2,
    },
  },
  {
    id: 'binomial-probability',
    name: 'Binomial Probability',
    category: 'Mathematics',
    subcategory: 'Statistics',
    equation: 'P(X=k) = C(n,k) pᵏ(1 − p)ⁿ⁻ᵏ',
    description: 'Calculates the probability of exactly k successes in n independent trials with success probability p.',
    variables: [
      { symbol: 'P', name: 'Probability of exactly k successes', unit: 'dimensionless' },
      { symbol: 'n', name: 'Number of trials', unit: 'dimensionless' },
      { symbol: 'k', name: 'Number of successes', unit: 'dimensionless' },
      { symbol: 'p', name: 'Probability of success per trial', unit: 'dimensionless' },
    ],
    keywords: ['binomial probability', 'binomial distribution', 'bernoulli trials'],
    solve: {
      P: (v) => {
        if (v.k > v.n) throw new Error('k cannot exceed n.');
        if (v.p < 0 || v.p > 1) throw new Error('p must be between 0 and 1.');
        const combos = factorial(v.n) / (factorial(v.k) * factorial(v.n - v.k));
        return combos * v.p ** v.k * (1 - v.p) ** (v.n - v.k);
      },
    },
  },
];
