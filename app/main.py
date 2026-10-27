from fastapi import FastAPI
from src.connection import get_connection
from src.seed_functions import seed
# from app.routes.events import events_router

app = FastAPI()

# app.include_router(events_router)

@app.get("/events", status_code=200)
def get_events():
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM events;")
        columns = [desc[0] for desc in cur.description]
        rows = cur.fetchall()
    conn.close()
    return {"events": [dict(zip(columns, row)) for row in rows]}


if __name__ == "__main__":
    conn = get_connection()
    seed(conn)