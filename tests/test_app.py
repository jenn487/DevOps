import json
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.app import app

def test_root_returns_hola_mundo():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Hola Mundo" in resp.data
