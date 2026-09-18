from ..calculations.registry import ALL_FORMULAS
from ..models.formula import Formula
from ..schemas.formula import FormulaOut, VariableOut

_BY_ID = {f.id: f for f in ALL_FORMULAS}


def get_all() -> list[Formula]:
    return ALL_FORMULAS


def get_by_id(formula_id: str) -> Formula | None:
    return _BY_ID.get(formula_id)


def filter_by_category(formulas: list[Formula], category: str | None, subcategory: str | None) -> list[Formula]:
    return [
        f
        for f in formulas
        if (category is None or f.category == category) and (subcategory is None or f.subcategory == subcategory)
    ]


def to_formula_out(formula: Formula) -> FormulaOut:
    return FormulaOut(
        id=formula.id,
        name=formula.name,
        category=formula.category,
        subcategory=formula.subcategory,
        equation=formula.equation,
        description=formula.description,
        variables=[VariableOut(symbol=v.symbol, name=v.name, unit=v.unit) for v in formula.variables],
        keywords=formula.keywords,
        solve_targets=list(formula.solve.keys()),
    )
