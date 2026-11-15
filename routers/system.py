from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["system"])

# System state tracking using your "system@mode" structure
SYSTEM_STATE = {
    "system@mode": "normal",  # Can be changed to "maintenance" when needed
    "version": "1.0.0",
}

class ModeUpdate(BaseModel):
    mode: str

@router.get("/system@mode")
def get_system_mode():
    """Returns the current system mode status to the TurboWarp extension."""
    return SYSTEM_STATE

@router.post("/admin/set_mode")
def set_system_mode(data: ModeUpdate):
    """Admin endpoint to instantly change the system mode without redeploying."""
    SYSTEM_STATE["system@mode"] = data.mode
    return {"status": "success", "system@mode": SYSTEM_STATE["system@mode"]}

@router.get("/ping")
def ping():
    """Health check endpoint used by the background keep-alive loop."""
    return {"status": "online"}
