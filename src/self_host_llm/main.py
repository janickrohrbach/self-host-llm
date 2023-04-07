import logging
from pathlib import Path

import yaml
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline

logger = logging.getLogger(__name__)

config = yaml.safe_load((Path(__file__).parent / "config.yaml").open())


class Prompt(BaseModel):
    text: str


logger.info("loading model")
model = pipeline(model=config["model_name"])
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
