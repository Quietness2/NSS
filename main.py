import asyncio
import httpx
from fastapi import FastAPI
from routers import system, events

app = FastAPI(title="New Scratch SEKAI Backend")

# Include your modular router handlers
app.include_router(system.router)
app.include_router(events.router)

async def keep_alive():
    """Background task to prevent Render free-tier from spinning down."""
    while True:
        await asyncio.sleep(300)  # Every 5 minutes
        try:
            async with httpx.AsyncClient() as client:
                await client.get("https://nss-47ky.onrender.com/ping")
        except Exception as err:
            print(f"Keep-alive error: {err}")

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(keep_alive())
