from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/events", tags=["events"])

# Current active event dictionary in memory
CURRENT_EVENT = {
    "event_id": "divafuyu1",
    "event_name": "Imprisoned Marinett",
    "bundle_url": "https://nss-47ky.onrender.com/assets/asset.bundle_divafuyu1.zip",
    "is_active": True
}

# Pydantic model defines what fields can be edited in /docs
class EventUpdate(BaseModel):
    event_id: str
    event_name: str
    bundle_url: str
    is_active: bool

@router.get("/active")
def get_active_event():
    """Returns the current active event details to the game."""
    return CURRENT_EVENT

@router.put("/active")
def update_active_event(event: EventUpdate):
    """Updates the active event details dynamically from /docs."""
    global CURRENT_EVENT
    CURRENT_EVENT.update(event.dict())
    return {
        "status": "success",
        "message": "Event updated successfully!",
        "current_event": CURRENT_EVENT
    }
