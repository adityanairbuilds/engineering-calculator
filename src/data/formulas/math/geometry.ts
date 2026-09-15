import type { Formula } from '../../../types';

export const geometryFormulas: Formula[] = [
  {
    id: 'circle-area',
    name: 'Area of a Circle',
    category: 'Mathematics',
    subcategory: 'Geometry',
    equation: 'A = πr²',
    description: 'Calculates the area of a circle from its radius.',
    variables: [
      { symbol: 'A', name: 'Area', unit: 'dimensionless' },
      { symbol: 'r', name: 'Radius', unit: 'dimensionless' },
    ],
    keywords: ['circle', 'area', 'radius'],
    solve: {
      A: (v) => Math.PI * v.r ** 2,
      r: (v) => Math.sqrt(v.A / Math.PI),
    },
  },
  {
    id: 'circle-circumference',
    name: 'Circumference of a Circle',
    category: 'Mathematics',
    subcategory: 'Geometry',
    equation: 'C = 2πr',
    description: 'Calculates the circumference of a circle from its radius.',
    variables: [
      { symbol: 'C', name: 'Circumference', unit: 'dimensionless' },
      { symbol: 'r', name: 'Radius', unit: 'dimensionless' },
    ],
    keywords: ['circle', 'circumference', 'perimeter'],
    solve: {
      C: (v) => 2 * Math.PI * v.r,
      r: (v) => v.C / (2 * Math.PI),
    },
  },
  {
    id: 'triangle-area',
    name: 'Area of a Triangle',
    category: 'Mathematics',
    subcategory: 'Geometry',
    equation: 'A = ½bh',
    description: 'Calculates the area of a triangle from its base and height.',
    variables: [
      { symbol: 'A', name: 'Area', unit: 'dimensionless' },
      { symbol: 'b', name: 'Base', unit: 'dimensionless' },
      { symbol: 'h', name: 'Height', unit: 'dimensionless' },
    ],
    keywords: ['triangle', 'area', 'base', 'height'],
    solve: {
      A: (v) => 0.5 * v.b * v.h,
      b: (v) => (2 * v.A) / v.h,
      h: (v) => (2 * v.A) / v.b,
    },
  },
  {
    id: 'rectangle-area',
    name: 'Area of a Rectangle',
    category: 'Mathematics',
    subcategory: 'Geometry',
    equation: 'A = lw',
    description: 'Calculates the area of a rectangle from its length and width.',
    variables: [
      { symbol: 'A', name: 'Area', unit: 'dimensionless' },
      { symbol: 'l', name: 'Length', unit: 'dimensionless' },
      { symbol: 'w', name: 'Width', unit: 'dimensionless' },
    ],
    keywords: ['rectangle', 'area', 'length', 'width'],
    solve: {
      A: (v) => v.l * v.w,
      l: (v) => v.A / v.w,
      w: (v) => v.A / v.l,
    },
  },
  {
    id: 'sphere-volume',
    name: 'Volume of a Sphere',
    category: 'Mathematics',
    subcategory: 'Geometry',
    equation: 'V = (4/3)πr³',
    description: 'Calculates the volume of a sphere from its radius.',
    variables: [
      { symbol: 'V', name: 'Volume', unit: 'dimensionless' },
      { symbol: 'r', name: 'Radius', unit: 'dimensionless' },
    ],
    keywords: ['sphere', 'volume', 'radius'],
    solve: {
      V: (v) => (4 / 3) * Math.PI * v.r ** 3,
      r: (v) => Math.cbrt((3 * v.V) / (4 * Math.PI)),
    },
  },
  {
    id: 'pythagorean-theorem',
    name: 'Pythagorean Theorem',
    category: 'Mathematics',
    subcategory: 'Geometry',
    equation: 'c = √(a² + b²)',
    description: 'Finds the hypotenuse of a right triangle from its two legs.',
    variables: [
      { symbol: 'c', name: 'Hypotenuse', unit: 'dimensionless' },
      { symbol: 'a', name: 'Leg a', unit: 'dimensionless' },
      { symbol: 'b', name: 'Leg b', unit: 'dimensionless' },
    ],
    keywords: ['pythagorean theorem', 'right triangle', 'hypotenuse'],
    solve: {
      c: (v) => Math.sqrt(v.a ** 2 + v.b ** 2),
      a: (v) => {
        if (v.c <= v.b) throw new Error('The hypotenuse must be longer than leg b.');
        return Math.sqrt(v.c ** 2 - v.b ** 2);
      },
      b: (v) => {
        if (v.c <= v.a) throw new Error('The hypotenuse must be longer than leg a.');
        return Math.sqrt(v.c ** 2 - v.a ** 2);
      },
    },
  },
  {
    id: 'sphere-surface-area',
    name: 'Surface Area of a Sphere',
    category: 'Mathematics',
    subcategory: 'Geometry',
    equation: 'A = 4πr²',
    description: 'Calculates the surface area of a sphere from its radius.',
    variables: [
      { symbol: 'A', name: 'Surface area', unit: 'dimensionless' },
      { symbol: 'r', name: 'Radius', unit: 'dimensionless' },
    ],
    keywords: ['sphere', 'surface area', 'radius'],
    solve: {
      A: (v) => 4 * Math.PI * v.r ** 2,
      r: (v) => Math.sqrt(v.A / (4 * Math.PI)),
    },
  },
  {
    id: 'cylinder-volume',
    name: 'Volume of a Cylinder',
    category: 'Mathematics',
    subcategory: 'Geometry',
    equation: 'V = πr²h',
    description: 'Calculates the volume of a cylinder from its radius and height.',
    variables: [
      { symbol: 'V', name: 'Volume', unit: 'dimensionless' },
      { symbol: 'r', name: 'Radius', unit: 'dimensionless' },
      { symbol: 'h', name: 'Height', unit: 'dimensionless' },
    ],
    keywords: ['cylinder', 'volume', 'radius', 'height'],
    solve: {
      V: (v) => Math.PI * v.r ** 2 * v.h,
      r: (v) => Math.sqrt(v.V / (Math.PI * v.h)),
      h: (v) => v.V / (Math.PI * v.r ** 2),
    },
  },
  {
    id: 'cone-volume',
    name: 'Volume of a Cone',
    category: 'Mathematics',
    subcategory: 'Geometry',
    equation: 'V = (1/3)πr²h',
    description: 'Calculates the volume of a cone from its radius and height.',
    variables: [
      { symbol: 'V', name: 'Volume', unit: 'dimensionless' },
      { symbol: 'r', name: 'Radius', unit: 'dimensionless' },
      { symbol: 'h', name: 'Height', unit: 'dimensionless' },
    ],
    keywords: ['cone', 'volume', 'radius', 'height'],
    solve: {
      V: (v) => (1 / 3) * Math.PI * v.r ** 2 * v.h,
      r: (v) => Math.sqrt((3 * v.V) / (Math.PI * v.h)),
      h: (v) => (3 * v.V) / (Math.PI * v.r ** 2),
    },
  },
  {
    id: 'rectangle-perimeter',
    name: 'Perimeter of a Rectangle',
    category: 'Mathematics',
    subcategory: 'Geometry',
    equation: 'P = 2(l + w)',
    description: 'Calculates the perimeter of a rectangle from its length and width.',
    variables: [
      { symbol: 'P', name: 'Perimeter', unit: 'dimensionless' },
      { symbol: 'l', name: 'Length', unit: 'dimensionless' },
      { symbol: 'w', name: 'Width', unit: 'dimensionless' },
    ],
    keywords: ['rectangle', 'perimeter', 'length', 'width'],
    solve: {
      P: (v) => 2 * (v.l + v.w),
      l: (v) => v.P / 2 - v.w,
      w: (v) => v.P / 2 - v.l,
    },
  },
  {
    id: 'trapezoid-area',
    name: 'Area of a Trapezoid',
    category: 'Mathematics',
    subcategory: 'Geometry',
    equation: 'A = ½(b₁ + b₂)h',
    description: 'Calculates the area of a trapezoid from its two parallel bases and height.',
    variables: [
      { symbol: 'A', name: 'Area', unit: 'dimensionless' },
      { symbol: 'b1', name: 'Base 1', unit: 'dimensionless' },
      { symbol: 'b2', name: 'Base 2', unit: 'dimensionless' },
      { symbol: 'h', name: 'Height', unit: 'dimensionless' },
    ],
    keywords: ['trapezoid', 'area', 'bases', 'height'],
    solve: {
      A: (v) => 0.5 * (v.b1 + v.b2) * v.h,
      h: (v) => (2 * v.A) / (v.b1 + v.b2),
      b1: (v) => (2 * v.A) / v.h - v.b2,
      b2: (v) => (2 * v.A) / v.h - v.b1,
    },
  },
  {
    id: 'regular-polygon-area',
    name: 'Area of a Regular Polygon',
    category: 'Mathematics',
    subcategory: 'Geometry',
    equation: 'A = ¼ n s² cot(π/n)',
    description: 'Calculates the area of a regular polygon from its number of sides and side length.',
    variables: [
      { symbol: 'A', name: 'Area', unit: 'dimensionless' },
      { symbol: 'n', name: 'Number of sides', unit: 'dimensionless' },
      { symbol: 's', name: 'Side length', unit: 'dimensionless' },
    ],
    keywords: ['regular polygon', 'polygon area', 'n-gon', 'hexagon', 'pentagon'],
    solve: {
      A: (v) => {
        if (v.n < 3) throw new Error('A polygon must have at least 3 sides.');
        return 0.25 * v.n * v.s ** 2 * (1 / Math.tan(Math.PI / v.n));
      },
      s: (v) => {
        if (v.n < 3) throw new Error('A polygon must have at least 3 sides.');
        return Math.sqrt((4 * v.A) / (v.n * (1 / Math.tan(Math.PI / v.n))));
      },
    },
  },
  {
    id: 'cylinder-surface-area',
    name: 'Surface Area of a Cylinder',
    category: 'Mathematics',
    subcategory: 'Geometry',
    equation: 'SA = 2πr² + 2πrh',
    description: 'Calculates the total surface area of a cylinder (including both circular ends).',
    variables: [
      { symbol: 'SA', name: 'Surface area', unit: 'dimensionless' },
      { symbol: 'r', name: 'Radius', unit: 'dimensionless' },
      { symbol: 'h', name: 'Height', unit: 'dimensionless' },
    ],
    keywords: ['cylinder', 'surface area', 'radius', 'height'],
    solve: {
      SA: (v) => 2 * Math.PI * v.r ** 2 + 2 * Math.PI * v.r * v.h,
      h: (v) => v.SA / (2 * Math.PI * v.r) - v.r,
      r: (v) => {
        const a = 2 * Math.PI;
        const b = 2 * Math.PI * v.h;
        const c = -v.SA;
        const disc = b ** 2 - 4 * a * c;
        if (disc < 0) throw new Error('No real solution for these inputs.');
        return (-b + Math.sqrt(disc)) / (2 * a);
      },
    },
  },
  {
    id: 'cone-surface-area',
    name: 'Surface Area of a Cone',
    category: 'Mathematics',
    subcategory: 'Geometry',
    equation: 'SA = πr² + πrl',
    description: 'Calculates the total surface area of a cone from its radius and slant height l.',
    variables: [
      { symbol: 'SA', name: 'Surface area', unit: 'dimensionless' },
      { symbol: 'r', name: 'Radius', unit: 'dimensionless' },
      { symbol: 'l', name: 'Slant height', unit: 'dimensionless' },
    ],
    keywords: ['cone', 'surface area', 'radius', 'slant height'],
    solve: {
      SA: (v) => Math.PI * v.r ** 2 + Math.PI * v.r * v.l,
      l: (v) => (v.SA - Math.PI * v.r ** 2) / (Math.PI * v.r),
      r: (v) => {
        const a = Math.PI;
        const b = Math.PI * v.l;
        const c = -v.SA;
        const disc = b ** 2 - 4 * a * c;
        if (disc < 0) throw new Error('No real solution for these inputs.');
        return (-b + Math.sqrt(disc)) / (2 * a);
      },
    },
  },
];
