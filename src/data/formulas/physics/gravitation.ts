import type { Formula } from '../../../types';

export const gravitationFormulas: Formula[] = [
  {
    id: 'gravitational-force',
    name: 'Newton\'s Law of Gravitation',
    category: 'Physics',
    subcategory: 'Gravitation',
    equation: 'F_g = Gm₁m₂ / r²',
    description: 'Calculates the gravitational attraction between two masses.',
    variables: [
      { symbol: 'Fg', name: 'Gravitational force', unit: 'N' },
      { symbol: 'G', name: 'Gravitational constant (≈6.674×10⁻¹¹)', unit: 'N·m²/kg²' },
      { symbol: 'm1', name: 'Mass 1', unit: 'kg' },
      { symbol: 'm2', name: 'Mass 2', unit: 'kg' },
      { symbol: 'r', name: 'Distance between centers', unit: 'm' },
    ],
    keywords: ['gravitation', 'gravity', 'force', 'mass', 'distance', 'newton'],
    solve: {
      Fg: (v) => (v.G * v.m1 * v.m2) / v.r ** 2,
      G: (v) => (v.Fg * v.r ** 2) / (v.m1 * v.m2),
      m1: (v) => (v.Fg * v.r ** 2) / (v.G * v.m2),
      m2: (v) => (v.Fg * v.r ** 2) / (v.G * v.m1),
      r: (v) => {
        const sq = (v.G * v.m1 * v.m2) / v.Fg;
        if (sq < 0) throw new Error('Gm₁m₂/Fg is negative — no real distance.');
        return Math.sqrt(sq);
      },
    },
  },
  {
    id: 'gravitational-field-strength',
    name: 'Gravitational Field Strength',
    category: 'Physics',
    subcategory: 'Gravitation',
    equation: 'g = GM / r²',
    description: 'Calculates the gravitational field strength (acceleration due to gravity) at a distance from a central mass.',
    variables: [
      { symbol: 'g', name: 'Gravitational field strength', unit: 'm/s²' },
      { symbol: 'G', name: 'Gravitational constant (≈6.674×10⁻¹¹)', unit: 'N·m²/kg²' },
      { symbol: 'M', name: 'Mass of central body', unit: 'kg' },
      { symbol: 'r', name: 'Distance from center', unit: 'm' },
    ],
    keywords: ['gravitational field', 'surface gravity', 'gravity', 'acceleration'],
    solve: {
      g: (v) => (v.G * v.M) / v.r ** 2,
      G: (v) => (v.g * v.r ** 2) / v.M,
      M: (v) => (v.g * v.r ** 2) / v.G,
      r: (v) => {
        const sq = (v.G * v.M) / v.g;
        if (sq < 0) throw new Error('GM/g is negative — no real distance.');
        return Math.sqrt(sq);
      },
    },
  },
  {
    id: 'gravitational-potential-energy',
    name: 'Gravitational Potential Energy (General)',
    category: 'Physics',
    subcategory: 'Gravitation',
    equation: 'U = -GMm / r',
    description: 'Calculates gravitational potential energy between two masses, taking the potential at infinite separation as zero.',
    variables: [
      { symbol: 'U', name: 'Gravitational potential energy', unit: 'J' },
      { symbol: 'G', name: 'Gravitational constant (≈6.674×10⁻¹¹)', unit: 'N·m²/kg²' },
      { symbol: 'M', name: 'Mass of central body', unit: 'kg' },
      { symbol: 'm', name: 'Mass of orbiting/second body', unit: 'kg' },
      { symbol: 'r', name: 'Distance between centers', unit: 'm' },
    ],
    keywords: ['gravitational potential energy', 'gravity', 'orbital energy', 'escape'],
    solve: {
      U: (v) => -(v.G * v.M * v.m) / v.r,
      G: (v) => -(v.U * v.r) / (v.M * v.m),
      M: (v) => -(v.U * v.r) / (v.G * v.m),
      m: (v) => -(v.U * v.r) / (v.G * v.M),
      r: (v) => -(v.G * v.M * v.m) / v.U,
    },
  },
  {
    id: 'orbital-velocity',
    name: 'Orbital Velocity',
    category: 'Physics',
    subcategory: 'Gravitation',
    equation: 'v_orbit = √(GM / r)',
    description: 'Calculates the speed needed to maintain a stable circular orbit around a central mass.',
    variables: [
      { symbol: 'vOrbit', name: 'Orbital velocity', unit: 'm/s' },
      { symbol: 'G', name: 'Gravitational constant (≈6.674×10⁻¹¹)', unit: 'N·m²/kg²' },
      { symbol: 'M', name: 'Mass of central body', unit: 'kg' },
      { symbol: 'r', name: 'Orbital radius', unit: 'm' },
    ],
    keywords: ['orbital velocity', 'orbit', 'gravity', 'space', 'satellite'],
    solve: {
      vOrbit: (v) => {
        const sq = (v.G * v.M) / v.r;
        if (sq < 0) throw new Error('GM/r is negative — no real orbital velocity.');
        return Math.sqrt(sq);
      },
      G: (v) => (v.vOrbit ** 2 * v.r) / v.M,
      M: (v) => (v.vOrbit ** 2 * v.r) / v.G,
      r: (v) => (v.G * v.M) / v.vOrbit ** 2,
    },
  },
  {
    id: 'escape-velocity',
    name: 'Escape Velocity',
    category: 'Physics',
    subcategory: 'Gravitation',
    equation: 'v_escape = √(2GM / r)',
    description: 'Calculates the minimum velocity needed to escape a gravitational field from a given distance.',
    variables: [
      { symbol: 'vEscape', name: 'Escape velocity', unit: 'm/s' },
      { symbol: 'G', name: 'Gravitational constant (≈6.674×10⁻¹¹)', unit: 'N·m²/kg²' },
      { symbol: 'M', name: 'Mass of central body', unit: 'kg' },
      { symbol: 'r', name: 'Distance from center', unit: 'm' },
    ],
    keywords: ['escape velocity', 'gravity', 'space', 'orbital mechanics', 'rocket'],
    solve: {
      vEscape: (v) => {
        const sq = (2 * v.G * v.M) / v.r;
        if (sq < 0) throw new Error('2GM/r is negative — no real escape velocity.');
        return Math.sqrt(sq);
      },
      G: (v) => (v.vEscape ** 2 * v.r) / (2 * v.M),
      M: (v) => (v.vEscape ** 2 * v.r) / (2 * v.G),
      r: (v) => (2 * v.G * v.M) / v.vEscape ** 2,
    },
  },
  {
    id: 'keplers-third-law',
    name: "Kepler's Third Law",
    category: 'Physics',
    subcategory: 'Gravitation',
    equation: 'T² = (4π² / GM)r³',
    description: 'Relates the orbital period and orbital radius for a body in circular orbit around a much larger central mass.',
    variables: [
      { symbol: 'T', name: 'Orbital period', unit: 's' },
      { symbol: 'G', name: 'Gravitational constant (≈6.674×10⁻¹¹)', unit: 'N·m²/kg²' },
      { symbol: 'M', name: 'Mass of central body', unit: 'kg' },
      { symbol: 'r', name: 'Orbital radius', unit: 'm' },
    ],
    keywords: ['kepler', 'orbital period', 'radius', 'gravity', 'orbit', "kepler's third law"],
    solve: {
      T: (v) => {
        const sq = (4 * Math.PI ** 2 * v.r ** 3) / (v.G * v.M);
        if (sq < 0) throw new Error('4π²r³/GM is negative — no real period.');
        return Math.sqrt(sq);
      },
      G: (v) => (4 * Math.PI ** 2 * v.r ** 3) / (v.M * v.T ** 2),
      M: (v) => (4 * Math.PI ** 2 * v.r ** 3) / (v.G * v.T ** 2),
      r: (v) => Math.cbrt((v.T ** 2 * v.G * v.M) / (4 * Math.PI ** 2)),
    },
  },
];
