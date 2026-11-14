import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow requests from TurboWarp and GitHub Pages
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
MAINTENANCE = os.getenv("MAINTENANCE", "false").lower() == "true"
class ScoreEntry(BaseModel):
    player: str
    song_id: str
    score: int

@app.get("/")
def root():
    return {"status": "online", "service": "NSS Backend"}

@app.get("/system@mode")
def get_sys_state():
    return {"state": "working", "version": "1.0.0"}

@app.post("/admin/maintenance")
def set_maintenance(enabled: bool, x_admin_key: str = Header(...)):
    if x_admin_key != ADMIN_KEY:
        raise HTTPException(status_code=403, detail="Invalid admin key")
    server_config["Maintenance"] = enabled
    return {"Maintenance": server_config["Maintenance"]}

@app.post("/submit_score")
def submit_score(entry: ScoreEntry):
    return {
        "received": True,
        "player": entry.player,
        "song_id": entry.song_id,
        "score": entry.score
    }
