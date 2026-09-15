import type { Formula } from '../../../types';

export const kinematicsFormulas: Formula[] = [
  {
    id: 'velocity',
    name: 'Velocity',
    category: 'Physics',
    subcategory: 'Kinematics',
    equation: 'v = Δx / Δt',
    description: 'Calculates average velocity from displacement and time interval.',
    variables: [
      { symbol: 'v', name: 'Velocity', unit: 'm/s' },
      { symbol: 'dx', name: 'Displacement', unit: 'm' },
      { symbol: 'dt', name: 'Time interval', unit: 's' },
    ],
    keywords: ['velocity', 'speed', 'kinematics', 'motion', 'displacement'],
    solve: {
      v: (v) => v.dx / v.dt,
      dx: (v) => v.v * v.dt,
      dt: (v) => v.dx / v.v,
    },
  },
  {
    id: 'acceleration',
    name: 'Acceleration',
    category: 'Physics',
    subcategory: 'Kinematics',
    equation: 'a = Δv / Δt',
    description: 'Calculates acceleration from a change in velocity over a time interval.',
    variables: [
      { symbol: 'a', name: 'Acceleration', unit: 'm/s²' },
      { symbol: 'dv', name: 'Change in velocity', unit: 'm/s' },
      { symbol: 'dt', name: 'Time interval', unit: 's' },
    ],
    keywords: ['acceleration', 'kinematics', 'motion', 'velocity change', 'speeding up'],
    solve: {
      a: (v) => v.dv / v.dt,
      dv: (v) => v.a * v.dt,
      dt: (v) => v.dv / v.a,
    },
  },
  {
    id: 'kinematics-velocity-time',
    name: 'Kinematic Equation (v = u + at)',
    category: 'Physics',
    subcategory: 'Kinematics',
    equation: 'v = u + at',
    description: 'Relates final velocity to initial velocity, acceleration, and time for constant acceleration.',
    variables: [
      { symbol: 'v', name: 'Final velocity', unit: 'm/s' },
      { symbol: 'u', name: 'Initial velocity', unit: 'm/s' },
      { symbol: 'a', name: 'Acceleration', unit: 'm/s²' },
      { symbol: 't', name: 'Time', unit: 's' },
    ],
    keywords: ['kinematics', 'equation of motion', 'final velocity', 'initial velocity', 'constant acceleration'],
    solve: {
      v: (v) => v.u + v.a * v.t,
      u: (v) => v.v - v.a * v.t,
      a: (v) => (v.v - v.u) / v.t,
      t: (v) => (v.v - v.u) / v.a,
    },
  },
  {
    id: 'kinematics-velocity-squared',
    name: 'Kinematic Equation (v² = u² + 2as)',
    category: 'Physics',
    subcategory: 'Kinematics',
    equation: 'v² = u² + 2as',
    description: 'Relates final velocity, initial velocity, acceleration, and displacement (no time needed).',
    variables: [
      { symbol: 'v', name: 'Final velocity', unit: 'm/s' },
      { symbol: 'u', name: 'Initial velocity', unit: 'm/s' },
      { symbol: 'a', name: 'Acceleration', unit: 'm/s²' },
      { symbol: 's', name: 'Displacement', unit: 'm' },
    ],
    keywords: ['kinematics', 'equation of motion', 'velocity', 'acceleration', 'displacement', 'torricelli'],
    solve: {
      v: (v) => {
        const sq = v.u ** 2 + 2 * v.a * v.s;
        if (sq < 0) throw new Error('u² + 2as is negative — no real velocity.');
        return Math.sqrt(sq);
      },
      u: (v) => {
        const sq = v.v ** 2 - 2 * v.a * v.s;
        if (sq < 0) throw new Error('v² - 2as is negative — no real velocity.');
        return Math.sqrt(sq);
      },
      a: (v) => (v.v ** 2 - v.u ** 2) / (2 * v.s),
      s: (v) => (v.v ** 2 - v.u ** 2) / (2 * v.a),
    },
  },
  {
    id: 'kinematics-displacement',
    name: 'Kinematic Equation (s = ut + ½at²)',
    category: 'Physics',
    subcategory: 'Kinematics',
    equation: 's = ut + ½at²',
    description: 'Relates displacement, initial velocity, acceleration, and time for constant acceleration.',
    variables: [
      { symbol: 's', name: 'Displacement', unit: 'm' },
      { symbol: 'u', name: 'Initial velocity', unit: 'm/s' },
      { symbol: 'a', name: 'Acceleration', unit: 'm/s²' },
      { symbol: 't', name: 'Time', unit: 's' },
    ],
    keywords: ['kinematics', 'equation of motion', 'displacement', 'time', 'position'],
    solve: {
      s: (v) => v.u * v.t + 0.5 * v.a * v.t ** 2,
      u: (v) => (v.s - 0.5 * v.a * v.t ** 2) / v.t,
      a: (v) => (2 * (v.s - v.u * v.t)) / v.t ** 2,
      t: (v) => {
        if (v.a === 0) {
          if (v.u === 0) throw new Error('Cannot solve for time when both initial velocity and acceleration are zero.');
          return v.s / v.u;
        }
        const disc = v.u ** 2 + 2 * v.a * v.s;
        if (disc < 0) throw new Error('No real solution for time with these values.');
        const sqrtDisc = Math.sqrt(disc);
        const candidates = [(-v.u + sqrtDisc) / v.a, (-v.u - sqrtDisc) / v.a].filter((t) => t >= 0);
        if (candidates.length === 0) throw new Error('No non-negative time solves these values.');
        return Math.min(...candidates);
      },
    },
  },
  {
    id: 'average-velocity',
    name: 'Average Velocity (Constant Acceleration)',
    category: 'Physics',
    subcategory: 'Kinematics',
    equation: 'v_avg = (u + v) / 2',
    description: 'Calculates the average velocity during constant acceleration from the initial and final velocities.',
    variables: [
      { symbol: 'vavg', name: 'Average velocity', unit: 'm/s' },
      { symbol: 'u', name: 'Initial velocity', unit: 'm/s' },
      { symbol: 'v', name: 'Final velocity', unit: 'm/s' },
    ],
    keywords: ['average velocity', 'kinematics', 'mean velocity', 'constant acceleration'],
    solve: {
      vavg: (v) => (v.u + v.v) / 2,
      u: (v) => 2 * v.vavg - v.v,
      v: (v) => 2 * v.vavg - v.u,
    },
  },
  {
    id: 'relative-velocity',
    name: 'Relative Velocity',
    category: 'Physics',
    subcategory: 'Kinematics',
    equation: 'v_rel = vA - vB',
    description: 'Calculates the velocity of object A relative to object B using signed velocities along one line of motion (opposite directions should have opposite signs).',
    variables: [
      { symbol: 'vRel', name: 'Relative velocity of A with respect to B', unit: 'm/s' },
      { symbol: 'vA', name: 'Velocity of A', unit: 'm/s' },
      { symbol: 'vB', name: 'Velocity of B', unit: 'm/s' },
    ],
    keywords: ['relative velocity', 'kinematics', 'relative motion', 'closing speed'],
    solve: {
      vRel: (v) => v.vA - v.vB,
      vA: (v) => v.vRel + v.vB,
      vB: (v) => v.vA - v.vRel,
    },
  },
  {
    id: 'free-fall',
    name: 'Free Fall Distance',
    category: 'Physics',
    subcategory: 'Kinematics',
    equation: 'h = ½gt²',
    description: 'Calculates the distance fallen under gravity from rest.',
    variables: [
      { symbol: 'h', name: 'Height fallen', unit: 'm' },
      { symbol: 'g', name: 'Gravitational acceleration', unit: 'm/s²' },
      { symbol: 't', name: 'Time', unit: 's' },
    ],
    keywords: ['free fall', 'gravity', 'kinematics', 'motion', 'height', 'drop'],
    solve: {
      h: (v) => 0.5 * v.g * v.t ** 2,
      g: (v) => (2 * v.h) / v.t ** 2,
      t: (v) => {
        const ratio = (2 * v.h) / v.g;
        if (ratio < 0) throw new Error('2h/g is negative — no real time.');
        return Math.sqrt(ratio);
      },
    },
  },
  {
    id: 'projectile-range',
    name: 'Projectile Range',
    category: 'Physics',
    subcategory: 'Kinematics',
    equation: 'R = (v₀² sin(2θ)) / g',
    description: 'Calculates the horizontal distance traveled by a projectile launched and landing at the same height.',
    variables: [
      { symbol: 'R', name: 'Range', unit: 'm' },
      { symbol: 'v0', name: 'Initial velocity', unit: 'm/s' },
      { symbol: 'theta', name: 'Launch angle', unit: '°' },
      { symbol: 'g', name: 'Gravitational acceleration', unit: 'm/s²' },
    ],
    keywords: ['projectile', 'range', 'kinematics', 'motion', 'angle', 'trajectory'],
    solve: {
      R: (v) => (v.v0 ** 2 * Math.sin((2 * v.theta * Math.PI) / 180)) / v.g,
      v0: (v) => {
        const sq = (v.R * v.g) / Math.sin((2 * v.theta * Math.PI) / 180);
        if (sq < 0) throw new Error('No real initial velocity for these values.');
        return Math.sqrt(sq);
      },
      g: (v) => (v.v0 ** 2 * Math.sin((2 * v.theta * Math.PI) / 180)) / v.R,
      theta: (v) => {
        const ratio = (v.R * v.g) / v.v0 ** 2;
        if (ratio < -1 || ratio > 1) throw new Error('Rg/v₀² must be between -1 and 1.');
        return Math.asin(ratio) * (90 / Math.PI);
      },
    },
  },
  {
    id: 'projectile-max-height',
    name: 'Projectile Maximum Height',
    category: 'Physics',
    subcategory: 'Kinematics',
    equation: 'h_max = (v₀² sin²(θ)) / (2g)',
    description: 'Calculates the maximum height reached by a projectile.',
    variables: [
      { symbol: 'hmax', name: 'Maximum height', unit: 'm' },
      { symbol: 'v0', name: 'Initial velocity', unit: 'm/s' },
      { symbol: 'theta', name: 'Launch angle', unit: '°' },
      { symbol: 'g', name: 'Gravitational acceleration', unit: 'm/s²' },
    ],
    keywords: ['projectile', 'maximum height', 'kinematics', 'motion', 'trajectory'],
    solve: {
      hmax: (v) => (v.v0 ** 2 * Math.sin((v.theta * Math.PI) / 180) ** 2) / (2 * v.g),
      v0: (v) => {
        const sq = (2 * v.g * v.hmax) / Math.sin((v.theta * Math.PI) / 180) ** 2;
        if (sq < 0) throw new Error('No real initial velocity for these values.');
        return Math.sqrt(sq);
      },
      g: (v) => (v.v0 ** 2 * Math.sin((v.theta * Math.PI) / 180) ** 2) / (2 * v.hmax),
      theta: (v) => {
        const sq = (2 * v.g * v.hmax) / v.v0 ** 2;
        if (sq < 0 || sq > 1) throw new Error('2ghmax/v₀² must be between 0 and 1.');
        return Math.asin(Math.sqrt(sq)) * (180 / Math.PI);
      },
    },
  },
];
