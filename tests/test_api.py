from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "online"


def test_prediction_endpoint():
    payload = {
        "area_sqft": 1400.0,
        "bedrooms": 3,
        "bathrooms": 3,
        "location": "Uttara",
    }
    response = client.post("/api/v1/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "estimated_price_bdt" in data
    assert data["estimated_price_bdt"] > 0
    assert "৳" in data["formatted_price"]