from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models.events import get_all_events, get_event_from_id

events_router = APIRouter(prefix="/events")


@events_router.get("/", status_code=200)
def get_events():
    return get_all_events()


@events_router.get("/{event_id}", status_code=201)
def get_event(event_id: int):
    
    if event_id < 1:
         raise HTTPException(
            status_code=400, 
            detail="Id is not a valid integer."
        ) 

    event = get_event_from_id(event_id)

    if event is None:
         raise HTTPException(
            status_code=404, 
            detail="Event not found."
        ) 

    return event