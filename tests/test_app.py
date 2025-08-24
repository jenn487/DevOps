import json
from app.app import app

def test_root_returns_hola_mundo():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert "Hola Mundo" in data.get("message", "")
