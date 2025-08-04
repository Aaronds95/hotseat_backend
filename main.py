from fastapi import FastAPI
from pydantic import BaseModel
from openai_client import generate_games, generate_questions
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

class GameResponse(BaseModel):
    games: list[GameOut]

class QuestionOut(BaseModel):
    questionText: str

class QuestionResponse(BaseModel):
    questions: list[QuestionOut]


@app.get("/")
def read_root():
    return {"message": "Hello Srikar, how's Portugal?"}

@app.post("/games", response_model=GameResponse)
def select_env(selection: SelectionIn):
    data = generate_games(
        selection.envSelection, selection.goalSelection, selection.moodSelection
    )
    games = data['games']

    return {"games": games}

@app.post("/questions", response_model=QuestionResponse)
def select_env(selection: SelectionIn):
    data = generate_questions(
        selection.envSelection, selection.goalSelection, selection.moodSelection
    )
    questions = data['questions']

    return {"questions": questions}