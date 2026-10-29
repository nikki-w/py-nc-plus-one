from fastapi.exceptions import HTTPException
from src.connection import get_connection


def get_all_events() -> dict:
    """Returns all events."""
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM events;")
        columns = [desc[0] for desc in cur.description]
        rows = cur.fetchall()
    conn.close()
    return {"events": [dict(zip(columns, row)) for row in rows]}


def get_event_from_id(event_id: int) -> dict:
    """Returns an event given an event id."""
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("""
                    SELECT e.id, e.title, e.description, e.starts_at, e.ends_at, v.name AS location, v.address, v.capacity, e.created_at
                    FROM events AS e
                    JOIN venues AS v
                        ON e.venue_id = v.id
                    WHERE e.id = %s;
                    """, (event_id,))

        columns = [desc[0] for desc in cur.description]
        row = cur.fetchone()
    conn.close()

    if row:
        return {"event": dict(zip(columns, row))}
    return None
