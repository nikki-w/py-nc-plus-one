import jwt
import os
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer
from datetime import datetime, timezone, timedelta
from pydantic import BaseModel
from backend.app.security import check_access_token
from backend.src.passwords import verify_password
from backend.app.models.rsvp import get_rsvps_by_event, create_rsvp

rsvp_router = APIRouter(prefix="/events/{id}/rsvp")

@rsvp_router.get("/", status_code=200)
def get_rsvps(id: int):
    return get_rsvps_by_event(id)


@rsvp_router.post("/", status_code=201)
def post_rsvp(id: int, user_id: int = Depends(check_access_token)):
    return create_rsvp(event_id=id, attendee_id=user_id)

