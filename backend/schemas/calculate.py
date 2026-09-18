from pydantic import BaseModel


class CalculateRequest(BaseModel):
    target: str
    values: dict[str, float] = {}


class CalculateResponse(BaseModel):
    value: float
