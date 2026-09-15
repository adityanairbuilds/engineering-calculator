import type { Formula } from '../../../types';

export const circularMotionFormulas: Formula[] = [
  {
    id: 'centripetal-acceleration',
    name: 'Centripetal Acceleration',
    category: 'Physics',
    subcategory: 'Circular Motion',
    equation: 'a_c = v² / r',
    description: 'Calculates the centripetal acceleration of an object moving in a circular path.',
    variables: [
      { symbol: 'ac', name: 'Centripetal acceleration', unit: 'm/s²' },
      { symbol: 'v', name: 'Tangential velocity', unit: 'm/s' },
      { symbol: 'r', name: 'Radius of circular path', unit: 'm' },
    ],
    keywords: ['centripetal', 'acceleration', 'circular motion', 'velocity', 'radius'],
    solve: {
      ac: (v) => v.v ** 2 / v.r,
      v: (v) => {
        const sq = v.ac * v.r;
        if (sq < 0) throw new Error('ac·r is negative — no real velocity.');
        return Math.sqrt(sq);
      },
      r: (v) => v.v ** 2 / v.ac,
    },
  },
  {
    id: 'centripetal-force',
    name: 'Centripetal Force',
    category: 'Physics',
    subcategory: 'Circular Motion',
    equation: 'F_c = mv² / r',
    description: 'Calculates the centripetal force needed to keep an object moving in a circular path.',
    variables: [
      { symbol: 'Fc', name: 'Centripetal force', unit: 'N' },
      { symbol: 'm', name: 'Mass', unit: 'kg' },
      { symbol: 'v', name: 'Tangential velocity', unit: 'm/s' },
      { symbol: 'r', name: 'Radius of circular path', unit: 'm' },
    ],
    keywords: ['centripetal', 'force', 'circular motion', 'mass', 'velocity'],
    solve: {
      Fc: (v) => (v.m * v.v ** 2) / v.r,
      m: (v) => (v.Fc * v.r) / v.v ** 2,
      v: (v) => {
        const sq = (v.Fc * v.r) / v.m;
        if (sq < 0) throw new Error('Fc·r/m is negative — no real velocity.');
        return Math.sqrt(sq);
      },
      r: (v) => (v.m * v.v ** 2) / v.Fc,
    },
  },
  {
    id: 'angular-velocity',
    name: 'Angular Velocity',
    category: 'Physics',
    subcategory: 'Circular Motion',
    equation: 'ω = θ / t',
    description: 'Calculates angular velocity from angular displacement and time.',
    variables: [
      { symbol: 'omega', name: 'Angular velocity', unit: 'rad/s' },
      { symbol: 'theta', name: 'Angular displacement', unit: 'rad' },
      { symbol: 't', name: 'Time', unit: 's' },
    ],
    keywords: ['angular velocity', 'circular motion', 'rotation', 'angle', 'time', 'omega'],
    solve: {
      omega: (v) => v.theta / v.t,
      theta: (v) => v.omega * v.t,
      t: (v) => v.theta / v.omega,
    },
  },
  {
    id: 'angular-acceleration',
    name: 'Angular Acceleration',
    category: 'Physics',
    subcategory: 'Circular Motion',
    equation: 'α = Δω / Δt',
    description: 'Calculates angular acceleration from a change in angular velocity over a time interval.',
    variables: [
      { symbol: 'alpha', name: 'Angular acceleration', unit: 'rad/s²' },
      { symbol: 'domega', name: 'Change in angular velocity', unit: 'rad/s' },
      { symbol: 'dt', name: 'Time interval', unit: 's' },
    ],
    keywords: ['angular acceleration', 'circular motion', 'rotation', 'angular velocity'],
    solve: {
      alpha: (v) => v.domega / v.dt,
      domega: (v) => v.alpha * v.dt,
      dt: (v) => v.domega / v.alpha,
    },
  },
  {
    id: 'period-frequency',
    name: 'Period and Frequency',
    category: 'Physics',
    subcategory: 'Circular Motion',
    equation: 'T = 1 / f',
    description: 'Relates the period and frequency of any repeating (periodic) motion, such as rotation or oscillation.',
    variables: [
      { symbol: 'T', name: 'Period', unit: 's' },
      { symbol: 'f', name: 'Frequency', unit: 'Hz' },
    ],
    keywords: ['period', 'frequency', 'circular motion', 'rotation', 'time', 'cycle'],
    solve: {
      T: (v) => 1 / v.f,
      f: (v) => 1 / v.T,
    },
  },
  {
    id: 'tangential-velocity',
    name: 'Tangential Velocity',
    category: 'Physics',
    subcategory: 'Circular Motion',
    equation: 'v = rω',
    description: 'Calculates the tangential (linear) speed of a point moving in a circle from the radius and angular velocity.',
    variables: [
      { symbol: 'v', name: 'Tangential velocity', unit: 'm/s' },
      { symbol: 'r', name: 'Radius', unit: 'm' },
      { symbol: 'omega', name: 'Angular velocity', unit: 'rad/s' },
    ],
    keywords: ['tangential velocity', 'linear velocity', 'angular velocity', 'circular motion', 'rotation'],
    solve: {
      v: (v) => v.r * v.omega,
      r: (v) => v.v / v.omega,
      omega: (v) => v.v / v.r,
    },
  },
  {
    id: 'torque',
    name: 'Torque',
    category: 'Physics',
    subcategory: 'Rotational Motion',
    equation: 'τ = rF sin(θ)',
    description: 'Calculates the torque produced by a force applied at a distance from a pivot point.',
    variables: [
      { symbol: 'tau', name: 'Torque', unit: 'N·m' },
      { symbol: 'r', name: 'Distance from pivot (lever arm)', unit: 'm' },
      { symbol: 'F', name: 'Applied force', unit: 'N' },
      { symbol: 'theta', name: 'Angle between force and lever arm', unit: '°' },
    ],
    keywords: ['torque', 'moment', 'rotation', 'force', 'lever arm', 'rotational motion'],
    solve: {
      tau: (v) => v.r * v.F * Math.sin((v.theta * Math.PI) / 180),
      r: (v) => v.tau / (v.F * Math.sin((v.theta * Math.PI) / 180)),
      F: (v) => v.tau / (v.r * Math.sin((v.theta * Math.PI) / 180)),
      theta: (v) => {
        const ratio = v.tau / (v.r * v.F);
        if (ratio < -1 || ratio > 1) throw new Error('τ/(rF) must be between -1 and 1.');
        return Math.asin(ratio) * (180 / Math.PI);
      },
    },
  },
  {
    id: 'moment-of-inertia-point-mass',
    name: 'Moment of Inertia (Point Mass)',
    category: 'Physics',
    subcategory: 'Rotational Motion',
    equation: 'I = mr²',
    description: 'Calculates the moment of inertia of a point mass rotating about an axis at a fixed radius.',
    variables: [
      { symbol: 'I', name: 'Moment of inertia', unit: 'kg·m²' },
      { symbol: 'm', name: 'Mass', unit: 'kg' },
      { symbol: 'r', name: 'Distance from axis', unit: 'm' },
    ],
    keywords: ['moment of inertia', 'rotational inertia', 'rotation', 'point mass'],
    solve: {
      I: (v) => v.m * v.r ** 2,
      m: (v) => v.I / v.r ** 2,
      r: (v) => {
        const sq = v.I / v.m;
        if (sq < 0) throw new Error('I/m is negative — no real radius.');
        return Math.sqrt(sq);
      },
    },
  },
  {
    id: 'angular-momentum',
    name: 'Angular Momentum',
    category: 'Physics',
    subcategory: 'Rotational Motion',
    equation: 'L = Iω',
    description: 'Calculates the angular momentum of a rotating object from its moment of inertia and angular velocity.',
    variables: [
      { symbol: 'L', name: 'Angular momentum', unit: 'kg·m²/s' },
      { symbol: 'I', name: 'Moment of inertia', unit: 'kg·m²' },
      { symbol: 'omega', name: 'Angular velocity', unit: 'rad/s' },
    ],
    keywords: ['angular momentum', 'rotation', 'moment of inertia', 'spin'],
    solve: {
      L: (v) => v.I * v.omega,
      I: (v) => v.L / v.omega,
      omega: (v) => v.L / v.I,
    },
  },
  {
    id: 'rotational-kinetic-energy',
    name: 'Rotational Kinetic Energy',
    category: 'Physics',
    subcategory: 'Rotational Motion',
    equation: 'KE_rot = ½Iω²',
    description: 'Calculates the kinetic energy of a rotating object from its moment of inertia and angular velocity.',
    variables: [
      { symbol: 'KErot', name: 'Rotational kinetic energy', unit: 'J' },
      { symbol: 'I', name: 'Moment of inertia', unit: 'kg·m²' },
      { symbol: 'omega', name: 'Angular velocity', unit: 'rad/s' },
    ],
    keywords: ['rotational kinetic energy', 'rotation', 'moment of inertia', 'spinning energy'],
    solve: {
      KErot: (v) => 0.5 * v.I * v.omega ** 2,
      I: (v) => (2 * v.KErot) / v.omega ** 2,
      omega: (v) => {
        const sq = (2 * v.KErot) / v.I;
        if (sq < 0) throw new Error('2·KErot/I is negative — no real angular velocity.');
        return Math.sqrt(sq);
      },
    },
  },
  {
    id: 'newtons-second-law-rotation',
    name: "Newton's Second Law (Rotation)",
    category: 'Physics',
    subcategory: 'Rotational Motion',
    equation: 'τ = Iα',
    description: 'Relates net torque, moment of inertia, and angular acceleration — the rotational analogue of F = ma.',
    variables: [
      { symbol: 'tau', name: 'Net torque', unit: 'N·m' },
      { symbol: 'I', name: 'Moment of inertia', unit: 'kg·m²' },
      { symbol: 'alpha', name: 'Angular acceleration', unit: 'rad/s²' },
    ],
    keywords: ['torque', 'rotational newtons second law', 'moment of inertia', 'angular acceleration', 'rotation'],
    solve: {
      tau: (v) => v.I * v.alpha,
      I: (v) => v.tau / v.alpha,
      alpha: (v) => v.tau / v.I,
    },
  },
];
