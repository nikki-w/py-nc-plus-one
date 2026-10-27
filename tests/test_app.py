import os
import pytest

from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture()
def client():
    return TestClient(app)

def test_get_events_responds_with_200(client):
    response = client.get("/events")

    assert response.status_code == 200

def test_get_events_responds_with_list_on_key_of_events(client):
    events = client.get("/events").json()["events"]

    assert isinstance(events, list)