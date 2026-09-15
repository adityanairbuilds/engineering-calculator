import type { Formula } from '../../../types';

export const structuralFormulas: Formula[] = [
  {
    id: 'simply-supported-beam-deflection',
    name: 'Simply Supported Beam Deflection (Uniform Load)',
    category: 'Engineering',
    subcategory: 'Structural Engineering',
    equation: 'δ_max = 5wL⁴ / (384EI)',
    description: 'Calculates the maximum deflection of a simply supported beam under a uniformly distributed load.',
    variables: [
      { symbol: 'deltaMax', name: 'Maximum deflection', unit: 'm' },
      { symbol: 'w', name: 'Load per unit length', unit: 'N/m' },
      { symbol: 'L', name: 'Beam length', unit: 'm' },
      { symbol: 'E', name: "Young's modulus", unit: 'Pa' },
      { symbol: 'I', name: 'Second moment of area', unit: 'm⁴' },
    ],
    keywords: ['beam deflection', 'bending', 'simply supported beam', 'structural engineering', 'uniform load'],
    solve: {
      deltaMax: (v) => (5 * v.w * v.L ** 4) / (384 * v.E * v.I),
      w: (v) => (384 * v.E * v.I * v.deltaMax) / (5 * v.L ** 4),
      E: (v) => (5 * v.w * v.L ** 4) / (384 * v.I * v.deltaMax),
      I: (v) => (5 * v.w * v.L ** 4) / (384 * v.E * v.deltaMax),
      L: (v) => {
        const val = (384 * v.E * v.I * v.deltaMax) / (5 * v.w);
        if (val < 0) throw new Error('Beam length cannot be computed from a negative value under the fourth root.');
        return Math.pow(val, 0.25);
      },
    },
  },
  {
    id: 'cantilever-beam-deflection',
    name: 'Cantilever Beam Deflection (End Load)',
    category: 'Engineering',
    subcategory: 'Structural Engineering',
    equation: 'δ = PL³ / (3EI)',
    description: 'Calculates the deflection at the free end of a cantilever beam under a point load at that end.',
    variables: [
      { symbol: 'delta', name: 'Deflection', unit: 'm' },
      { symbol: 'P', name: 'Point load at free end', unit: 'N' },
      { symbol: 'L', name: 'Beam length', unit: 'm' },
      { symbol: 'E', name: "Young's modulus", unit: 'Pa' },
      { symbol: 'I', name: 'Second moment of area', unit: 'm⁴' },
    ],
    keywords: ['cantilever beam', 'beam deflection', 'bending', 'structural engineering', 'end load'],
    solve: {
      delta: (v) => (v.P * v.L ** 3) / (3 * v.E * v.I),
      P: (v) => (3 * v.E * v.I * v.delta) / v.L ** 3,
      E: (v) => (v.P * v.L ** 3) / (3 * v.I * v.delta),
      I: (v) => (v.P * v.L ** 3) / (3 * v.E * v.delta),
      L: (v) => {
        const val = (3 * v.E * v.I * v.delta) / v.P;
        if (val < 0) throw new Error('Beam length cannot be computed from a negative value under the cube root.');
        return Math.cbrt(val);
      },
    },
  },
  {
    id: 'bending-stress',
    name: 'Bending Stress',
    category: 'Engineering',
    subcategory: 'Structural Engineering',
    equation: 'σ = My / I',
    description: 'Calculates the bending (flexural) stress at a distance from the neutral axis of a beam under a bending moment.',
    variables: [
      { symbol: 'sigma', name: 'Bending stress', unit: 'Pa' },
      { symbol: 'M', name: 'Bending moment', unit: 'N·m' },
      { symbol: 'y', name: 'Distance from neutral axis', unit: 'm' },
      { symbol: 'I', name: 'Second moment of area', unit: 'm⁴' },
    ],
    keywords: ['bending stress', 'flexural stress', 'beam', 'structural engineering', 'neutral axis'],
    solve: {
      sigma: (v) => (v.M * v.y) / v.I,
      M: (v) => (v.sigma * v.I) / v.y,
      y: (v) => (v.sigma * v.I) / v.M,
      I: (v) => (v.M * v.y) / v.sigma,
    },
  },
  {
    id: 'euler-buckling-load',
    name: 'Euler Buckling Load',
    category: 'Engineering',
    subcategory: 'Structural Engineering',
    equation: 'P_cr = π²EI / (KL)²',
    description: 'Calculates the critical axial load at which a slender column buckles.',
    variables: [
      { symbol: 'Pcr', name: 'Critical buckling load', unit: 'N' },
      { symbol: 'E', name: "Young's modulus", unit: 'Pa' },
      { symbol: 'I', name: 'Second moment of area', unit: 'm⁴' },
      { symbol: 'K', name: 'Column effective length factor', unit: 'dimensionless' },
      { symbol: 'L', name: 'Column length', unit: 'm' },
    ],
    keywords: ['euler buckling', 'column buckling', 'critical load', 'structural engineering', 'columns'],
    solve: {
      Pcr: (v) => (Math.PI ** 2 * v.E * v.I) / (v.K * v.L) ** 2,
      E: (v) => (v.Pcr * (v.K * v.L) ** 2) / (Math.PI ** 2 * v.I),
      I: (v) => (v.Pcr * (v.K * v.L) ** 2) / (Math.PI ** 2 * v.E),
      L: (v) => {
        const val = (Math.PI ** 2 * v.E * v.I) / v.Pcr;
        if (val < 0) throw new Error('Cannot take the square root of a negative value for these inputs.');
        return Math.sqrt(val) / v.K;
      },
      K: (v) => {
        const val = (Math.PI ** 2 * v.E * v.I) / v.Pcr;
        if (val < 0) throw new Error('Cannot take the square root of a negative value for these inputs.');
        return Math.sqrt(val) / v.L;
      },
    },
  },
  {
    id: 'rectangular-moment-of-inertia',
    name: 'Second Moment of Area (Rectangular Section)',
    category: 'Engineering',
    subcategory: 'Structural Engineering',
    equation: 'I = bh³ / 12',
    description: 'Calculates the second moment of area of a rectangular cross-section about its centroidal axis.',
    variables: [
      { symbol: 'I', name: 'Second moment of area', unit: 'm⁴' },
      { symbol: 'b', name: 'Width', unit: 'm' },
      { symbol: 'h', name: 'Height (bending direction)', unit: 'm' },
    ],
    keywords: ['second moment of area', 'moment of inertia', 'rectangular section', 'structural engineering', 'section properties'],
    solve: {
      I: (v) => (v.b * v.h ** 3) / 12,
      b: (v) => (12 * v.I) / v.h ** 3,
      h: (v) => Math.cbrt((12 * v.I) / v.b),
    },
  },
  {
    id: 'factor-of-safety',
    name: 'Factor of Safety',
    category: 'Engineering',
    subcategory: 'Structural Engineering',
    equation: 'FS = σ_ultimate / σ_allowable',
    description: 'Calculates the factor of safety as the ratio of a material\'s ultimate stress to the allowable (working) stress.',
    variables: [
      { symbol: 'FS', name: 'Factor of safety', unit: 'dimensionless' },
      { symbol: 'sigmaUlt', name: 'Ultimate stress', unit: 'Pa' },
      { symbol: 'sigmaAllow', name: 'Allowable stress', unit: 'Pa' },
    ],
    keywords: ['factor of safety', 'safety factor', 'ultimate stress', 'allowable stress', 'structural engineering'],
    solve: {
      FS: (v) => v.sigmaUlt / v.sigmaAllow,
      sigmaUlt: (v) => v.FS * v.sigmaAllow,
      sigmaAllow: (v) => v.sigmaUlt / v.FS,
    },
  },
  {
    id: 'thin-wall-pressure-vessel-hoop-stress',
    name: 'Thin-Wall Pressure Vessel Hoop Stress',
    category: 'Engineering',
    subcategory: 'Structural Engineering',
    equation: 'σ_hoop = pr / t',
    description: 'Calculates the circumferential (hoop) stress in a thin-walled cylindrical pressure vessel.',
    variables: [
      { symbol: 'sigmaHoop', name: 'Hoop stress', unit: 'Pa' },
      { symbol: 'p', name: 'Internal pressure', unit: 'Pa' },
      { symbol: 'r', name: 'Inner radius', unit: 'm' },
      { symbol: 't', name: 'Wall thickness', unit: 'm' },
    ],
    keywords: ['hoop stress', 'pressure vessel', 'thin wall', 'structural engineering', 'circumferential stress'],
    solve: {
      sigmaHoop: (v) => (v.p * v.r) / v.t,
      p: (v) => (v.sigmaHoop * v.t) / v.r,
      r: (v) => (v.sigmaHoop * v.t) / v.p,
      t: (v) => (v.p * v.r) / v.sigmaHoop,
    },
  },
  {
    id: 'thin-wall-pressure-vessel-longitudinal-stress',
    name: 'Thin-Wall Pressure Vessel Longitudinal Stress',
    category: 'Engineering',
    subcategory: 'Structural Engineering',
    equation: 'σ_long = pr / (2t)',
    description: 'Calculates the longitudinal (axial) stress in a thin-walled cylindrical pressure vessel.',
    variables: [
      { symbol: 'sigmaLong', name: 'Longitudinal stress', unit: 'Pa' },
      { symbol: 'p', name: 'Internal pressure', unit: 'Pa' },
      { symbol: 'r', name: 'Inner radius', unit: 'm' },
      { symbol: 't', name: 'Wall thickness', unit: 'm' },
    ],
    keywords: ['longitudinal stress', 'pressure vessel', 'thin wall', 'structural engineering', 'axial stress'],
    solve: {
      sigmaLong: (v) => (v.p * v.r) / (2 * v.t),
      p: (v) => (2 * v.sigmaLong * v.t) / v.r,
      r: (v) => (2 * v.sigmaLong * v.t) / v.p,
      t: (v) => (v.p * v.r) / (2 * v.sigmaLong),
    },
  },
  {
    id: 'average-shear-stress',
    name: 'Average (Direct) Shear Stress',
    category: 'Engineering',
    subcategory: 'Structural Engineering',
    equation: 'τ = V / A',
    description: 'Calculates the average shear stress on a cross-section from the applied shear force and its area.',
    variables: [
      { symbol: 'tau', name: 'Average shear stress', unit: 'Pa' },
      { symbol: 'V', name: 'Shear force', unit: 'N' },
      { symbol: 'A', name: 'Cross-sectional area', unit: 'm²' },
    ],
    keywords: ['shear stress', 'direct shear', 'structural engineering', 'shear force'],
    solve: {
      tau: (v) => v.V / v.A,
      V: (v) => v.tau * v.A,
      A: (v) => v.V / v.tau,
    },
  },
];
