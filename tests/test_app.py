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

def test_get_event_from_id_responds_with_201_for_existing_event(client):
    response = client.get("/events/2")

    assert response.status_code == 201

def test_get_event_from_id_responds_with_404_for_event_not_found(client):
    response = client.get("/events/999")

    assert response.status_code == 404

def test_get_event_from_id_responds_with_400_for_invalid_value_in_id(client):
    response = client.get("/events/-3")

    assert response.status_code == 400

def test_get_event_from_id_gives_correct_response_from_valid_id(client):
    response = client.get("/events/2")

    expected_output = {
            "event": {
                "id": 2,
                "title": "Intro to Machine Learning Workshop",
                "description": "Hands-on workshop covering perceptrons, neural networks, and classifiers using NumPy and PyTorch.",
                "starts_at": "2026-06-25T10:00:00+01:00",
                "ends_at": "2026-06-25T13:00:00+01:00",
                "location": "Online – Zoom",
                "address": None,
                "capacity": 500,
                "created_at": "2026-10-22T09:41:27.968806+01:00"
            }
            }

    assert response.json() == expected_output