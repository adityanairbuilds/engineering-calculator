"""Ranked formula search — name, keywords, equation, category, and variable
name matching, with multi-word queries also scored token-by-token so
"electric resistance" still finds Ohm's Law (keyword "resistance")."""

import re

from ..models.formula import Formula

_NON_EQUATION_CHARS = re.compile(r"[^a-z0-9=]")


def _normalize_equation(s: str) -> str:
    return _NON_EQUATION_CHARS.sub("", s.lower())


def _normalize_text(s: str) -> str:
    return s.lower().strip()


def _score_formula(formula: Formula, query: str, normalized_equation_query: str) -> int:
    name = _normalize_text(formula.name)
    category = _normalize_text(formula.category)
    subcategory = _normalize_text(formula.subcategory)
    score = 0

    if name == query:
        score += 100
    elif name.startswith(query):
        score += 60
    elif query in name:
        score += 40

    for keyword in formula.keywords:
        k = _normalize_text(keyword)
        if k == query:
            score += 70
        elif query in k:
            score += 25

    if len(normalized_equation_query) > 1 and normalized_equation_query in _normalize_equation(formula.equation):
        score += 50

    if query in category:
        score += 15
    if query in subcategory:
        score += 15

    for variable in formula.variables:
        if query in _normalize_text(variable.name):
            score += 10

    tokens = [t for t in query.split() if len(t) > 2]
    if len(tokens) > 1:
        for token in tokens:
            if token in name:
                score += 5
            if any(token in _normalize_text(k) for k in formula.keywords):
                score += 8

    return score


def search_formulas(formulas: list[Formula], raw_query: str) -> list[Formula]:
    query = _normalize_text(raw_query)
    if not query:
        return []

    normalized_equation_query = _normalize_equation(raw_query)

    scored = [(f, _score_formula(f, query, normalized_equation_query)) for f in formulas]
    scored = [(f, s) for f, s in scored if s > 0]
    scored.sort(key=lambda pair: pair[1], reverse=True)
    return [f for f, _ in scored]
