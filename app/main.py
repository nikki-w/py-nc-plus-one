from fastapi import FastAPI
from src.connection import get_connection
from src.seed_functions import seed
from starlette.exceptions import HTTPException

app = FastAPI()


@app.get("/events", status_code=200)
def get_events():
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM events;")
        columns = [desc[0] for desc in cur.description]
        rows = cur.fetchall()
    conn.close()
    return {"events": [dict(zip(columns, row)) for row in rows]}


@app.get("/events/{event_id}", status_code=201)
def get_event_from_id(event_id: int):
    conn = get_connection()
    with conn.cursor() as cur:

        # Raise exception if the integer isn't valid before attempting to to execute
        if event_id < 1:
            raise HTTPException(status_code=400, detail="Id is not a valid integer.")

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

    # If an event isn't found then return a 404 error
    if row is None:
        raise HTTPException(status_code=404, detail="Event not found")

    return {"event": dict(zip(columns, row))}


if __name__ == "__main__":
    conn = get_connection()
    seed(conn)