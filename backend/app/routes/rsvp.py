import jwt
import os
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer
from datetime import datetime, timezone, timedelta
from pydantic import BaseModel
from backend.app.security import check_access_token
from backend.src.passwords import verify_password

rsvp_router = APIRouter("/events/{id}/rsvp")

@rsvp_router.post("/", status_code=201, dependencies=[Depends(check_access_token)])
def rsvp_event(event_id: int, user_id: int):
    pass


{
  "rsvp": {
    "id": 55,
    "attendee_id": 1,
    "event_id": 12,
    "created_at": "2025-06-01T11:00:00Z"
  }
}