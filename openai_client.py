from openai import OpenAI, OpenAIError
import os
from dotenv import load_dotenv
import json

load_dotenv()

_client   = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
_GAMESPROMPTID = os.getenv("HOTSEAT_GAMES_PROMPT_ID")
_QUESTIONSPROMPTID = os.getenv("HOTSEAT_QUESTIONS_PROMPT_ID")

client = OpenAI()

def generate_games(env, goal, mood):

    response = client.responses.create(
    prompt={
        "id": _GAMESPROMPTID,
        "version": "3",
        "variables": {
        "userenvselection": env,
        "usergoalselection": goal,
        "usermoodselection": mood
        }
    },
    input=[{
        "role": "user",
        "content": "Please return the result in JSON."
        }],
    reasoning={},
    max_output_tokens=2048,
    store=True
    )

    json_string = response.output[0].content[0].text
    data = json.loads(json_string)

    return data


def generate_questions(env, goal, mood):

    response = client.responses.create(
    prompt={
        "id": _QUESTIONSPROMPTID,
        "version": "1",
        "variables": {
        "userenvselection": env,
        "usergoalselection": goal,
        "usermoodselection": mood
        }
    },
    input=[{
        "role": "user",
        "content": "Please return the result in JSON."
        }],
    reasoning={},
    max_output_tokens=2048,
    store=True
    )

    json_string = response.output[0].content[0].text
    data = json.loads(json_string)

    return data
