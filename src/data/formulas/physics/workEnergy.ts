import type { Formula } from '../../../types';

export const workEnergyFormulas: Formula[] = [
  {
    id: 'work',
    name: 'Work',
    category: 'Physics',
    subcategory: 'Work and Energy',
    equation: 'W = Fd cos(θ)',
    description: 'Calculates the work done by a constant force applied at an angle to the displacement.',
    variables: [
      { symbol: 'W', name: 'Work', unit: 'J' },
      { symbol: 'F', name: 'Force', unit: 'N' },
      { symbol: 'd', name: 'Displacement', unit: 'm' },
      { symbol: 'theta', name: 'Angle between force and displacement', unit: '°' },
    ],
    keywords: ['work', 'energy', 'force', 'displacement', 'physics'],
    solve: {
      W: (v) => v.F * v.d * Math.cos((v.theta * Math.PI) / 180),
      F: (v) => v.W / (v.d * Math.cos((v.theta * Math.PI) / 180)),
      d: (v) => v.W / (v.F * Math.cos((v.theta * Math.PI) / 180)),
      theta: (v) => {
        const ratio = v.W / (v.F * v.d);
        if (ratio < -1 || ratio > 1) throw new Error('W/(Fd) must be between -1 and 1.');
        return Math.acos(ratio) * (180 / Math.PI);
      },
    },
  },
  {
    id: 'kinetic-energy',
    name: 'Kinetic Energy',
    category: 'Physics',
    subcategory: 'Work and Energy',
    equation: 'KE = ½mv²',
    description: 'Calculates the kinetic energy of a moving object from its mass and speed.',
    variables: [
      { symbol: 'KE', name: 'Kinetic energy', unit: 'J' },
      { symbol: 'm', name: 'Mass', unit: 'kg' },
      { symbol: 'v', name: 'Velocity', unit: 'm/s' },
    ],
    keywords: ['kinetic energy', 'energy', 'motion', 'velocity', 'mass', 'speed'],
    solve: {
      KE: (v) => 0.5 * v.m * v.v ** 2,
      m: (v) => (2 * v.KE) / v.v ** 2,
      v: (v) => {
        const sq = (2 * v.KE) / v.m;
        if (sq < 0) throw new Error('2·KE/m is negative — no real velocity.');
        return Math.sqrt(sq);
      },
    },
  },
  {
    id: 'potential-energy',
    name: 'Gravitational Potential Energy',
    category: 'Physics',
    subcategory: 'Work and Energy',
    equation: 'PE = mgh',
    description: 'Calculates gravitational potential energy near a planet\'s surface from mass, gravity, and height.',
    variables: [
      { symbol: 'PE', name: 'Potential energy', unit: 'J' },
      { symbol: 'm', name: 'Mass', unit: 'kg' },
      { symbol: 'g', name: 'Gravitational acceleration', unit: 'm/s²' },
      { symbol: 'h', name: 'Height', unit: 'm' },
    ],
    keywords: ['potential energy', 'energy', 'gravity', 'height', 'mass'],
    solve: {
      PE: (v) => v.m * v.g * v.h,
      m: (v) => v.PE / (v.g * v.h),
      g: (v) => v.PE / (v.m * v.h),
      h: (v) => v.PE / (v.m * v.g),
    },
  },
  {
    id: 'elastic-potential-energy',
    name: 'Elastic Potential Energy',
    category: 'Physics',
    subcategory: 'Work and Energy',
    equation: 'PE = ½kx²',
    description: 'Calculates the energy stored in a stretched or compressed spring.',
    variables: [
      { symbol: 'PE', name: 'Elastic potential energy', unit: 'J' },
      { symbol: 'k', name: 'Spring constant', unit: 'N/m' },
      { symbol: 'x', name: 'Displacement from equilibrium', unit: 'm' },
    ],
    keywords: ['elastic potential energy', 'spring energy', 'hooke', 'spring constant', 'energy'],
    solve: {
      PE: (v) => 0.5 * v.k * v.x ** 2,
      k: (v) => (2 * v.PE) / v.x ** 2,
      x: (v) => {
        const sq = (2 * v.PE) / v.k;
        if (sq < 0) throw new Error('2·PE/k is negative — no real displacement.');
        return Math.sqrt(sq);
      },
    },
  },
  {
    id: 'power',
    name: 'Power (Work / Time)',
    category: 'Physics',
    subcategory: 'Work and Energy',
    equation: 'P = W / t',
    description: 'Calculates power as the rate at which work is done.',
    variables: [
      { symbol: 'P', name: 'Power', unit: 'W' },
      { symbol: 'W', name: 'Work', unit: 'J' },
      { symbol: 't', name: 'Time', unit: 's' },
    ],
    keywords: ['power', 'energy', 'work', 'time', 'watts'],
    solve: {
      P: (v) => v.W / v.t,
      W: (v) => v.P * v.t,
      t: (v) => v.W / v.P,
    },
  },
  {
    id: 'power-force-velocity',
    name: 'Power (Force & Velocity)',
    category: 'Physics',
    subcategory: 'Work and Energy',
    equation: 'P = Fv',
    description: 'Calculates the instantaneous power delivered by a force acting on an object moving at a given velocity.',
    variables: [
      { symbol: 'P', name: 'Power', unit: 'W' },
      { symbol: 'F', name: 'Force', unit: 'N' },
      { symbol: 'v', name: 'Velocity', unit: 'm/s' },
    ],
    keywords: ['power', 'force', 'velocity', 'watts', 'instantaneous power'],
    solve: {
      P: (v) => v.F * v.v,
      F: (v) => v.P / v.v,
      v: (v) => v.P / v.F,
    },
  },
  {
    id: 'efficiency',
    name: 'Efficiency',
    category: 'Physics',
    subcategory: 'Work and Energy',
    equation: 'η = (E_out / E_in) × 100%',
    description: 'Calculates the efficiency of a machine or process as a percentage of useful energy output over total energy input.',
    variables: [
      { symbol: 'eta', name: 'Efficiency', unit: '%' },
      { symbol: 'Eout', name: 'Useful energy output', unit: 'J' },
      { symbol: 'Ein', name: 'Total energy input', unit: 'J' },
    ],
    keywords: ['efficiency', 'energy', 'power', 'output', 'input', 'percentage'],
    solve: {
      eta: (v) => (v.Eout / v.Ein) * 100,
      Eout: (v) => (v.eta / 100) * v.Ein,
      Ein: (v) => v.Eout / (v.eta / 100),
    },
  },
];
