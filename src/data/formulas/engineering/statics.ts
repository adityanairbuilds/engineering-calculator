import type { Formula } from '../../../types';

export const staticsFormulas: Formula[] = [
  {
    id: 'equilibrium-force',
    name: 'Force Equilibrium',
    category: 'Engineering',
    subcategory: 'Statics',
    equation: 'ΣF = 0',
    description: 'The net force on a body in static equilibrium is zero. Reference relation — sum each force component by hand.',
    variables: [{ symbol: 'sumF', name: 'Sum of all forces', unit: 'N' }],
    keywords: ['equilibrium', 'statics', 'force', 'net force', 'engineering', 'sum of forces'],
    solve: {},
  },
  {
    id: 'equilibrium-torque',
    name: 'Torque (Moment) Equilibrium',
    category: 'Engineering',
    subcategory: 'Statics',
    equation: 'ΣM = 0',
    description: 'The net moment on a body in static equilibrium is zero. Reference relation — sum each moment by hand.',
    variables: [{ symbol: 'sumM', name: 'Sum of all moments', unit: 'N·m' }],
    keywords: ['equilibrium', 'statics', 'torque', 'moment', 'rotational', 'engineering'],
    solve: {},
  },
  {
    id: 'center-of-mass-two-point',
    name: 'Center of Mass (Two Point Masses)',
    category: 'Engineering',
    subcategory: 'Statics',
    equation: 'x_cm = (m₁x₁ + m₂x₂) / (m₁ + m₂)',
    description: 'Calculates the center of mass position for a system of two point masses.',
    variables: [
      { symbol: 'xcm', name: 'Center of mass position', unit: 'm' },
      { symbol: 'm1', name: 'Mass 1', unit: 'kg' },
      { symbol: 'x1', name: 'Position of mass 1', unit: 'm' },
      { symbol: 'm2', name: 'Mass 2', unit: 'kg' },
      { symbol: 'x2', name: 'Position of mass 2', unit: 'm' },
    ],
    keywords: ['center of mass', 'centroid', 'statics', 'equilibrium', 'center of gravity'],
    solve: {
      xcm: (v) => (v.m1 * v.x1 + v.m2 * v.x2) / (v.m1 + v.m2),
      m1: (v) => {
        if (v.xcm === v.x1) throw new Error('x_cm cannot equal x1 when solving for m1.');
        return (v.m2 * (v.x2 - v.xcm)) / (v.xcm - v.x1);
      },
      m2: (v) => {
        if (v.xcm === v.x2) throw new Error('x_cm cannot equal x2 when solving for m2.');
        return (v.m1 * (v.x1 - v.xcm)) / (v.xcm - v.x2);
      },
      x1: (v) => {
        if (v.m1 === 0) throw new Error('m1 cannot be zero when solving for x1.');
        return (v.xcm * (v.m1 + v.m2) - v.m2 * v.x2) / v.m1;
      },
      x2: (v) => {
        if (v.m2 === 0) throw new Error('m2 cannot be zero when solving for x2.');
        return (v.xcm * (v.m1 + v.m2) - v.m1 * v.x1) / v.m2;
      },
    },
  },
  {
    id: 'moment-of-force',
    name: 'Moment of a Force',
    category: 'Engineering',
    subcategory: 'Statics',
    equation: 'M = Fd',
    description: 'Calculates the moment (turning effect) of a force about a point from the force and its perpendicular distance.',
    variables: [
      { symbol: 'M', name: 'Moment', unit: 'N·m' },
      { symbol: 'F', name: 'Force', unit: 'N' },
      { symbol: 'd', name: 'Perpendicular distance to point', unit: 'm' },
    ],
    keywords: ['moment', 'force', 'statics', 'torque', 'lever arm'],
    solve: {
      M: (v) => v.F * v.d,
      F: (v) => v.M / v.d,
      d: (v) => v.M / v.F,
    },
  },
  {
    id: 'static-friction-force',
    name: 'Maximum Static Friction Force',
    category: 'Engineering',
    subcategory: 'Statics',
    equation: 'f = μN',
    description: 'Calculates the maximum static friction force from the coefficient of static friction and the normal force.',
    variables: [
      { symbol: 'f', name: 'Friction force', unit: 'N' },
      { symbol: 'mu', name: 'Coefficient of static friction', unit: 'dimensionless' },
      { symbol: 'N', name: 'Normal force', unit: 'N' },
    ],
    keywords: ['friction', 'static friction', 'coefficient of friction', 'statics', 'normal force'],
    solve: {
      f: (v) => v.mu * v.N,
      mu: (v) => v.f / v.N,
      N: (v) => v.f / v.mu,
    },
  },
  {
    id: 'friction-angle',
    name: 'Angle of Friction',
    category: 'Engineering',
    subcategory: 'Statics',
    equation: 'φ = tan⁻¹(μ)',
    description: 'Calculates the friction angle at which a body just begins to slide, from the coefficient of friction.',
    variables: [
      { symbol: 'phi', name: 'Friction angle', unit: '°' },
      { symbol: 'mu', name: 'Coefficient of friction', unit: 'dimensionless' },
    ],
    keywords: ['friction angle', 'angle of repose', 'coefficient of friction', 'statics'],
    solve: {
      phi: (v) => (Math.atan(v.mu) * 180) / Math.PI,
      mu: (v) => Math.tan((v.phi * Math.PI) / 180),
    },
  },
  {
    id: 'resultant-force-two-perpendicular',
    name: 'Resultant of Two Perpendicular Forces',
    category: 'Engineering',
    subcategory: 'Statics',
    equation: 'R = √(Fx² + Fy²), θ = tan⁻¹(Fy/Fx)',
    description: 'Calculates the magnitude and direction of the resultant of two perpendicular force components.',
    variables: [
      { symbol: 'R', name: 'Resultant force magnitude', unit: 'N' },
      { symbol: 'Fx', name: 'Force component (x)', unit: 'N' },
      { symbol: 'Fy', name: 'Force component (y)', unit: 'N' },
      { symbol: 'theta', name: 'Direction of resultant', unit: '°' },
    ],
    keywords: ['resultant force', 'force components', 'statics', 'vector addition', 'resultant'],
    solve: {
      R: (v) => Math.sqrt(v.Fx ** 2 + v.Fy ** 2),
      theta: (v) => (Math.atan2(v.Fy, v.Fx) * 180) / Math.PI,
      Fx: (v) => v.R * Math.cos((v.theta * Math.PI) / 180),
      Fy: (v) => v.R * Math.sin((v.theta * Math.PI) / 180),
    },
  },
  {
    id: 'simply-supported-beam-reaction-left',
    name: 'Simply Supported Beam Reaction — Left Support',
    category: 'Engineering',
    subcategory: 'Statics',
    equation: 'R₁ = Pb / (a + b)',
    description: 'Calculates the reaction at the left support of a simply supported beam carrying a single point load.',
    variables: [
      { symbol: 'R1', name: 'Reaction at left support', unit: 'N' },
      { symbol: 'P', name: 'Point load', unit: 'N' },
      { symbol: 'a', name: 'Distance from left support to load', unit: 'm' },
      { symbol: 'b', name: 'Distance from load to right support', unit: 'm' },
    ],
    keywords: ['beam reactions', 'simply supported beam', 'statics', 'point load', 'support reactions'],
    solve: {
      R1: (v) => (v.P * v.b) / (v.a + v.b),
      P: (v) => (v.R1 * (v.a + v.b)) / v.b,
      a: (v) => (v.P * v.b) / v.R1 - v.b,
      b: (v) => {
        if (v.P === v.R1) throw new Error('P cannot equal R1 when solving for b.');
        return (v.R1 * v.a) / (v.P - v.R1);
      },
    },
  },
  {
    id: 'simply-supported-beam-reaction-right',
    name: 'Simply Supported Beam Reaction — Right Support',
    category: 'Engineering',
    subcategory: 'Statics',
    equation: 'R₂ = Pa / (a + b)',
    description: 'Calculates the reaction at the right support of a simply supported beam carrying a single point load.',
    variables: [
      { symbol: 'R2', name: 'Reaction at right support', unit: 'N' },
      { symbol: 'P', name: 'Point load', unit: 'N' },
      { symbol: 'a', name: 'Distance from left support to load', unit: 'm' },
      { symbol: 'b', name: 'Distance from load to right support', unit: 'm' },
    ],
    keywords: ['beam reactions', 'simply supported beam', 'statics', 'point load', 'support reactions'],
    solve: {
      R2: (v) => (v.P * v.a) / (v.a + v.b),
      P: (v) => (v.R2 * (v.a + v.b)) / v.a,
      b: (v) => (v.P * v.a) / v.R2 - v.a,
      a: (v) => {
        if (v.P === v.R2) throw new Error('P cannot equal R2 when solving for a.');
        return (v.R2 * v.b) / (v.P - v.R2);
      },
    },
  },
];
