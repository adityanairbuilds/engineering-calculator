import type { Formula } from '../../../types';

export const magnetismFormulas: Formula[] = [
  {
    id: 'magnetic-force-charge',
    name: 'Magnetic Force on a Moving Charge',
    category: 'Physics',
    subcategory: 'Magnetism',
    equation: 'F = qvB sin(θ)',
    description: 'Calculates the force on a charged particle moving through a magnetic field.',
    variables: [
      { symbol: 'F', name: 'Magnetic force', unit: 'N' },
      { symbol: 'q', name: 'Charge', unit: 'C' },
      { symbol: 'v', name: 'Velocity', unit: 'm/s' },
      { symbol: 'B', name: 'Magnetic field strength', unit: 'T' },
      { symbol: 'theta', name: 'Angle between velocity and field', unit: '°' },
    ],
    keywords: ['magnetic force', 'lorentz force', 'charge', 'velocity', 'magnetic field'],
    solve: {
      F: (v) => v.q * v.v * v.B * Math.sin((v.theta * Math.PI) / 180),
      q: (v) => v.F / (v.v * v.B * Math.sin((v.theta * Math.PI) / 180)),
      v: (v) => v.F / (v.q * v.B * Math.sin((v.theta * Math.PI) / 180)),
      B: (v) => v.F / (v.q * v.v * Math.sin((v.theta * Math.PI) / 180)),
      theta: (v) => {
        const ratio = v.F / (v.q * v.v * v.B);
        if (ratio < -1 || ratio > 1) throw new Error('F/(qvB) must be between -1 and 1.');
        return Math.asin(ratio) * (180 / Math.PI);
      },
    },
  },
  {
    id: 'magnetic-force-current',
    name: 'Magnetic Force on a Current-Carrying Wire',
    category: 'Physics',
    subcategory: 'Magnetism',
    equation: 'F = ILB sin(θ)',
    description: 'Calculates the force on a current-carrying conductor placed in a magnetic field.',
    variables: [
      { symbol: 'F', name: 'Magnetic force', unit: 'N' },
      { symbol: 'I', name: 'Current', unit: 'A' },
      { symbol: 'L', name: 'Length of conductor', unit: 'm' },
      { symbol: 'B', name: 'Magnetic field strength', unit: 'T' },
      { symbol: 'theta', name: 'Angle between conductor and field', unit: '°' },
    ],
    keywords: ['magnetic force', 'current-carrying wire', 'conductor', 'magnetic field'],
    solve: {
      F: (v) => v.I * v.L * v.B * Math.sin((v.theta * Math.PI) / 180),
      I: (v) => v.F / (v.L * v.B * Math.sin((v.theta * Math.PI) / 180)),
      L: (v) => v.F / (v.I * v.B * Math.sin((v.theta * Math.PI) / 180)),
      B: (v) => v.F / (v.I * v.L * Math.sin((v.theta * Math.PI) / 180)),
      theta: (v) => {
        const ratio = v.F / (v.I * v.L * v.B);
        if (ratio < -1 || ratio > 1) throw new Error('F/(ILB) must be between -1 and 1.');
        return Math.asin(ratio) * (180 / Math.PI);
      },
    },
  },
  {
    id: 'magnetic-field-wire',
    name: 'Magnetic Field Around a Straight Wire',
    category: 'Physics',
    subcategory: 'Magnetism',
    equation: 'B = μ₀I / (2πr)',
    description: 'Calculates the magnetic field strength at a distance from a long straight current-carrying wire.',
    variables: [
      { symbol: 'B', name: 'Magnetic field', unit: 'T' },
      { symbol: 'mu0', name: 'Permeability of free space (≈4π×10⁻⁷)', unit: 'T·m/A' },
      { symbol: 'I', name: 'Current', unit: 'A' },
      { symbol: 'r', name: 'Distance from wire', unit: 'm' },
    ],
    keywords: ['magnetic field', 'wire', 'current', 'permeability', 'ampere'],
    solve: {
      B: (v) => (v.mu0 * v.I) / (2 * Math.PI * v.r),
      mu0: (v) => (v.B * 2 * Math.PI * v.r) / v.I,
      I: (v) => (v.B * 2 * Math.PI * v.r) / v.mu0,
      r: (v) => (v.mu0 * v.I) / (2 * Math.PI * v.B),
    },
  },
  {
    id: 'magnetic-flux',
    name: 'Magnetic Flux',
    category: 'Physics',
    subcategory: 'Magnetism',
    equation: 'Φ = BA cos(θ)',
    description: 'Calculates the magnetic flux through a flat surface in a uniform magnetic field.',
    variables: [
      { symbol: 'Phi', name: 'Magnetic flux', unit: 'Wb' },
      { symbol: 'B', name: 'Magnetic field strength', unit: 'T' },
      { symbol: 'A', name: 'Surface area', unit: 'm²' },
      { symbol: 'theta', name: 'Angle between field and surface normal', unit: '°' },
    ],
    keywords: ['magnetic flux', 'weber', 'magnetic field', 'induction'],
    solve: {
      Phi: (v) => v.B * v.A * Math.cos((v.theta * Math.PI) / 180),
      B: (v) => v.Phi / (v.A * Math.cos((v.theta * Math.PI) / 180)),
      A: (v) => v.Phi / (v.B * Math.cos((v.theta * Math.PI) / 180)),
      theta: (v) => {
        const ratio = v.Phi / (v.B * v.A);
        if (ratio < -1 || ratio > 1) throw new Error('Φ/(BA) must be between -1 and 1.');
        return Math.acos(ratio) * (180 / Math.PI);
      },
    },
  },
  {
    id: 'electromagnetic-induction',
    name: "Faraday's Law of Induction",
    category: 'Physics',
    subcategory: 'Magnetism',
    equation: 'ε = N(ΔΦ / Δt)',
    description: 'Calculates the magnitude of the EMF induced in a coil by a changing magnetic flux (the direction, given by the minus sign, follows from Lenz\'s law).',
    variables: [
      { symbol: 'emf', name: 'Induced EMF', unit: 'V' },
      { symbol: 'N', name: 'Number of coil turns', unit: 'dimensionless' },
      { symbol: 'dPhi', name: 'Change in magnetic flux', unit: 'Wb' },
      { symbol: 'dt', name: 'Time interval', unit: 's' },
    ],
    keywords: ['faraday', "faraday's law", 'electromagnetic induction', 'emf', 'flux', 'lenz'],
    solve: {
      emf: (v) => (v.N * v.dPhi) / v.dt,
      N: (v) => (v.emf * v.dt) / v.dPhi,
      dPhi: (v) => (v.emf * v.dt) / v.N,
      dt: (v) => (v.N * v.dPhi) / v.emf,
    },
  },
  {
    id: 'inductance',
    name: 'Inductance',
    category: 'Physics',
    subcategory: 'Magnetism',
    equation: 'L = NΦ / I',
    description: 'Calculates the self-inductance of a coil from its flux linkage and current.',
    variables: [
      { symbol: 'L', name: 'Inductance', unit: 'H' },
      { symbol: 'N', name: 'Number of coil turns', unit: 'dimensionless' },
      { symbol: 'Phi', name: 'Magnetic flux', unit: 'Wb' },
      { symbol: 'I', name: 'Current', unit: 'A' },
    ],
    keywords: ['inductance', 'inductor', 'magnetic flux', 'coil', 'henry'],
    solve: {
      L: (v) => (v.N * v.Phi) / v.I,
      N: (v) => (v.L * v.I) / v.Phi,
      Phi: (v) => (v.L * v.I) / v.N,
      I: (v) => (v.N * v.Phi) / v.L,
    },
  },
  {
    id: 'force-between-wires',
    name: 'Force Between Two Parallel Wires',
    category: 'Physics',
    subcategory: 'Magnetism',
    equation: 'F = μ₀I₁I₂L / (2πd)',
    description: 'Calculates the magnetic force between two long parallel current-carrying wires.',
    variables: [
      { symbol: 'F', name: 'Force', unit: 'N' },
      { symbol: 'mu0', name: 'Permeability of free space (≈4π×10⁻⁷)', unit: 'T·m/A' },
      { symbol: 'I1', name: 'Current in wire 1', unit: 'A' },
      { symbol: 'I2', name: 'Current in wire 2', unit: 'A' },
      { symbol: 'L', name: 'Length of wires', unit: 'm' },
      { symbol: 'd', name: 'Distance between wires', unit: 'm' },
    ],
    keywords: ['force between wires', 'parallel wires', 'magnetic force', 'ampere', 'current'],
    solve: {
      F: (v) => (v.mu0 * v.I1 * v.I2 * v.L) / (2 * Math.PI * v.d),
      mu0: (v) => (v.F * 2 * Math.PI * v.d) / (v.I1 * v.I2 * v.L),
      I1: (v) => (v.F * 2 * Math.PI * v.d) / (v.mu0 * v.I2 * v.L),
      I2: (v) => (v.F * 2 * Math.PI * v.d) / (v.mu0 * v.I1 * v.L),
      L: (v) => (v.F * 2 * Math.PI * v.d) / (v.mu0 * v.I1 * v.I2),
      d: (v) => (v.mu0 * v.I1 * v.I2 * v.L) / (2 * Math.PI * v.F),
    },
  },
  {
    id: 'solenoid-field',
    name: 'Magnetic Field Inside a Solenoid',
    category: 'Physics',
    subcategory: 'Magnetism',
    equation: 'B = μ₀nI',
    description: 'Calculates the magnetic field strength inside a long, tightly-wound solenoid.',
    variables: [
      { symbol: 'B', name: 'Magnetic field', unit: 'T' },
      { symbol: 'mu0', name: 'Permeability of free space (≈4π×10⁻⁷)', unit: 'T·m/A' },
      { symbol: 'n', name: 'Turns per unit length', unit: '1/m' },
      { symbol: 'I', name: 'Current', unit: 'A' },
    ],
    keywords: ['solenoid', 'magnetic field', 'coil', 'turns per length'],
    solve: {
      B: (v) => v.mu0 * v.n * v.I,
      mu0: (v) => v.B / (v.n * v.I),
      n: (v) => v.B / (v.mu0 * v.I),
      I: (v) => v.B / (v.mu0 * v.n),
    },
  },
];
