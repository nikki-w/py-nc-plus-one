from fastapi import FastAPI
from src.connection import get_connection
from src.seed_functions import seed
from starlette.exceptions import HTTPException
from app.routes.auth import auth_router
from app.routes.events import events_router

app = FastAPI(title="Booking API")


app.include_router(auth_router)
app.include_router(events_router)


if __name__ == "__main__":
    conn = get_connection()
    seed(conn)
