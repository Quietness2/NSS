from fastapi import APIRouter

router = APIRouter(prefix="/events", tags=["events"])

CURRENT_EVENT = {
    "event_id": "divafuyu1",
    "event_name": "Imprisoned Marinett",
    "bundle_url": "https://nss-47ky.onrender.com/assets/asset.bundle_divafuyu1.zip",
    "is_active": True
}

@router.get("/active")
def get_active_event():
    """Returns the current active event details."""
    return CURRENT_EVENT
