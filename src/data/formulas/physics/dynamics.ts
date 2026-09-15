import type { Formula } from '../../../types';

export const dynamicsFormulas: Formula[] = [
  {
    id: 'newtons-second-law',
    name: "Newton's Second Law",
    category: 'Physics',
    subcategory: 'Dynamics',
    equation: 'F = ma',
    description: 'Calculates the net force on an object from its mass and acceleration.',
    variables: [
      { symbol: 'F', name: 'Force', unit: 'N' },
      { symbol: 'm', name: 'Mass', unit: 'kg' },
      { symbol: 'a', name: 'Acceleration', unit: 'm/s²' },
    ],
    keywords: ['force', 'mass', 'acceleration', 'newton', "newton's second law", 'f=ma'],
    solve: {
      F: (v) => v.m * v.a,
      m: (v) => v.F / v.a,
      a: (v) => v.F / v.m,
    },
  },
  {
    id: 'weight',
    name: 'Weight',
    category: 'Physics',
    subcategory: 'Dynamics',
    equation: 'W = mg',
    description: 'Calculates the gravitational force (weight) on a mass.',
    variables: [
      { symbol: 'W', name: 'Weight', unit: 'N' },
      { symbol: 'm', name: 'Mass', unit: 'kg' },
      { symbol: 'g', name: 'Gravitational acceleration', unit: 'm/s²' },
    ],
    keywords: ['weight', 'gravity', 'gravitational force'],
    solve: {
      W: (v) => v.m * v.g,
      m: (v) => v.W / v.g,
      g: (v) => v.W / v.m,
    },
  },
  {
    id: 'friction-force',
    name: 'Friction Force',
    category: 'Physics',
    subcategory: 'Dynamics',
    equation: 'f = μN',
    description: 'Calculates the friction force from the coefficient of friction and the normal force.',
    variables: [
      { symbol: 'f', name: 'Friction force', unit: 'N' },
      { symbol: 'mu', name: 'Coefficient of friction', unit: 'dimensionless' },
      { symbol: 'N', name: 'Normal force', unit: 'N' },
    ],
    keywords: ['friction', 'coefficient of friction', 'normal force'],
    solve: {
      f: (v) => v.mu * v.N,
      mu: (v) => v.f / v.N,
      N: (v) => v.f / v.mu,
    },
  },
  {
    id: 'force-components-horizontal',
    name: 'Force Component (Horizontal)',
    category: 'Physics',
    subcategory: 'Dynamics',
    equation: 'Fₓ = F cos(θ)',
    description: 'Finds the horizontal component of a force applied at an angle from horizontal.',
    variables: [
      { symbol: 'Fx', name: 'Horizontal component', unit: 'N' },
      { symbol: 'F', name: 'Force magnitude', unit: 'N' },
      { symbol: 'theta', name: 'Angle from horizontal', unit: '°' },
    ],
    keywords: ['force components', 'horizontal force', 'vector components'],
    solve: {
      Fx: (v) => v.F * Math.cos((v.theta * Math.PI) / 180),
    },
  },
  {
    id: 'tension-pulley',
    name: 'Tension in an Atwood Machine',
    category: 'Physics',
    subcategory: 'Dynamics',
    equation: 'T = 2m₁m₂g / (m₁ + m₂)',
    description: 'Calculates the string tension for two masses connected over a frictionless, massless pulley (Atwood machine).',
    variables: [
      { symbol: 'T', name: 'Tension', unit: 'N' },
      { symbol: 'm1', name: 'Mass 1', unit: 'kg' },
      { symbol: 'm2', name: 'Mass 2', unit: 'kg' },
      { symbol: 'g', name: 'Gravitational acceleration', unit: 'm/s²' },
    ],
    keywords: ['tension', 'pulley', 'atwood machine', 'dynamics', 'force', 'mass'],
    solve: {
      T: (v) => (2 * v.m1 * v.m2 * v.g) / (v.m1 + v.m2),
      m1: (v) => (v.T * v.m2) / (2 * v.m2 * v.g - v.T),
      m2: (v) => (v.T * v.m1) / (2 * v.m1 * v.g - v.T),
      g: (v) => (v.T * (v.m1 + v.m2)) / (2 * v.m1 * v.m2),
    },
  },
];
