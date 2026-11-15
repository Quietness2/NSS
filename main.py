import os
import asyncio
import httpx
from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
async def keep_alive():
    """Background task that pings the server every 5 minutes to prevent Render from spinning down."""
    while True:
        await asyncio.sleep(300) # 300 seconds = 5 minutes
        try:
            async with httpx.AsyncClient() as client:
                # Replace with your actual live Render URL
                await client.get("https://nss-47ky.onrender.com/ping")
        except Exception as err:
            print(f"Keep-alive ping failed: {err}")

ADMIN_KEY = os.getenv("ADMIN_KEY", "testing.passwd.maintenance")

# Add this dictionary so both /sys_state and /admin/maintenance share the same state
server_config = {
    "Maintenance": os.getenv("MAINTENANCE", "false").lower() == "true",
    "version": "1.0.0"
}

@app.on_event("startup")
async def startup_event():
    # Start the background loop as soon as FastAPI boots up
    asyncio.create_task(keep_alive())

@app.get("/")
def root():
    return {"status": "online", "service": "NSS Backend"}

@app.get("/ping")
def ping():
    return {"status": "awake"}

@app.get("/sys_state")
def get_sys_state():
    return server_config

@app.post("/admin/maintenance")
def set_maintenance(enabled: bool, x_admin_key: str = Header(...)):
    if x_admin_key != ADMIN_KEY:
        raise HTTPException(status_code=403, detail="Invalid admin key")
    server_config["Maintenance"] = enabled
    return {"Maintenance": server_config["Maintenance"]}
def root():
    return {"status": "online", "service": "NSS Backend"}
