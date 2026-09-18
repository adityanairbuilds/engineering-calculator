# Engineering Calculator

A full-stack student project that puts hundreds of useful math, physics, and engineering formulas
in one searchable place, plus a basic calculator, to help with homework and studying.

- **Search** — type a concept ("velocity", "Ohm's law", "F=ma") and it matches formula names,
  equations, keywords, and variables.
- **Formula Library** — browse and filter every formula by category/subcategory.
- **Calculators** — pick a formula, choose which variable to solve for, enter the rest, and get
  a live result computed by the backend.

## Stack

- **Frontend** — React 19 + TypeScript + Vite, no CSS framework.
- **Backend** — Python + FastAPI. Python is the source of truth for formula data and does the
  actual math: every formula's solve logic, input validation, and search/filter ranking run
  server-side; the frontend only renders what the API returns.

## How it fits together

The frontend never computes a formula result itself — it calls the API:

| Endpoint | What it does |
|---|---|
| `GET /api/formulas` | List formulas, optionally filtered by `category`/`subcategory` |
| `GET /api/formulas/{id}` | One formula's metadata (variables, units, which symbols it can solve for) |
| `GET /api/search?q=...` | Ranked search across name, equation, keywords, category, and variable names |
| `POST /api/calculate/{id}` | `{ target, values }` in → the computed value out, or a 400 with a plain-English error (division by zero, no real solution, non-integer factorial, ...) |

Backend code lives under `backend/`:

```
backend/
  main.py            FastAPI app + CORS
  routes/             API endpoints (formulas, calculate)
  services/           formula lookup/filtering, search ranking, the solve() runner
  models/             internal Formula/Variable dataclasses
  schemas/             Pydantic request/response models
  calculations/        the formula data itself — one module per subject
    mathematics/       algebra, geometry, trigonometry, precalculus, calculus, statistics
    physics/            kinematics, dynamics, circuits, waves, thermodynamics, ...
    engineering/        statics, materials, structural, electrical, fluid mechanics, aerospace, ...
  tests/               pytest suite (solver, search, and API integration tests)
```

Each formula is a small Python object: its equation, its variables (with units), and a `solve`
dict mapping each solvable variable to a plain function of the others. A formula that's only
useful as a reference (e.g. ΣF = 0) has an empty `solve` dict and the frontend shows it read-only.

The frontend's API layer lives under `src/api/` (`formulas.ts`, `calculate.ts`) — every fetch call
goes through there, not scattered across components.

## Running it locally

**Backend:**

```
cd "World Engineering Calculator"
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
uvicorn backend.main:app --reload --port 8000
```

**Frontend** (separate terminal):

```
npm install
npm run dev
```

Or run both together: `./dev.sh` (after the one-time setup above).

The frontend expects the API at `http://localhost:8000` by default — set `VITE_API_BASE_URL` to
point elsewhere (see `.env.example`). The backend allows requests from `http://localhost:5173` by
default — set `FRONTEND_ORIGINS` for a different origin (see `backend/.env.example`).

## Tests

```
pip install -r backend/requirements-dev.txt
PYTHONPATH=. pytest backend/tests -q
```

## Disclaimer

This is an educational tool. Verify results independently before relying on them for
professional or safety-critical engineering work.
