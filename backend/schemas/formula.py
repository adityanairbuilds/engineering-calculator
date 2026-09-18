from pydantic import BaseModel


class VariableOut(BaseModel):
    symbol: str
    name: str
    unit: str


class FormulaOut(BaseModel):
    id: str
    name: str
    category: str
    subcategory: str
    equation: str
    description: str
    variables: list[VariableOut]
    keywords: list[str]
    solve_targets: list[str]
