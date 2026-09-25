from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_automation():
    response = client.post("/automate", json={"task": "summarize this project for me"})
    assert response.status_code == 200
    assert response.json()["intent"] == "summarize"
