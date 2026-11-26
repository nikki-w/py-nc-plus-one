from fastapi import FastAPI
from backend.src.connection import get_connection
from backend.src.seed_functions import seed
from starlette.exceptions import HTTPException
from backend.app.routes.auth import auth_router
from backend.app.routes.events import events_router
from backend.app.routes.rsvp import rsvp_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Booking API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(events_router)
app.include_router(rsvp_router)


if __name__ == "__main__":
    conn = get_connection()
    seed(conn)
