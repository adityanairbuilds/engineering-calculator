"""Engineering Calculator API — FastAPI backend.

Run with: uvicorn backend.main:app --reload
"""

import os
import sys
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

if __package__ in (None, ""):
    # Loaded as a bare top-level module (Vercel service: root=backend, entrypoint
    # main:app) instead of as `backend.main` (local dev: `uvicorn backend.main:app`
    # from the repo root). Every submodule below uses imports relative to the
    # `backend` package, so put the repo root on sys.path and import the same way
    # local dev does, rather than special-casing every submodule.
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from backend.routes import calculate, formulas
else:
    from .routes import calculate, formulas

# Comma-separated list of allowed frontend origins. Defaults to the Vite
# dev server; set FRONTEND_ORIGINS in production instead of widening this.
_origins = [origin.strip() for origin in os.environ.get("FRONTEND_ORIGINS", "http://localhost:5173").split(",")]

app = FastAPI(title="Engineering Calculator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=_origins,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(formulas.router)
app.include_router(calculate.router)


@app.get("/api/health")
def health() -> dict[str, bool]:
    return {"ok": True}
