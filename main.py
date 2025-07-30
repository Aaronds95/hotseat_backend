from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SelecionIn(BaseModel):
    envSelction: str
    goalSelection: str
    moodSelection: str

class SelectionOut(BaseModel):
    envSelection: str
    goalSelection: str
    moodSelection: str


@app.get("/")
def read_root():
    return {"message": "Hello Srikar, how's Portugal?"}

@app.post("/selection", response_model=SelectionOut)
def select_env(selection: SelecionIn):
    
    return SelectionOut(**selection.model_dump())
