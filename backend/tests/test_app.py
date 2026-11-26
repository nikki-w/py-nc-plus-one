from datetime import datetime
from datetime import datetime, timezone

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

def test_get_event_from_id_returns_the_matching_event(client):
    expected =   {
        'id': 1,
        'title': 'Leeds Tech Meetup – June Edition',
        'description': 'Monthly meetup for Leeds-based developers. Lightning talks and '
        'networking.',
        'starts_at': '2026-06-18T18:30:00+01:00',
        'ends_at': '2026-06-18T21:00:00+01:00',
        'location': 'Nexus, University of Leeds',
        'address': 'Discovery Way, Leeds, LS2 3AA',
        'capacity': 200,
        'created_at': datetime.now(timezone.utc).isoformat(),
    }


    event = client.get(f"/events/{expected["id"]}").json()["event"]

    # As there's a delay with the datetime module in pytest, pop out the created_at value and test this seperately
    actual_created_at = event.pop("created_at", None)
    expected.pop("created_at")

    assert event == expected

    # Tests for created_at
    assert actual_created_at is not None
    assert datetime.fromisoformat(actual_created_at)


def get_auth_headers(client):
    """Registers and logs in a test user, returning valid Bearer headers."""
    test_user = {
        "name": "Test User",
        "email": "testuser@example.com",
        "password": "password123",
    }
    client.post("/auth/register", json=test_user)

    response = client.post(
        "/auth/login",
        json={"email": test_user["email"], "password": test_user["password"]},
    )
    assert response.status_code == 200, f"Login failed: {response.json()}"

    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_post_rsvp_success(client):
    headers = get_auth_headers(client)
    response = client.post("/events/1/rsvp/", headers=headers)

    assert response.status_code == 201
    data = response.json()["rsvp"]
    assert data["event_id"] == 1
    assert "id" in data
    assert "attendee_id" in data
    assert "created_at" in data


def test_post_rsvp_duplicate_returns_409(client):
    headers = get_auth_headers(client)
    client.post("/events/2/rsvp/", headers=headers)
    response = client.post("/events/2/rsvp/", headers=headers)

    assert response.status_code == 409
    assert response.json()["detail"] == "User has already RSVP'd to this event"


def test_post_rsvp_unauthenticated_returns_401(client):
    response = client.post("/events/1/rsvp/")
    assert response.status_code in (401, 403)


def test_post_rsvp_nonexistent_event_returns_404(client):
    headers = get_auth_headers(client)
    response = client.post("/events/99999/rsvp/", headers=headers)
    assert response.status_code == 404

