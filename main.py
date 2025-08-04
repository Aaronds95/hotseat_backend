from fastapi import FastAPI
from pydantic import BaseModel
from openai_client import generate_games
from typing import Optional
import json

app = FastAPI()

class SelectionIn(BaseModel):
    envSelection: str
    goalSelection: str
    moodSelection: str

class GameOut(BaseModel):
    gameName: str
    gameInstructions: str
    gameExamples: Optional[str]

class SelectionResponse(BaseModel):
    games: list[GameOut]


@app.get("/")
def read_root():
    return {"message": "Hello Srikar, how's Portugal?"}

@app.post("/selection", response_model=SelectionResponse)
def select_env(selection: SelectionIn):
    data = generate_games(
        selection.envSelection, selection.goalSelection, selection.moodSelection
    )
    games = data['games']

    return {"games": games}
