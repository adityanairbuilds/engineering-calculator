from fastapi import APIRouter, HTTPException, Query

from ..schemas.formula import FormulaOut
from ..services import formula_service, search_service

router = APIRouter(prefix="/api", tags=["formulas"])


@router.get("/formulas")
def list_formulas(
    category: str | None = None,
    subcategory: str | None = None,
) -> list[FormulaOut]:
    formulas = formula_service.filter_by_category(formula_service.get_all(), category, subcategory)
    return [formula_service.to_formula_out(f) for f in formulas]


@router.get("/formulas/{formula_id}")
def get_formula(formula_id: str) -> FormulaOut:
    formula = formula_service.get_by_id(formula_id)
    if formula is None:
        raise HTTPException(status_code=404, detail=f'No formula with id "{formula_id}".')
    return formula_service.to_formula_out(formula)


@router.get("/search")
def search(
    q: str = Query("", description="Search text — matches name, equation, keywords, category, variables."),
    category: str | None = None,
    subcategory: str | None = None,
) -> list[FormulaOut]:
    results = search_service.search_formulas(formula_service.get_all(), q)
    results = formula_service.filter_by_category(results, category, subcategory)
    return [formula_service.to_formula_out(f) for f in results]
