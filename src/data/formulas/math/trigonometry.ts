import type { Formula } from '../../../types';

const toRad = (deg: number) => (deg * Math.PI) / 180;
const toDeg = (rad: number) => (rad * 180) / Math.PI;

export const trigonometryFormulas: Formula[] = [
  {
    id: 'sine-ratio-right-triangle',
    name: 'Sine Ratio (Right Triangle)',
    category: 'Mathematics',
    subcategory: 'Trigonometry',
    equation: 'sin(θ) = opposite / hypotenuse',
    description: 'Defines the sine of an acute angle in a right triangle (SOH).',
    variables: [
      { symbol: 'sinTheta', name: 'sin(θ)', unit: 'dimensionless' },
      { symbol: 'opposite', name: 'Opposite side', unit: 'dimensionless' },
      { symbol: 'hypotenuse', name: 'Hypotenuse', unit: 'dimensionless' },
    ],
    keywords: ['sine', 'soh cah toa', 'right triangle', 'trig ratio'],
    solve: {
      sinTheta: (v) => v.opposite / v.hypotenuse,
      opposite: (v) => v.sinTheta * v.hypotenuse,
      hypotenuse: (v) => v.opposite / v.sinTheta,
    },
  },
  {
    id: 'cosine-ratio-right-triangle',
    name: 'Cosine Ratio (Right Triangle)',
    category: 'Mathematics',
    subcategory: 'Trigonometry',
    equation: 'cos(θ) = adjacent / hypotenuse',
    description: 'Defines the cosine of an acute angle in a right triangle (CAH).',
    variables: [
      { symbol: 'cosTheta', name: 'cos(θ)', unit: 'dimensionless' },
      { symbol: 'adjacent', name: 'Adjacent side', unit: 'dimensionless' },
      { symbol: 'hypotenuse', name: 'Hypotenuse', unit: 'dimensionless' },
    ],
    keywords: ['cosine', 'soh cah toa', 'right triangle', 'trig ratio'],
    solve: {
      cosTheta: (v) => v.adjacent / v.hypotenuse,
      adjacent: (v) => v.cosTheta * v.hypotenuse,
      hypotenuse: (v) => v.adjacent / v.cosTheta,
    },
  },
  {
    id: 'tangent-ratio-right-triangle',
    name: 'Tangent Ratio (Right Triangle)',
    category: 'Mathematics',
    subcategory: 'Trigonometry',
    equation: 'tan(θ) = opposite / adjacent',
    description: 'Defines the tangent of an acute angle in a right triangle (TOA).',
    variables: [
      { symbol: 'tanTheta', name: 'tan(θ)', unit: 'dimensionless' },
      { symbol: 'opposite', name: 'Opposite side', unit: 'dimensionless' },
      { symbol: 'adjacent', name: 'Adjacent side', unit: 'dimensionless' },
    ],
    keywords: ['tangent', 'soh cah toa', 'right triangle', 'trig ratio'],
    solve: {
      tanTheta: (v) => v.opposite / v.adjacent,
      opposite: (v) => v.tanTheta * v.adjacent,
      adjacent: (v) => v.opposite / v.tanTheta,
    },
  },
  {
    id: 'law-of-sines',
    name: 'Law of Sines',
    category: 'Mathematics',
    subcategory: 'Trigonometry',
    equation: 'a / sin(A) = b / sin(B)',
    description: 'Relates two side–angle pairs of any triangle. Angles are in degrees.',
    variables: [
      { symbol: 'a', name: 'Side a', unit: 'dimensionless' },
      { symbol: 'A', name: 'Angle opposite side a', unit: 'degrees' },
      { symbol: 'b', name: 'Side b', unit: 'dimensionless' },
      { symbol: 'B', name: 'Angle opposite side b', unit: 'degrees' },
    ],
    keywords: ['law of sines', 'triangle', 'sine rule', 'oblique triangle'],
    solve: {
      a: (v) => (v.b * Math.sin(toRad(v.A))) / Math.sin(toRad(v.B)),
      b: (v) => (v.a * Math.sin(toRad(v.B))) / Math.sin(toRad(v.A)),
      A: (v) => {
        const s = (v.a * Math.sin(toRad(v.B))) / v.b;
        if (s < -1 || s > 1) throw new Error('No valid angle exists for these inputs.');
        return toDeg(Math.asin(s));
      },
      B: (v) => {
        const s = (v.b * Math.sin(toRad(v.A))) / v.a;
        if (s < -1 || s > 1) throw new Error('No valid angle exists for these inputs.');
        return toDeg(Math.asin(s));
      },
    },
  },
  {
    id: 'law-of-cosines',
    name: 'Law of Cosines',
    category: 'Mathematics',
    subcategory: 'Trigonometry',
    equation: 'c² = a² + b² − 2ab·cos(C)',
    description: 'Relates the three sides of a triangle to the angle opposite one of them. Angle is in degrees.',
    variables: [
      { symbol: 'c', name: 'Side c', unit: 'dimensionless' },
      { symbol: 'a', name: 'Side a', unit: 'dimensionless' },
      { symbol: 'b', name: 'Side b', unit: 'dimensionless' },
      { symbol: 'C', name: 'Angle opposite side c', unit: 'degrees' },
    ],
    keywords: ['law of cosines', 'triangle', 'cosine rule', 'oblique triangle'],
    solve: {
      c: (v) => {
        const val = v.a ** 2 + v.b ** 2 - 2 * v.a * v.b * Math.cos(toRad(v.C));
        if (val < 0) throw new Error('No real solution — check that the inputs form a valid triangle.');
        return Math.sqrt(val);
      },
      C: (v) => {
        const cosC = (v.a ** 2 + v.b ** 2 - v.c ** 2) / (2 * v.a * v.b);
        if (cosC < -1 || cosC > 1) throw new Error('These side lengths cannot form a triangle.');
        return toDeg(Math.acos(cosC));
      },
    },
  },
  {
    id: 'inverse-sine-arcsin',
    name: 'Inverse Sine (Arcsine)',
    category: 'Mathematics',
    subcategory: 'Trigonometry',
    equation: 'θ = sin⁻¹(x)',
    description: 'Finds the angle whose sine is x (principal value, in degrees).',
    variables: [
      { symbol: 'theta', name: 'Angle θ', unit: 'degrees' },
      { symbol: 'x', name: 'Ratio (opposite/hypotenuse)', unit: 'dimensionless' },
    ],
    keywords: ['arcsine', 'inverse sine', 'arcsin', 'solve for angle'],
    solve: {
      theta: (v) => {
        if (v.x < -1 || v.x > 1) throw new Error('x must be between −1 and 1 for arcsine to be defined.');
        return toDeg(Math.asin(v.x));
      },
      x: (v) => Math.sin(toRad(v.theta)),
    },
  },
  {
    id: 'inverse-cosine-arccos',
    name: 'Inverse Cosine (Arccosine)',
    category: 'Mathematics',
    subcategory: 'Trigonometry',
    equation: 'θ = cos⁻¹(x)',
    description: 'Finds the angle whose cosine is x (principal value, in degrees).',
    variables: [
      { symbol: 'theta', name: 'Angle θ', unit: 'degrees' },
      { symbol: 'x', name: 'Ratio (adjacent/hypotenuse)', unit: 'dimensionless' },
    ],
    keywords: ['arccosine', 'inverse cosine', 'arccos', 'solve for angle'],
    solve: {
      theta: (v) => {
        if (v.x < -1 || v.x > 1) throw new Error('x must be between −1 and 1 for arccosine to be defined.');
        return toDeg(Math.acos(v.x));
      },
      x: (v) => Math.cos(toRad(v.theta)),
    },
  },
  {
    id: 'inverse-tangent-arctan',
    name: 'Inverse Tangent (Arctangent)',
    category: 'Mathematics',
    subcategory: 'Trigonometry',
    equation: 'θ = tan⁻¹(x)',
    description: 'Finds the angle whose tangent is x (principal value, in degrees).',
    variables: [
      { symbol: 'theta', name: 'Angle θ', unit: 'degrees' },
      { symbol: 'x', name: 'Ratio (opposite/adjacent)', unit: 'dimensionless' },
    ],
    keywords: ['arctangent', 'inverse tangent', 'arctan', 'solve for angle'],
    solve: {
      theta: (v) => toDeg(Math.atan(v.x)),
      x: (v) => Math.tan(toRad(v.theta)),
    },
  },
  {
    id: 'degrees-radians-conversion',
    name: 'Degrees–Radians Conversion',
    category: 'Mathematics',
    subcategory: 'Trigonometry',
    equation: 'rad = deg × (π / 180)',
    description: 'Converts an angle between degrees and radians.',
    variables: [
      { symbol: 'rad', name: 'Angle in radians', unit: 'radians' },
      { symbol: 'deg', name: 'Angle in degrees', unit: 'degrees' },
    ],
    keywords: ['degrees to radians', 'radians to degrees', 'angle conversion', 'radian measure'],
    solve: {
      rad: (v) => toRad(v.deg),
      deg: (v) => toDeg(v.rad),
    },
  },
  {
    id: 'pythagorean-trig-identity',
    name: 'Pythagorean Identity',
    category: 'Mathematics',
    subcategory: 'Trigonometry',
    equation: 'sin²θ + cos²θ = 1',
    description: 'Fundamental trig identity relating the sine and cosine of the same angle (principal, non-negative root shown).',
    variables: [
      { symbol: 'sinTheta', name: 'sin(θ)', unit: 'dimensionless' },
      { symbol: 'cosTheta', name: 'cos(θ)', unit: 'dimensionless' },
    ],
    keywords: ['pythagorean identity', 'trig identity', 'sin squared cos squared', 'unit circle'],
    solve: {
      sinTheta: (v) => {
        if (v.cosTheta < -1 || v.cosTheta > 1) throw new Error('cos(θ) must be between −1 and 1.');
        return Math.sqrt(1 - v.cosTheta ** 2);
      },
      cosTheta: (v) => {
        if (v.sinTheta < -1 || v.sinTheta > 1) throw new Error('sin(θ) must be between −1 and 1.');
        return Math.sqrt(1 - v.sinTheta ** 2);
      },
    },
  },
];
