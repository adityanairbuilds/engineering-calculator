import type { Formula } from '../../../types';

export const electricityFormulas: Formula[] = [
  {
    id: 'coulombs-law',
    name: "Coulomb's Law",
    category: 'Physics',
    subcategory: 'Electricity',
    equation: 'F = kq₁q₂ / r²',
    description: 'Calculates the electric force between two point charges.',
    variables: [
      { symbol: 'F', name: 'Electric force', unit: 'N' },
      { symbol: 'k', name: "Coulomb constant (≈8.99×10⁹)", unit: 'N·m²/C²' },
      { symbol: 'q1', name: 'Charge 1', unit: 'C' },
      { symbol: 'q2', name: 'Charge 2', unit: 'C' },
      { symbol: 'r', name: 'Distance between charges', unit: 'm' },
    ],
    keywords: ['coulomb', "coulomb's law", 'electric force', 'charge', 'electricity'],
    solve: {
      F: (v) => (v.k * v.q1 * v.q2) / v.r ** 2,
      k: (v) => (v.F * v.r ** 2) / (v.q1 * v.q2),
      q1: (v) => (v.F * v.r ** 2) / (v.k * v.q2),
      q2: (v) => (v.F * v.r ** 2) / (v.k * v.q1),
      r: (v) => {
        const sq = (v.k * v.q1 * v.q2) / v.F;
        if (sq < 0) throw new Error('kq₁q₂/F is negative — no real distance.');
        return Math.sqrt(sq);
      },
    },
  },
  {
    id: 'electric-field',
    name: 'Electric Field',
    category: 'Physics',
    subcategory: 'Electricity',
    equation: 'E = F / q',
    description: 'Calculates the electric field from the force it exerts on a test charge.',
    variables: [
      { symbol: 'E', name: 'Electric field', unit: 'N/C' },
      { symbol: 'F', name: 'Electric force', unit: 'N' },
      { symbol: 'q', name: 'Test charge', unit: 'C' },
    ],
    keywords: ['electric field', 'electricity', 'charge', 'force'],
    solve: {
      E: (v) => v.F / v.q,
      F: (v) => v.E * v.q,
      q: (v) => v.F / v.E,
    },
  },
  {
    id: 'electric-potential',
    name: 'Electric Potential',
    category: 'Physics',
    subcategory: 'Electricity',
    equation: 'V = W / q',
    description: 'Calculates electric potential (voltage) from the work done moving a charge.',
    variables: [
      { symbol: 'V', name: 'Electric potential', unit: 'V' },
      { symbol: 'W', name: 'Work done on charge', unit: 'J' },
      { symbol: 'q', name: 'Charge', unit: 'C' },
    ],
    keywords: ['electric potential', 'voltage', 'electricity', 'charge'],
    solve: {
      V: (v) => v.W / v.q,
      W: (v) => v.V * v.q,
      q: (v) => v.W / v.V,
    },
  },
  {
    id: 'electric-potential-energy',
    name: 'Electric Potential Energy',
    category: 'Physics',
    subcategory: 'Electricity',
    equation: 'U = kq₁q₂ / r',
    description: 'Calculates the electric potential energy between two point charges.',
    variables: [
      { symbol: 'U', name: 'Potential energy', unit: 'J' },
      { symbol: 'k', name: 'Coulomb constant (≈8.99×10⁹)', unit: 'N·m²/C²' },
      { symbol: 'q1', name: 'Charge 1', unit: 'C' },
      { symbol: 'q2', name: 'Charge 2', unit: 'C' },
      { symbol: 'r', name: 'Distance between charges', unit: 'm' },
    ],
    keywords: ['electric potential energy', 'charge', 'electricity'],
    solve: {
      U: (v) => (v.k * v.q1 * v.q2) / v.r,
      k: (v) => (v.U * v.r) / (v.q1 * v.q2),
      q1: (v) => (v.U * v.r) / (v.k * v.q2),
      q2: (v) => (v.U * v.r) / (v.k * v.q1),
      r: (v) => (v.k * v.q1 * v.q2) / v.U,
    },
  },
  {
    id: 'electric-flux',
    name: "Gauss's Law (Electric Flux)",
    category: 'Physics',
    subcategory: 'Electricity',
    equation: 'Φ = EA cos(θ)',
    description: 'Calculates the electric flux through a flat surface in a uniform electric field.',
    variables: [
      { symbol: 'Phi', name: 'Electric flux', unit: 'N·m²/C' },
      { symbol: 'E', name: 'Electric field', unit: 'N/C' },
      { symbol: 'A', name: 'Surface area', unit: 'm²' },
      { symbol: 'theta', name: 'Angle between field and surface normal', unit: '°' },
    ],
    keywords: ['electric flux', 'gauss', "gauss's law", 'electric field', 'electricity'],
    solve: {
      Phi: (v) => v.E * v.A * Math.cos((v.theta * Math.PI) / 180),
      E: (v) => v.Phi / (v.A * Math.cos((v.theta * Math.PI) / 180)),
      A: (v) => v.Phi / (v.E * Math.cos((v.theta * Math.PI) / 180)),
      theta: (v) => {
        const ratio = v.Phi / (v.E * v.A);
        if (ratio < -1 || ratio > 1) throw new Error('Φ/(EA) must be between -1 and 1.');
        return Math.acos(ratio) * (180 / Math.PI);
      },
    },
  },
  {
    id: 'electric-current',
    name: 'Electric Current',
    category: 'Physics',
    subcategory: 'Electricity',
    equation: 'I = Q / t',
    description: 'Calculates the average electric current from the charge that flows past a point over time.',
    variables: [
      { symbol: 'I', name: 'Current', unit: 'A' },
      { symbol: 'Q', name: 'Charge', unit: 'C' },
      { symbol: 't', name: 'Time', unit: 's' },
    ],
    keywords: ['electric current', 'current', 'charge', 'amperes', 'electricity'],
    solve: {
      I: (v) => v.Q / v.t,
      Q: (v) => v.I * v.t,
      t: (v) => v.Q / v.I,
    },
  },
  {
    id: 'capacitor-energy',
    name: 'Energy Stored in a Capacitor',
    category: 'Physics',
    subcategory: 'Electricity',
    equation: 'U = ½CV²',
    description: 'Calculates the electrical energy stored in a charged capacitor.',
    variables: [
      { symbol: 'U', name: 'Stored energy', unit: 'J' },
      { symbol: 'C', name: 'Capacitance', unit: 'F' },
      { symbol: 'V', name: 'Voltage', unit: 'V' },
    ],
    keywords: ['capacitor energy', 'stored energy', 'capacitance', 'voltage', 'electricity'],
    solve: {
      U: (v) => 0.5 * v.C * v.V ** 2,
      C: (v) => (2 * v.U) / v.V ** 2,
      V: (v) => {
        const sq = (2 * v.U) / v.C;
        if (sq < 0) throw new Error('2U/C is negative — no real voltage.');
        return Math.sqrt(sq);
      },
    },
  },
];
