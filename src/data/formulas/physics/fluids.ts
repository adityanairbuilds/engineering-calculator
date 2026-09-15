import type { Formula } from '../../../types';

export const fluidsFormulas: Formula[] = [
  {
    id: 'pressure',
    name: 'Pressure',
    category: 'Physics',
    subcategory: 'Fluids',
    equation: 'P = F / A',
    description: 'Calculates pressure from a force distributed over an area.',
    variables: [
      { symbol: 'P', name: 'Pressure', unit: 'Pa' },
      { symbol: 'F', name: 'Force', unit: 'N' },
      { symbol: 'A', name: 'Area', unit: 'm²' },
    ],
    keywords: ['pressure', 'force', 'area', 'fluid', 'pascal'],
    solve: {
      P: (v) => v.F / v.A,
      F: (v) => v.P * v.A,
      A: (v) => v.F / v.P,
    },
  },
  {
    id: 'hydrostatic-pressure',
    name: 'Hydrostatic Pressure',
    category: 'Physics',
    subcategory: 'Fluids',
    equation: 'P = P₀ + ρgh',
    description: 'Calculates the pressure at a depth in a fluid, including the pressure at the surface.',
    variables: [
      { symbol: 'P', name: 'Pressure at depth', unit: 'Pa' },
      { symbol: 'P0', name: 'Surface pressure', unit: 'Pa' },
      { symbol: 'rho', name: 'Fluid density', unit: 'kg/m³' },
      { symbol: 'g', name: 'Gravitational acceleration', unit: 'm/s²' },
      { symbol: 'h', name: 'Depth', unit: 'm' },
    ],
    keywords: ['pressure', 'depth', 'fluid', 'density', 'hydrostatic'],
    solve: {
      P: (v) => v.P0 + v.rho * v.g * v.h,
      P0: (v) => v.P - v.rho * v.g * v.h,
      rho: (v) => (v.P - v.P0) / (v.g * v.h),
      g: (v) => (v.P - v.P0) / (v.rho * v.h),
      h: (v) => (v.P - v.P0) / (v.rho * v.g),
    },
  },
  {
    id: 'bernoullis-principle',
    name: "Bernoulli's Equation",
    category: 'Physics',
    subcategory: 'Fluids',
    equation: 'P₁ + ½ρv₁² + ρgh₁ = P₂ + ½ρv₂² + ρgh₂',
    description: 'Relates pressure, speed, and height between two points along a streamline in an ideal fluid.',
    variables: [
      { symbol: 'P1', name: 'Pressure at point 1', unit: 'Pa' },
      { symbol: 'P2', name: 'Pressure at point 2', unit: 'Pa' },
      { symbol: 'rho', name: 'Fluid density', unit: 'kg/m³' },
      { symbol: 'v1', name: 'Velocity at point 1', unit: 'm/s' },
      { symbol: 'v2', name: 'Velocity at point 2', unit: 'm/s' },
      { symbol: 'g', name: 'Gravitational acceleration', unit: 'm/s²' },
      { symbol: 'h1', name: 'Height of point 1', unit: 'm' },
      { symbol: 'h2', name: 'Height of point 2', unit: 'm' },
    ],
    keywords: ['bernoulli', "bernoulli's principle", 'pressure', 'velocity', 'fluid', 'flow', 'venturi'],
    solve: {
      P1: (v) => v.P2 + 0.5 * v.rho * v.v2 ** 2 + v.rho * v.g * v.h2 - 0.5 * v.rho * v.v1 ** 2 - v.rho * v.g * v.h1,
      P2: (v) => v.P1 + 0.5 * v.rho * v.v1 ** 2 + v.rho * v.g * v.h1 - 0.5 * v.rho * v.v2 ** 2 - v.rho * v.g * v.h2,
      v1: (v) => {
        const sq = (2 * (v.P2 - v.P1)) / v.rho + v.v2 ** 2 + 2 * v.g * (v.h2 - v.h1);
        if (sq < 0) throw new Error('No real velocity v₁ for these values.');
        return Math.sqrt(sq);
      },
      v2: (v) => {
        const sq = (2 * (v.P1 - v.P2)) / v.rho + v.v1 ** 2 + 2 * v.g * (v.h1 - v.h2);
        if (sq < 0) throw new Error('No real velocity v₂ for these values.');
        return Math.sqrt(sq);
      },
      h1: (v) => v.h2 + (v.P2 - v.P1 + 0.5 * v.rho * (v.v2 ** 2 - v.v1 ** 2)) / (v.rho * v.g),
      h2: (v) => v.h1 + (v.P1 - v.P2 + 0.5 * v.rho * (v.v1 ** 2 - v.v2 ** 2)) / (v.rho * v.g),
      rho: (v) => (v.P1 - v.P2) / (0.5 * (v.v2 ** 2 - v.v1 ** 2) + v.g * (v.h2 - v.h1)),
      g: (v) => (v.P1 - v.P2 - 0.5 * v.rho * (v.v2 ** 2 - v.v1 ** 2)) / (v.rho * (v.h2 - v.h1)),
    },
  },
  {
    id: 'continuity-equation',
    name: 'Continuity Equation',
    category: 'Physics',
    subcategory: 'Fluids',
    equation: 'A₁v₁ = A₂v₂',
    description: 'Relates flow speed across two cross-sections of a pipe for an incompressible fluid.',
    variables: [
      { symbol: 'A1', name: 'Cross-sectional area 1', unit: 'm²' },
      { symbol: 'v1', name: 'Velocity 1', unit: 'm/s' },
      { symbol: 'A2', name: 'Cross-sectional area 2', unit: 'm²' },
      { symbol: 'v2', name: 'Velocity 2', unit: 'm/s' },
    ],
    keywords: ['continuity', 'continuity equation', 'flow rate', 'fluid', 'velocity', 'area'],
    solve: {
      A1: (v) => (v.A2 * v.v2) / v.v1,
      v1: (v) => (v.A2 * v.v2) / v.A1,
      A2: (v) => (v.A1 * v.v1) / v.v2,
      v2: (v) => (v.A1 * v.v1) / v.A2,
    },
  },
  {
    id: 'buoyant-force',
    name: 'Buoyant Force',
    category: 'Physics',
    subcategory: 'Fluids',
    equation: 'F_b = ρVg',
    description: "Calculates the upward buoyant force on a submerged object from Archimedes' principle.",
    variables: [
      { symbol: 'Fb', name: 'Buoyant force', unit: 'N' },
      { symbol: 'rho', name: 'Fluid density', unit: 'kg/m³' },
      { symbol: 'V', name: 'Volume displaced', unit: 'm³' },
      { symbol: 'g', name: 'Gravitational acceleration', unit: 'm/s²' },
    ],
    keywords: ['buoyant force', 'buoyancy', 'archimedes', 'fluid', 'floating'],
    solve: {
      Fb: (v) => v.rho * v.V * v.g,
      rho: (v) => v.Fb / (v.V * v.g),
      V: (v) => v.Fb / (v.rho * v.g),
      g: (v) => v.Fb / (v.rho * v.V),
    },
  },
  {
    id: 'stokes-law',
    name: "Stokes' Law",
    category: 'Physics',
    subcategory: 'Fluids',
    equation: 'F_drag = 6πηrv',
    description: 'Calculates the viscous drag force on a small sphere moving slowly through a fluid.',
    variables: [
      { symbol: 'Fdrag', name: 'Drag force', unit: 'N' },
      { symbol: 'eta', name: 'Fluid viscosity', unit: 'Pa·s' },
      { symbol: 'r', name: 'Sphere radius', unit: 'm' },
      { symbol: 'v', name: 'Velocity', unit: 'm/s' },
    ],
    keywords: ['stokes law', 'drag', 'viscosity', 'fluid', 'terminal velocity', 'resistance'],
    solve: {
      Fdrag: (v) => 6 * Math.PI * v.eta * v.r * v.v,
      eta: (v) => v.Fdrag / (6 * Math.PI * v.r * v.v),
      r: (v) => v.Fdrag / (6 * Math.PI * v.eta * v.v),
      v: (v) => v.Fdrag / (6 * Math.PI * v.eta * v.r),
    },
  },
  {
    id: 'dynamic-pressure',
    name: 'Dynamic Pressure',
    category: 'Physics',
    subcategory: 'Fluids',
    equation: 'q = ½ρv²',
    description: 'Calculates the dynamic pressure of a moving fluid, the kinetic-energy-per-volume term used in Bernoulli\'s equation and aerodynamics.',
    variables: [
      { symbol: 'q', name: 'Dynamic pressure', unit: 'Pa' },
      { symbol: 'rho', name: 'Fluid density', unit: 'kg/m³' },
      { symbol: 'v', name: 'Flow velocity', unit: 'm/s' },
    ],
    keywords: ['dynamic pressure', 'fluid', 'aerodynamics', 'velocity', 'bernoulli'],
    solve: {
      q: (v) => 0.5 * v.rho * v.v ** 2,
      rho: (v) => (2 * v.q) / v.v ** 2,
      v: (v) => {
        const sq = (2 * v.q) / v.rho;
        if (sq < 0) throw new Error('2q/ρ is negative — no real velocity.');
        return Math.sqrt(sq);
      },
    },
  },
  {
    id: 'pascals-principle',
    name: "Pascal's Principle",
    category: 'Physics',
    subcategory: 'Fluids',
    equation: 'F₁ / A₁ = F₂ / A₂',
    description: 'Relates force and piston area in a hydraulic system, where pressure applied at one point is transmitted equally throughout the fluid.',
    variables: [
      { symbol: 'F1', name: 'Force on piston 1', unit: 'N' },
      { symbol: 'A1', name: 'Area of piston 1', unit: 'm²' },
      { symbol: 'F2', name: 'Force on piston 2', unit: 'N' },
      { symbol: 'A2', name: 'Area of piston 2', unit: 'm²' },
    ],
    keywords: ['pascal', "pascal's principle", 'hydraulic', 'hydraulic press', 'fluid', 'piston'],
    solve: {
      F1: (v) => (v.A1 * v.F2) / v.A2,
      A1: (v) => (v.F1 * v.A2) / v.F2,
      F2: (v) => (v.A2 * v.F1) / v.A1,
      A2: (v) => (v.F2 * v.A1) / v.F1,
    },
  },
  {
    id: 'volume-flow-rate',
    name: 'Volume Flow Rate',
    category: 'Physics',
    subcategory: 'Fluids',
    equation: 'Q = Av',
    description: 'Calculates the volume of fluid passing through a cross-section per unit time.',
    variables: [
      { symbol: 'Q', name: 'Volume flow rate', unit: 'm³/s' },
      { symbol: 'A', name: 'Cross-sectional area', unit: 'm²' },
      { symbol: 'v', name: 'Flow velocity', unit: 'm/s' },
    ],
    keywords: ['flow rate', 'volume flow rate', 'fluid', 'discharge', 'pipe flow'],
    solve: {
      Q: (v) => v.A * v.v,
      A: (v) => v.Q / v.v,
      v: (v) => v.Q / v.A,
    },
  },
];
