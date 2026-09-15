import type { Formula } from '../../../types';

export const circuitsFormulas: Formula[] = [
  {
    id: 'ohms-law',
    name: "Ohm's Law",
    category: 'Physics',
    subcategory: 'Circuits',
    equation: 'V = IR',
    description: 'Relates voltage, current, and resistance in a circuit.',
    variables: [
      { symbol: 'V', name: 'Voltage', unit: 'V' },
      { symbol: 'I', name: 'Current', unit: 'A' },
      { symbol: 'R', name: 'Resistance', unit: 'Ω' },
    ],
    keywords: ['ohms law', "ohm's law", 'voltage', 'current', 'resistance', 'electric resistance', 'v=ir'],
    solve: {
      V: (v) => v.I * v.R,
      I: (v) => v.V / v.R,
      R: (v) => v.V / v.I,
    },
  },
  {
    id: 'electrical-power',
    name: 'Electrical Power',
    category: 'Physics',
    subcategory: 'Circuits',
    equation: 'P = IV',
    description: 'Calculates electrical power from current and voltage.',
    variables: [
      { symbol: 'P', name: 'Power', unit: 'W' },
      { symbol: 'I', name: 'Current', unit: 'A' },
      { symbol: 'V', name: 'Voltage', unit: 'V' },
    ],
    keywords: ['electrical power', 'power', 'watts', 'p=iv'],
    solve: {
      P: (v) => v.I * v.V,
      I: (v) => v.P / v.V,
      V: (v) => v.P / v.I,
    },
  },
  {
    id: 'series-resistance',
    name: 'Series Resistance',
    category: 'Physics',
    subcategory: 'Circuits',
    equation: 'R_total = R₁ + R₂',
    description: 'Combines two resistors in series. Add more R terms by hand for additional resistors.',
    variables: [
      { symbol: 'Rt', name: 'Total resistance', unit: 'Ω' },
      { symbol: 'R1', name: 'Resistor 1', unit: 'Ω' },
      { symbol: 'R2', name: 'Resistor 2', unit: 'Ω' },
    ],
    keywords: ['series resistance', 'resistors in series', 'total resistance'],
    solve: {
      Rt: (v) => v.R1 + v.R2,
      R1: (v) => v.Rt - v.R2,
      R2: (v) => v.Rt - v.R1,
    },
  },
  {
    id: 'parallel-resistance',
    name: 'Parallel Resistance',
    category: 'Physics',
    subcategory: 'Circuits',
    equation: '1/R_total = 1/R₁ + 1/R₂',
    description: 'Combines two resistors in parallel.',
    variables: [
      { symbol: 'Rt', name: 'Total resistance', unit: 'Ω' },
      { symbol: 'R1', name: 'Resistor 1', unit: 'Ω' },
      { symbol: 'R2', name: 'Resistor 2', unit: 'Ω' },
    ],
    keywords: ['parallel resistance', 'resistors in parallel', 'total resistance'],
    solve: {
      Rt: (v) => (v.R1 * v.R2) / (v.R1 + v.R2),
      R1: (v) => {
        if (v.R2 <= v.Rt) throw new Error('R2 must be greater than the total resistance.');
        return (v.Rt * v.R2) / (v.R2 - v.Rt);
      },
      R2: (v) => {
        if (v.R1 <= v.Rt) throw new Error('R1 must be greater than the total resistance.');
        return (v.Rt * v.R1) / (v.R1 - v.Rt);
      },
    },
  },
  {
    id: 'power-current-resistance',
    name: 'Electrical Power (Current & Resistance)',
    category: 'Physics',
    subcategory: 'Circuits',
    equation: 'P = I²R',
    description: 'Calculates electrical power dissipated from current and resistance.',
    variables: [
      { symbol: 'P', name: 'Power', unit: 'W' },
      { symbol: 'I', name: 'Current', unit: 'A' },
      { symbol: 'R', name: 'Resistance', unit: 'Ω' },
    ],
    keywords: ['power', 'current', 'resistance', 'watts', 'dissipation', 'i squared r'],
    solve: {
      P: (v) => v.I ** 2 * v.R,
      I: (v) => {
        const sq = v.P / v.R;
        if (sq < 0) throw new Error('P/R is negative — no real current.');
        return Math.sqrt(sq);
      },
      R: (v) => v.P / v.I ** 2,
    },
  },
  {
    id: 'power-voltage-resistance',
    name: 'Electrical Power (Voltage & Resistance)',
    category: 'Physics',
    subcategory: 'Circuits',
    equation: 'P = V²/R',
    description: 'Calculates electrical power dissipated from voltage and resistance.',
    variables: [
      { symbol: 'P', name: 'Power', unit: 'W' },
      { symbol: 'V', name: 'Voltage', unit: 'V' },
      { symbol: 'R', name: 'Resistance', unit: 'Ω' },
    ],
    keywords: ['power', 'voltage', 'resistance', 'watts', 'dissipation', 'v squared over r'],
    solve: {
      P: (v) => v.V ** 2 / v.R,
      V: (v) => {
        const sq = v.P * v.R;
        if (sq < 0) throw new Error('P·R is negative — no real voltage.');
        return Math.sqrt(sq);
      },
      R: (v) => v.V ** 2 / v.P,
    },
  },
  {
    id: 'resistivity',
    name: 'Resistivity',
    category: 'Physics',
    subcategory: 'Circuits',
    equation: 'R = ρL / A',
    description: 'Calculates the resistance of a conductor from its resistivity, length, and cross-sectional area.',
    variables: [
      { symbol: 'R', name: 'Resistance', unit: 'Ω' },
      { symbol: 'rho', name: 'Resistivity', unit: 'Ω·m' },
      { symbol: 'L', name: 'Length of conductor', unit: 'm' },
      { symbol: 'A', name: 'Cross-sectional area', unit: 'm²' },
    ],
    keywords: ['resistivity', 'resistance', 'conductor', 'circuit', 'wire'],
    solve: {
      R: (v) => (v.rho * v.L) / v.A,
      rho: (v) => (v.R * v.A) / v.L,
      L: (v) => (v.R * v.A) / v.rho,
      A: (v) => (v.rho * v.L) / v.R,
    },
  },
  {
    id: 'capacitance',
    name: 'Capacitance',
    category: 'Physics',
    subcategory: 'Circuits',
    equation: 'C = Q / V',
    description: 'Calculates capacitance from stored charge and voltage.',
    variables: [
      { symbol: 'C', name: 'Capacitance', unit: 'F' },
      { symbol: 'Q', name: 'Charge', unit: 'C' },
      { symbol: 'V', name: 'Voltage', unit: 'V' },
    ],
    keywords: ['capacitance', 'capacitor', 'charge', 'voltage', 'circuit'],
    solve: {
      C: (v) => v.Q / v.V,
      Q: (v) => v.C * v.V,
      V: (v) => v.Q / v.C,
    },
  },
  {
    id: 'parallel-plate-capacitor',
    name: 'Parallel Plate Capacitor',
    category: 'Physics',
    subcategory: 'Circuits',
    equation: 'C = ε₀εᵣA / d',
    description: 'Calculates the capacitance of a parallel plate capacitor from plate area, separation, and the dielectric.',
    variables: [
      { symbol: 'C', name: 'Capacitance', unit: 'F' },
      { symbol: 'eps0', name: 'Permittivity of free space (≈8.854×10⁻¹²)', unit: 'F/m' },
      { symbol: 'epsR', name: 'Relative permittivity of dielectric', unit: 'dimensionless' },
      { symbol: 'A', name: 'Plate area', unit: 'm²' },
      { symbol: 'd', name: 'Plate separation', unit: 'm' },
    ],
    keywords: ['parallel plate', 'capacitor', 'capacitance', 'circuit', 'dielectric'],
    solve: {
      C: (v) => (v.eps0 * v.epsR * v.A) / v.d,
      eps0: (v) => (v.C * v.d) / (v.epsR * v.A),
      epsR: (v) => (v.C * v.d) / (v.eps0 * v.A),
      A: (v) => (v.C * v.d) / (v.eps0 * v.epsR),
      d: (v) => (v.eps0 * v.epsR * v.A) / v.C,
    },
  },
];
