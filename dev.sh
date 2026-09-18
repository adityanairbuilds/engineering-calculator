#!/usr/bin/env bash
# Runs the FastAPI backend and the Vite dev server together.
# Ctrl+C stops both. First-time setup (venv, npm install) is not done here —
# see README.md.
set -e
cd "$(dirname "$0")"

source .venv/bin/activate
uvicorn backend.main:app --reload --port 8000 &
BACKEND_PID=$!
trap "kill $BACKEND_PID" EXIT

npm run dev
