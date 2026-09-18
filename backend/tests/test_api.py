from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_health():
    res = client.get("/api/health")
    assert res.status_code == 200
    assert res.json() == {"ok": True}


def test_list_formulas():
    res = client.get("/api/formulas")
    assert res.status_code == 200
    body = res.json()
    assert len(body) > 100  # the real registry has hundreds of formulas
    assert {"id", "name", "category", "solve_targets"} <= body[0].keys()


def test_list_formulas_filtered_by_category():
    res = client.get("/api/formulas", params={"category": "Mathematics"})
    assert res.status_code == 200
    body = res.json()
    assert len(body) > 0
    assert all(f["category"] == "Mathematics" for f in body)


def test_get_formula_by_id():
    res = client.get("/api/formulas/quadratic-formula")
    assert res.status_code == 200
    assert res.json()["id"] == "quadratic-formula"


def test_get_formula_404():
    res = client.get("/api/formulas/does-not-exist")
    assert res.status_code == 404
    assert "does-not-exist" in res.json()["detail"]


def test_search_finds_by_equation():
    res = client.get("/api/search", params={"q": "F=ma"})
    assert res.status_code == 200
    ids = [f["id"] for f in res.json()]
    assert "newtons-second-law" in ids


def test_search_empty_query_returns_nothing():
    res = client.get("/api/search", params={"q": ""})
    assert res.status_code == 200
    assert res.json() == []


def test_calculate_success():
    res = client.post("/api/calculate/quadratic-formula", json={"target": "x", "values": {"a": 1, "b": -3, "c": 2}})
    assert res.status_code == 200
    assert res.json()["value"] == 2.0


def test_calculate_domain_error_returns_400():
    res = client.post("/api/calculate/quadratic-formula", json={"target": "x", "values": {"a": 0, "b": -3, "c": 2}})
    assert res.status_code == 400
    assert "quadratic" in res.json()["detail"].lower()


def test_calculate_missing_values_returns_400():
    res = client.post("/api/calculate/quadratic-formula", json={"target": "x", "values": {"a": 1}})
    assert res.status_code == 400


def test_calculate_rejects_absurdly_large_factorial_input():
    # Regression test: factorial used to have no upper bound, so a huge n
    # would hang the server computing it instead of failing fast.
    res = client.post("/api/calculate/permutations", json={"target": "Pnr", "values": {"n": 1e300, "r": 2}})
    assert res.status_code == 400


def test_calculate_unknown_formula_returns_404():
    res = client.post("/api/calculate/does-not-exist", json={"target": "x", "values": {}})
    assert res.status_code == 404


def test_calculate_bad_request_body_returns_422():
    res = client.post("/api/calculate/quadratic-formula", json={"target": "x", "values": {"a": "not-a-number"}})
    assert res.status_code == 422
