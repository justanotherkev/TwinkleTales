from storyGenerator.storyGen import storyGenerator
from storySummerizer.summerizer import storySummerizer
from ImageGenerator.imageGen import generateImages
from UI.api.main import speak
from fastapi import FastAPI
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


class Item(BaseModel):
    list1: List[str]

# Post method to recive the prompts for the story generation
@story_app.post("/")
async def start_content_generation(item: Item ):
    print("This is printing the list from the pyhton post method")
    print(item.list1)
    return {"message": set_output(item.list1)}


# Get the method for the story narration
@story_app.get("/")
def get_narration():
    speak(story)
    return {"message": "The story is being played..."}
        

story = ""

def set_output(speech_inputs):
    global story
    story = storyGenerator(speech_inputs)

    print("Print the story from inside the set_output function:",story)

    sentences = storySummerizer(story)
    print("Print the sentences from inside the set_output function:",sentences)

    print()

    ending = "in a colourful 3D children's story animation style with out any texts."
    image_prompts = []

    for i in sentences:
        i = str(i).replace("."," ")
        i = i+ending
        image_prompts.append(i)

    global images
    images = generateImages(image_prompts)
    print("Print the image urls from inside the set_output function:",images)

    return(images)
    








