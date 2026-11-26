import psycopg2
from backend.src.connection import get_connection
from fastapi.exceptions import HTTPException

def get_rsvps_by_event(event_id: int) -> dict:
    """Returns all RSVPs for a given event."""
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT 
                r.id AS rsvp_id,
                u.id AS user_id,
                u.name AS attendee_name,
                u.email AS attendee_email,
                e.id AS event_id,
                e.title AS event_title,
                e.starts_at
            FROM rsvps AS r
            JOIN users AS u ON r.attendee_id = u.id
            JOIN events AS e ON r.event_id = e.id
            WHERE r.event_id = %s
            ORDER BY r.id
            """,
            (event_id,),
        )
        columns = [desc[0] for desc in cur.description]
        rows = cur.fetchall()

    conn.close()

    return {"rsvp": [dict(zip(columns, row)) for row in rows]}


def create_rsvp(event_id: int, attendee_id: int) -> dict:
    """Creates an RSVP for an authenticated user and returns the new record."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            # Check if the user has already RSVP'd and if so, raise an error.
            cur.execute(
                """
                SELECT id 
                FROM rsvps
                WHERE event_id = %s AND attendee_id = %s;
                """,
                (event_id, attendee_id),
            )
            if cur.fetchone() is not None:
                raise HTTPException(
                    status_code=409,
                    detail="User has already RSVP'd to this event",
                )
        
            # If they havent then allow them to RSVP to the event.
            cur.execute(
                """
                INSERT INTO rsvps 
                    (event_id, attendee_id)
                VALUES 
                    (%s, %s)
                RETURNING id, attendee_id, event_id, created_at;
                """,
                (event_id, attendee_id),
            )
            columns = [desc[0] for desc in cur.description]
            row = cur.fetchone()
            conn.commit()

    except psycopg2.errors.ForeignKeyViolation:
        # Cancel any changes if the event can't be found in the db.
        conn.rollback()
        raise HTTPException(status_code=404, detail="Event not found")
    
    finally:
        conn.close()

    return {"rsvp": dict(zip(columns, row))}