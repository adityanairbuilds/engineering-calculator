import type { Formula } from '../../../types';

export const aerospaceFormulas: Formula[] = [
  {
    id: 'lift-coefficient',
    name: 'Lift Coefficient',
    category: 'Engineering',
    subcategory: 'Aerospace Engineering',
    equation: 'C_l = L / (½ρv²S)',
    description: 'Dimensionless coefficient relating lift force to dynamic pressure and wing area.',
    variables: [
      { symbol: 'Cl', name: 'Lift coefficient', unit: 'dimensionless' },
      { symbol: 'L', name: 'Lift force', unit: 'N' },
      { symbol: 'rho', name: 'Air density', unit: 'kg/m³' },
      { symbol: 'v', name: 'Airspeed', unit: 'm/s' },
      { symbol: 'S', name: 'Wing area', unit: 'm²' },
    ],
    keywords: ['lift coefficient', 'aerodynamics', 'aerospace engineering', 'wing'],
    solve: {
      Cl: (v) => v.L / (0.5 * v.rho * v.v ** 2 * v.S),
      L: (v) => v.Cl * 0.5 * v.rho * v.v ** 2 * v.S,
      rho: (v) => (2 * v.L) / (v.Cl * v.v ** 2 * v.S),
      v: (v) => {
        const val = (2 * v.L) / (v.Cl * v.rho * v.S);
        if (val < 0) throw new Error('Cannot take the square root of a negative value for these inputs.');
        return Math.sqrt(val);
      },
      S: (v) => (2 * v.L) / (v.Cl * v.rho * v.v ** 2),
    },
  },
  {
    id: 'drag-coefficient',
    name: 'Drag Coefficient',
    category: 'Engineering',
    subcategory: 'Aerospace Engineering',
    equation: 'C_d = D / (½ρv²S)',
    description: 'Dimensionless coefficient relating drag force to dynamic pressure and reference area.',
    variables: [
      { symbol: 'Cd', name: 'Drag coefficient', unit: 'dimensionless' },
      { symbol: 'D', name: 'Drag force', unit: 'N' },
      { symbol: 'rho', name: 'Air density', unit: 'kg/m³' },
      { symbol: 'v', name: 'Airspeed', unit: 'm/s' },
      { symbol: 'S', name: 'Reference area', unit: 'm²' },
    ],
    keywords: ['drag coefficient', 'aerodynamics', 'aerospace engineering'],
    solve: {
      Cd: (v) => v.D / (0.5 * v.rho * v.v ** 2 * v.S),
      D: (v) => v.Cd * 0.5 * v.rho * v.v ** 2 * v.S,
      rho: (v) => (2 * v.D) / (v.Cd * v.v ** 2 * v.S),
      v: (v) => {
        const val = (2 * v.D) / (v.Cd * v.rho * v.S);
        if (val < 0) throw new Error('Cannot take the square root of a negative value for these inputs.');
        return Math.sqrt(val);
      },
      S: (v) => (2 * v.D) / (v.Cd * v.rho * v.v ** 2),
    },
  },
  {
    id: 'wing-loading',
    name: 'Wing Loading',
    category: 'Engineering',
    subcategory: 'Aerospace Engineering',
    equation: 'WL = W / S',
    description: 'Calculates the weight supported per unit of wing area.',
    variables: [
      { symbol: 'WL', name: 'Wing loading', unit: 'N/m²' },
      { symbol: 'W', name: 'Aircraft weight', unit: 'N' },
      { symbol: 'S', name: 'Wing area', unit: 'm²' },
    ],
    keywords: ['wing loading', 'aerospace engineering', 'aircraft weight'],
    solve: {
      WL: (v) => v.W / v.S,
      W: (v) => v.WL * v.S,
      S: (v) => v.W / v.WL,
    },
  },
  {
    id: 'mach-number',
    name: 'Mach Number',
    category: 'Engineering',
    subcategory: 'Aerospace Engineering',
    equation: 'M = v / a',
    description: 'Calculates the ratio of an object\'s speed to the local speed of sound.',
    variables: [
      { symbol: 'M', name: 'Mach number', unit: 'dimensionless' },
      { symbol: 'v', name: 'Velocity', unit: 'm/s' },
      { symbol: 'a', name: 'Speed of sound', unit: 'm/s' },
    ],
    keywords: ['mach number', 'speed of sound', 'supersonic', 'aerospace engineering'],
    solve: {
      M: (v) => v.v / v.a,
      v: (v) => v.M * v.a,
      a: (v) => v.v / v.M,
    },
  },
  {
    id: 'specific-fuel-consumption',
    name: 'Specific Fuel Consumption',
    category: 'Engineering',
    subcategory: 'Aerospace Engineering',
    equation: 'SFC = Fuel / (Thrust × Time)',
    description: 'Calculates fuel mass consumed per unit of thrust per unit of time.',
    variables: [
      { symbol: 'SFC', name: 'Specific fuel consumption', unit: 'kg/(N·s)' },
      { symbol: 'Fuel', name: 'Fuel mass consumed', unit: 'kg' },
      { symbol: 'Thrust', name: 'Engine thrust', unit: 'N' },
      { symbol: 'Time', name: 'Operating time', unit: 's' },
    ],
    keywords: ['specific fuel consumption', 'sfc', 'aerospace engineering', 'engine performance'],
    solve: {
      SFC: (v) => v.Fuel / (v.Thrust * v.Time),
      Fuel: (v) => v.SFC * v.Thrust * v.Time,
      Thrust: (v) => v.Fuel / (v.SFC * v.Time),
      Time: (v) => v.Fuel / (v.SFC * v.Thrust),
    },
  },
  {
    id: 'thrust-to-weight-ratio',
    name: 'Thrust-to-Weight Ratio',
    category: 'Engineering',
    subcategory: 'Aerospace Engineering',
    equation: 'TWR = T / W',
    description: 'Calculates the ratio of thrust to weight for an aircraft or rocket, a key measure of performance.',
    variables: [
      { symbol: 'TWR', name: 'Thrust-to-weight ratio', unit: 'dimensionless' },
      { symbol: 'T', name: 'Thrust', unit: 'N' },
      { symbol: 'W', name: 'Weight', unit: 'N' },
    ],
    keywords: ['thrust to weight ratio', 'twr', 'aerospace engineering', 'rocket', 'aircraft performance'],
    solve: {
      TWR: (v) => v.T / v.W,
      T: (v) => v.TWR * v.W,
      W: (v) => v.T / v.TWR,
    },
  },
  {
    id: 'ideal-rocket-equation',
    name: 'Ideal Rocket Equation (Tsiolkovsky)',
    category: 'Engineering',
    subcategory: 'Aerospace Engineering',
    equation: 'Δv = I_spg₀ln(m₀/m_f)',
    description: "Calculates a rocket's change in velocity from its specific impulse and the ratio of initial to final mass.",
    variables: [
      { symbol: 'deltaV', name: 'Change in velocity', unit: 'm/s' },
      { symbol: 'Isp', name: 'Specific impulse', unit: 's' },
      { symbol: 'g0', name: 'Standard gravity', unit: 'm/s²' },
      { symbol: 'm0', name: 'Initial (wet) mass', unit: 'kg' },
      { symbol: 'mf', name: 'Final (dry) mass', unit: 'kg' },
    ],
    keywords: ['rocket equation', 'tsiolkovsky', 'delta-v', 'specific impulse', 'aerospace engineering'],
    solve: {
      deltaV: (v) => {
        if (v.m0 <= 0 || v.mf <= 0) throw new Error('Initial and final mass must be positive.');
        return v.Isp * v.g0 * Math.log(v.m0 / v.mf);
      },
      Isp: (v) => {
        if (v.m0 <= 0 || v.mf <= 0) throw new Error('Initial and final mass must be positive.');
        return v.deltaV / (v.g0 * Math.log(v.m0 / v.mf));
      },
      g0: (v) => {
        if (v.m0 <= 0 || v.mf <= 0) throw new Error('Initial and final mass must be positive.');
        return v.deltaV / (v.Isp * Math.log(v.m0 / v.mf));
      },
      m0: (v) => v.mf * Math.exp(v.deltaV / (v.Isp * v.g0)),
      mf: (v) => v.m0 * Math.exp(-v.deltaV / (v.Isp * v.g0)),
    },
  },
  {
    id: 'specific-impulse',
    name: 'Specific Impulse',
    category: 'Engineering',
    subcategory: 'Aerospace Engineering',
    equation: 'I_sp = F / (ṁg₀)',
    description: 'Calculates the specific impulse of a rocket engine from thrust and propellant mass flow rate.',
    variables: [
      { symbol: 'Isp', name: 'Specific impulse', unit: 's' },
      { symbol: 'F', name: 'Thrust', unit: 'N' },
      { symbol: 'mdot', name: 'Propellant mass flow rate', unit: 'kg/s' },
      { symbol: 'g0', name: 'Standard gravity', unit: 'm/s²' },
    ],
    keywords: ['specific impulse', 'isp', 'rocket engine', 'thrust', 'aerospace engineering'],
    solve: {
      Isp: (v) => v.F / (v.mdot * v.g0),
      F: (v) => v.Isp * v.mdot * v.g0,
      mdot: (v) => v.F / (v.Isp * v.g0),
      g0: (v) => v.F / (v.Isp * v.mdot),
    },
  },
];
