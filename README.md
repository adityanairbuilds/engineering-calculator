# Engineering Calculator

A student project that puts hundreds of useful math, physics, and engineering formulas in one
searchable place, plus a basic calculator, to help with homework and studying.

- **Search** — type a concept ("velocity", "Ohm's law", "F=ma") and it matches formula names,
  equations, keywords, and variables.
- **Formula Library** — browse and filter every formula by category/subcategory.
- **Calculators** — pick a formula, choose which variable to solve for, and enter the rest.

## Stack

React 19 + TypeScript + Vite, no backend, no CSS framework. Formula data lives under
`src/data/formulas/<domain>/<subcategory>.ts`; each formula carries a small hand-written `solve`
closure per variable it can be solved for (see `src/types/index.ts`).

## Development

```
npm install
npm run dev      # start the dev server
npm run build    # type-check + production build
npm run lint     # oxlint
```

## Disclaimer

This is an educational tool. Verify results independently before relying on them for
professional or safety-critical engineering work.
