from fastapi import FastAPI

app = FastAPI()

userEnvSelection = ""
userGoalSelection = ""
userMoodSelection = ""


@app.get("/")
def read_root():
    return {"message": "Hello Srikar, how's Portugal?"}

@app.post("/items/")
def create_item(name: str, price: float):
    return {"name:" : name, "price": price}


@app.post("/selection")
def select_env(envSelection: str, goalSelection: str, moodSelection: str):
    
    userEnvSelection = envSelection
    userGoalSelection = goalSelection
    userMoodSelection = moodSelection

    return {"envSelection" : userEnvSelection, "goalSelection" : userGoalSelection, "moodSelection" : userMoodSelection}
