from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline


class Prompt(BaseModel):
    text: str


model = pipeline(model="declare-lab/flan-alpaca-base")
app = FastAPI()


@app.post(path="/")
async def send_prompt(prompt: Prompt):
    return model(prompt.text, max_length=128, do_sample=True)
