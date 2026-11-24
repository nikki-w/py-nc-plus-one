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


