import type { Formula } from '../../../types';

export const mechanicsFormulas: Formula[] = [
  {
    id: 'stress',
    name: 'Stress',
    category: 'Engineering',
    subcategory: 'Mechanics',
    equation: 'σ = F / A',
    description: 'Calculates mechanical (normal) stress from applied force and cross-sectional area.',
    variables: [
      { symbol: 'sigma', name: 'Stress', unit: 'Pa' },
      { symbol: 'F', name: 'Applied force', unit: 'N' },
      { symbol: 'A', name: 'Cross-sectional area', unit: 'm²' },
    ],
    keywords: ['stress', 'mechanics', 'force', 'engineering', 'normal stress'],
    solve: {
      sigma: (v) => v.F / v.A,
      F: (v) => v.sigma * v.A,
      A: (v) => v.F / v.sigma,
    },
  },
  {
    id: 'strain',
    name: 'Strain',
    category: 'Engineering',
    subcategory: 'Mechanics',
    equation: 'ε = ΔL / L₀',
    description: 'Calculates engineering strain from the change in length relative to original length.',
    variables: [
      { symbol: 'epsilon', name: 'Strain', unit: 'dimensionless' },
      { symbol: 'deltaL', name: 'Change in length', unit: 'm' },
      { symbol: 'L0', name: 'Original length', unit: 'm' },
    ],
    keywords: ['strain', 'deformation', 'mechanics', 'engineering', 'elongation'],
    solve: {
      epsilon: (v) => v.deltaL / v.L0,
      deltaL: (v) => v.epsilon * v.L0,
      L0: (v) => v.deltaL / v.epsilon,
    },
  },
  {
    id: 'youngs-modulus',
    name: "Young's Modulus",
    category: 'Engineering',
    subcategory: 'Mechanics',
    equation: 'E = σ / ε',
    description: "Calculates the modulus of elasticity from stress and strain in the linear-elastic range.",
    variables: [
      { symbol: 'E', name: "Young's modulus", unit: 'Pa' },
      { symbol: 'sigma', name: 'Stress', unit: 'Pa' },
      { symbol: 'epsilon', name: 'Strain', unit: 'dimensionless' },
    ],
    keywords: ["young's modulus", 'elasticity', 'stress', 'strain', 'mechanics', 'elastic modulus'],
    solve: {
      E: (v) => v.sigma / v.epsilon,
      sigma: (v) => v.E * v.epsilon,
      epsilon: (v) => v.sigma / v.E,
    },
  },
  {
    id: 'moment-inertia-cylinder',
    name: 'Moment of Inertia (Solid Cylinder)',
    category: 'Engineering',
    subcategory: 'Mechanics',
    equation: 'I = ½mr²',
    description: 'Mass moment of inertia of a solid cylinder about its central longitudinal axis.',
    variables: [
      { symbol: 'I', name: 'Moment of inertia', unit: 'kg·m²' },
      { symbol: 'm', name: 'Mass', unit: 'kg' },
      { symbol: 'r', name: 'Radius', unit: 'm' },
    ],
    keywords: ['moment of inertia', 'cylinder', 'rotational', 'mechanics', 'engineering'],
    solve: {
      I: (v) => 0.5 * v.m * v.r ** 2,
      m: (v) => (2 * v.I) / v.r ** 2,
      r: (v) => {
        const val = (2 * v.I) / v.m;
        if (val < 0) throw new Error('Radius squared cannot be negative for these inputs.');
        return Math.sqrt(val);
      },
    },
  },
  {
    id: 'moment-inertia-sphere',
    name: 'Moment of Inertia (Solid Sphere)',
    category: 'Engineering',
    subcategory: 'Mechanics',
    equation: 'I = (2/5)mr²',
    description: 'Mass moment of inertia of a solid sphere about an axis through its center.',
    variables: [
      { symbol: 'I', name: 'Moment of inertia', unit: 'kg·m²' },
      { symbol: 'm', name: 'Mass', unit: 'kg' },
      { symbol: 'r', name: 'Radius', unit: 'm' },
    ],
    keywords: ['moment of inertia', 'sphere', 'rotational', 'mechanics', 'engineering'],
    solve: {
      I: (v) => (2 / 5) * v.m * v.r ** 2,
      m: (v) => v.I / ((2 / 5) * v.r ** 2),
      r: (v) => {
        const val = v.I / ((2 / 5) * v.m);
        if (val < 0) throw new Error('Radius squared cannot be negative for these inputs.');
        return Math.sqrt(val);
      },
    },
  },
  {
    id: 'moment-inertia-rod-center',
    name: 'Moment of Inertia (Slender Rod, Center)',
    category: 'Engineering',
    subcategory: 'Mechanics',
    equation: 'I = (1/12)mL²',
    description: 'Mass moment of inertia of a slender rod about an axis through its center, perpendicular to its length.',
    variables: [
      { symbol: 'I', name: 'Moment of inertia', unit: 'kg·m²' },
      { symbol: 'm', name: 'Mass', unit: 'kg' },
      { symbol: 'L', name: 'Rod length', unit: 'm' },
    ],
    keywords: ['moment of inertia', 'rod', 'rotational', 'mechanics', 'engineering'],
    solve: {
      I: (v) => (1 / 12) * v.m * v.L ** 2,
      m: (v) => v.I / ((1 / 12) * v.L ** 2),
      L: (v) => {
        const val = v.I / ((1 / 12) * v.m);
        if (val < 0) throw new Error('Length squared cannot be negative for these inputs.');
        return Math.sqrt(val);
      },
    },
  },
  {
    id: 'parallel-axis-theorem',
    name: 'Parallel Axis Theorem',
    category: 'Engineering',
    subcategory: 'Mechanics',
    equation: 'I = I_cm + md²',
    description: 'Relates the moment of inertia about any axis to the moment of inertia about a parallel axis through the center of mass.',
    variables: [
      { symbol: 'I', name: 'Moment of inertia about new axis', unit: 'kg·m²' },
      { symbol: 'Icm', name: 'Moment of inertia about center of mass', unit: 'kg·m²' },
      { symbol: 'm', name: 'Mass', unit: 'kg' },
      { symbol: 'd', name: 'Distance between axes', unit: 'm' },
    ],
    keywords: ['parallel axis theorem', 'moment of inertia', 'mechanics', 'engineering'],
    solve: {
      I: (v) => v.Icm + v.m * v.d ** 2,
      Icm: (v) => v.I - v.m * v.d ** 2,
      m: (v) => (v.I - v.Icm) / v.d ** 2,
      d: (v) => {
        const val = (v.I - v.Icm) / v.m;
        if (val < 0) throw new Error('Distance squared cannot be negative for these inputs.');
        return Math.sqrt(val);
      },
    },
  },
  {
    id: 'mechanical-advantage-lever',
    name: 'Mechanical Advantage (Lever)',
    category: 'Engineering',
    subcategory: 'Mechanics',
    equation: 'MA = F_out / F_in',
    description: 'Calculates the mechanical advantage of a lever from output and input forces.',
    variables: [
      { symbol: 'MA', name: 'Mechanical advantage', unit: 'dimensionless' },
      { symbol: 'Fout', name: 'Output force', unit: 'N' },
      { symbol: 'Fin', name: 'Input force', unit: 'N' },
    ],
    keywords: ['mechanical advantage', 'lever', 'simple machines', 'engineering'],
    solve: {
      MA: (v) => v.Fout / v.Fin,
      Fout: (v) => v.MA * v.Fin,
      Fin: (v) => v.Fout / v.MA,
    },
  },
];
