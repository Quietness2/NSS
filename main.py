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

class ScoreEntry(BaseModel):
    player: str
    song_id: str
    score: int

@app.get("/")
def root():
    return {"status": "online", "service": "NSS Backend"}

@app.get("/sys_state")
def get_sys_state():
    return {"state": "working", "version": "1.0.0"}

@app.post("/submit_score")
def submit_score(entry: ScoreEntry):
    return {
        "received": True,
        "player": entry.player,
        "song_id": entry.song_id,
        "score": entry.score
    }
