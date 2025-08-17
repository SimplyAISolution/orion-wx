from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_health():
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json()['status'] == 'ok'

def test_forecast():
    r = client.post('/forecast', json={"lat": 40.0, "lon": -105.0, "lead_hours": 12, "variable": "precip"})
    assert r.status_code == 200
    body = r.json()
    assert 'quantiles' in body
    assert 'event_probs' in body
