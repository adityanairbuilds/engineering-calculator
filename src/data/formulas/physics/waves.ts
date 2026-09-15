import type { Formula } from '../../../types';

export const wavesFormulas: Formula[] = [
  {
    id: 'wave-speed',
    name: 'Wave Speed',
    category: 'Physics',
    subcategory: 'Waves',
    equation: 'v = fλ',
    description: 'Calculates wave speed from frequency and wavelength.',
    variables: [
      { symbol: 'v', name: 'Wave speed', unit: 'm/s' },
      { symbol: 'f', name: 'Frequency', unit: 'Hz' },
      { symbol: 'lambda', name: 'Wavelength', unit: 'm' },
    ],
    keywords: ['wave speed', 'frequency', 'wavelength', 'wave', 'sound', 'light'],
    solve: {
      v: (v) => v.f * v.lambda,
      f: (v) => v.v / v.lambda,
      lambda: (v) => v.v / v.f,
    },
  },
  {
    id: 'sound-intensity',
    name: 'Sound Intensity',
    category: 'Physics',
    subcategory: 'Waves',
    equation: 'I = P / A',
    description: 'Calculates sound (or wave) intensity from power and the area it is spread over.',
    variables: [
      { symbol: 'I', name: 'Intensity', unit: 'W/m²' },
      { symbol: 'P', name: 'Power', unit: 'W' },
      { symbol: 'A', name: 'Area', unit: 'm²' },
    ],
    keywords: ['sound', 'intensity', 'power', 'area', 'wave'],
    solve: {
      I: (v) => v.P / v.A,
      P: (v) => v.I * v.A,
      A: (v) => v.P / v.I,
    },
  },
  {
    id: 'decibel',
    name: 'Decibel Scale',
    category: 'Physics',
    subcategory: 'Waves',
    equation: 'dB = 10 log₁₀(I / I₀)',
    description: 'Calculates sound level in decibels from intensity relative to a reference intensity.',
    variables: [
      { symbol: 'dB', name: 'Sound level', unit: 'dB' },
      { symbol: 'I', name: 'Sound intensity', unit: 'W/m²' },
      { symbol: 'I0', name: 'Reference intensity (typically 10⁻¹²)', unit: 'W/m²' },
    ],
    keywords: ['decibel', 'sound level', 'logarithm', 'intensity', 'wave', 'loudness'],
    solve: {
      dB: (v) => {
        if (v.I <= 0 || v.I0 <= 0) throw new Error('Intensities must be positive.');
        return 10 * Math.log10(v.I / v.I0);
      },
      I: (v) => v.I0 * 10 ** (v.dB / 10),
      I0: (v) => v.I / 10 ** (v.dB / 10),
    },
  },
  {
    id: 'doppler-effect',
    name: 'Doppler Effect',
    category: 'Physics',
    subcategory: 'Waves',
    equation: 'f_obs = f(v + v_o) / (v - v_s)',
    description: 'Calculates the observed frequency when a source and/or observer are moving relative to each other. Use a positive v_o (observer velocity) if the observer moves toward the source, negative if away; positive v_s (source velocity) if the source moves toward the observer, negative if away.',
    variables: [
      { symbol: 'fObserved', name: 'Observed frequency', unit: 'Hz' },
      { symbol: 'f', name: 'Source frequency', unit: 'Hz' },
      { symbol: 'v', name: 'Wave speed in medium', unit: 'm/s' },
      { symbol: 'vObserver', name: 'Observer velocity (+ toward source)', unit: 'm/s' },
      { symbol: 'vSource', name: 'Source velocity (+ toward observer)', unit: 'm/s' },
    ],
    keywords: ['doppler', 'doppler effect', 'frequency', 'motion', 'wave', 'sound', 'observed frequency'],
    solve: {
      fObserved: (v) => (v.f * (v.v + v.vObserver)) / (v.v - v.vSource),
      f: (v) => (v.fObserved * (v.v - v.vSource)) / (v.v + v.vObserver),
      v: (v) => (v.fObserved * v.vSource + v.f * v.vObserver) / (v.fObserved - v.f),
      vObserver: (v) => (v.fObserved * (v.v - v.vSource) - v.f * v.v) / v.f,
      vSource: (v) => v.v - (v.f * (v.v + v.vObserver)) / v.fObserved,
    },
  },
  {
    id: 'interference-double-slit',
    name: 'Double Slit Interference',
    category: 'Physics',
    subcategory: 'Waves',
    equation: 'd sin(θ) = nλ',
    description: 'Calculates the condition for constructive interference (bright fringes) in a double slit experiment.',
    variables: [
      { symbol: 'd', name: 'Slit separation', unit: 'm' },
      { symbol: 'theta', name: 'Angle to the bright fringe', unit: '°' },
      { symbol: 'n', name: 'Fringe order (integer)', unit: 'dimensionless' },
      { symbol: 'lambda', name: 'Wavelength', unit: 'm' },
    ],
    keywords: ['interference', 'double slit', 'diffraction', 'wavelength', 'light', 'fringe'],
    solve: {
      d: (v) => (v.n * v.lambda) / Math.sin((v.theta * Math.PI) / 180),
      theta: (v) => {
        const ratio = (v.n * v.lambda) / v.d;
        if (ratio < -1 || ratio > 1) throw new Error('nλ/d must be between -1 and 1.');
        return Math.asin(ratio) * (180 / Math.PI);
      },
      n: (v) => (v.d * Math.sin((v.theta * Math.PI) / 180)) / v.lambda,
      lambda: (v) => (v.d * Math.sin((v.theta * Math.PI) / 180)) / v.n,
    },
  },
  {
    id: 'harmonic-motion',
    name: 'Simple Harmonic Motion',
    category: 'Physics',
    subcategory: 'Waves',
    equation: 'x = A cos(ωt + φ)',
    description: 'Describes the displacement of an object undergoing simple harmonic motion over time. Inverse solves return the principal-value solution.',
    variables: [
      { symbol: 'x', name: 'Displacement', unit: 'm' },
      { symbol: 'A', name: 'Amplitude', unit: 'm' },
      { symbol: 'omega', name: 'Angular frequency', unit: 'rad/s' },
      { symbol: 't', name: 'Time', unit: 's' },
      { symbol: 'phi', name: 'Phase constant', unit: '°' },
    ],
    keywords: ['harmonic motion', 'oscillation', 'amplitude', 'frequency', 'wave', 'shm', 'phase'],
    solve: {
      x: (v) => v.A * Math.cos(v.omega * v.t + (v.phi * Math.PI) / 180),
      A: (v) => v.x / Math.cos(v.omega * v.t + (v.phi * Math.PI) / 180),
      omega: (v) => {
        const ratio = v.x / v.A;
        if (ratio < -1 || ratio > 1) throw new Error('x/A must be between -1 and 1.');
        return (Math.acos(ratio) - (v.phi * Math.PI) / 180) / v.t;
      },
      t: (v) => {
        const ratio = v.x / v.A;
        if (ratio < -1 || ratio > 1) throw new Error('x/A must be between -1 and 1.');
        return (Math.acos(ratio) - (v.phi * Math.PI) / 180) / v.omega;
      },
      phi: (v) => {
        const ratio = v.x / v.A;
        if (ratio < -1 || ratio > 1) throw new Error('x/A must be between -1 and 1.');
        return (Math.acos(ratio) - v.omega * v.t) * (180 / Math.PI);
      },
    },
  },
  {
    id: 'pendulum-period',
    name: 'Simple Pendulum Period',
    category: 'Physics',
    subcategory: 'Waves',
    equation: 'T = 2π√(L / g)',
    description: 'Calculates the period of a simple pendulum for small oscillation angles.',
    variables: [
      { symbol: 'T', name: 'Period', unit: 's' },
      { symbol: 'L', name: 'Pendulum length', unit: 'm' },
      { symbol: 'g', name: 'Gravitational acceleration', unit: 'm/s²' },
    ],
    keywords: ['pendulum', 'period', 'oscillation', 'simple harmonic motion', 'gravity'],
    solve: {
      T: (v) => {
        if (v.L / v.g < 0) throw new Error('L/g is negative — no real period.');
        return 2 * Math.PI * Math.sqrt(v.L / v.g);
      },
      L: (v) => v.g * (v.T / (2 * Math.PI)) ** 2,
      g: (v) => v.L / (v.T / (2 * Math.PI)) ** 2,
    },
  },
  {
    id: 'mass-spring-period',
    name: 'Mass-Spring Period',
    category: 'Physics',
    subcategory: 'Waves',
    equation: 'T = 2π√(m / k)',
    description: 'Calculates the period of oscillation of a mass on an ideal spring.',
    variables: [
      { symbol: 'T', name: 'Period', unit: 's' },
      { symbol: 'm', name: 'Mass', unit: 'kg' },
      { symbol: 'k', name: 'Spring constant', unit: 'N/m' },
    ],
    keywords: ['spring', 'period', 'oscillation', 'simple harmonic motion', 'mass-spring system'],
    solve: {
      T: (v) => {
        if (v.m / v.k < 0) throw new Error('m/k is negative — no real period.');
        return 2 * Math.PI * Math.sqrt(v.m / v.k);
      },
      m: (v) => v.k * (v.T / (2 * Math.PI)) ** 2,
      k: (v) => v.m / (v.T / (2 * Math.PI)) ** 2,
    },
  },
  {
    id: 'snells-law',
    name: "Snell's Law",
    category: 'Physics',
    subcategory: 'Optics',
    equation: 'n₁ sin(θ₁) = n₂ sin(θ₂)',
    description: 'Relates the angles of incidence and refraction as light passes between two media of different refractive index.',
    variables: [
      { symbol: 'n1', name: 'Refractive index of medium 1', unit: 'dimensionless' },
      { symbol: 'theta1', name: 'Angle of incidence', unit: '°' },
      { symbol: 'n2', name: 'Refractive index of medium 2', unit: 'dimensionless' },
      { symbol: 'theta2', name: 'Angle of refraction', unit: '°' },
    ],
    keywords: ['snell', "snell's law", 'refraction', 'optics', 'light', 'refractive index'],
    solve: {
      theta2: (v) => {
        const ratio = (v.n1 * Math.sin((v.theta1 * Math.PI) / 180)) / v.n2;
        if (ratio < -1 || ratio > 1) throw new Error('Total internal reflection — no real refraction angle.');
        return Math.asin(ratio) * (180 / Math.PI);
      },
      theta1: (v) => {
        const ratio = (v.n2 * Math.sin((v.theta2 * Math.PI) / 180)) / v.n1;
        if (ratio < -1 || ratio > 1) throw new Error('No real angle of incidence for these values.');
        return Math.asin(ratio) * (180 / Math.PI);
      },
      n1: (v) => (v.n2 * Math.sin((v.theta2 * Math.PI) / 180)) / Math.sin((v.theta1 * Math.PI) / 180),
      n2: (v) => (v.n1 * Math.sin((v.theta1 * Math.PI) / 180)) / Math.sin((v.theta2 * Math.PI) / 180),
    },
  },
];
