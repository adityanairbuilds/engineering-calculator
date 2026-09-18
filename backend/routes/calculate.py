from fastapi import APIRouter, HTTPException

from ..schemas.calculate import CalculateRequest, CalculateResponse
from ..services import formula_service, solver_service

router = APIRouter(prefix="/api", tags=["calculate"])


@router.post("/calculate/{formula_id}")
def calculate(formula_id: str, body: CalculateRequest) -> CalculateResponse:
    formula = formula_service.get_by_id(formula_id)
    if formula is None:
        raise HTTPException(status_code=404, detail=f'No formula with id "{formula_id}".')

    try:
        value = solver_service.solve(formula, body.target, body.values)
    except solver_service.SolveError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return CalculateResponse(value=value)
