from fastapi import APIRouter

router = APIRouter(tags=["system"])

# Change Maintenance to True or False here when you need to lock the game
SYSTEM_STATE = {
    "Maintenance": False,
    "version": "1.0.0"
}

@router.get("/sys_state")
def get_system_state():
    return SYSTEM_STATE

@router.get("/ping")
def ping():
    return {"status": "online"}
