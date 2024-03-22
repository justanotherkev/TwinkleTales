from sympy import true
from storyGenerator.storyGen import storyGenerator
from storySummerizer.summerizer import storySummerizer
from ImageGenerator.imageGen import generateImages
from UI.api.main import speak
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv

story_app = FastAPI()

origins = ["*"]


story_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()

story = ""


# Post method to recive the prompts for the story generation
@story_app.post("/")
async def start_content_generation(request: Request):
    print("\n[integration.py] - start_content_generation() running...")
    list_str = await request.json()
    return {"message": set_output(list_str)}


# Get the method for the story narration
@story_app.get("/")
def get_narration():
    print("\n[integration.py] - get_narration() running...")
    global story
    speak(story)
    return {"message": "OK"}


def set_output(speech_inputs):
    global story
    story = storyGenerator(speech_inputs)

    sentences = storySummerizer(story)

    ending = "in a colourful 3D-cartoon children's story animation style without any texts."
    image_prompts = []

    for i in sentences:
        i = str(i).replace(".", " ")
        i = i + ending
        image_prompts.append(i)

    global images
    images = generateImages(image_prompts)
    print("\n[integration.py] - Received images", images)

    return images
