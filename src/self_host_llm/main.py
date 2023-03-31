from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline


class Prompt(BaseModel):
    text: str


model = pipeline(model="declare-lab/flan-alpaca-base")
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post(path="/api")
async def send_prompt(prompt: Prompt):
    return model(prompt.text, max_length=128, do_sample=True)
