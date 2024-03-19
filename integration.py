from storyGenerator.storyGen import storyGenerator
from storySummerizer.summerizer import storySummerizer
from ImageGenerator.imageGen import generateImages
# from UI.api.main import speak
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

story_app = FastAPI()

origins = ["*"]


story_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# story = ""
# image_prompts = []

class Item(BaseModel):
    list1: List[str]

# Post method to recive the prompts for the story generation
@story_app.post("/")
async def start_content_generation(item: Item ):
    # print("This is printing the list from the pyhton post method")
    # print(item.list1)
    set_output(item.list1)

# Get method for sending the image URL to be displayed 
    
# Get the method for the story narration
    

def set_output(speech_inputs):
    story = storyGenerator(speech_inputs)

    print()

    sentences = storySummerizer(story)

    print()

    ending = "in a colourful children's story animation style with out any texts."
    image_prompts = []

    for i in sentences:
        i = str(i).replace("."," ")
        i = i+ending
        image_prompts.append(i)

    # print("The image prompts after editing: ")
    # print(image_prompts)
    # print()

    images = generateImages(image_prompts)
    print()

    print("Print images:")
    print(images)
    

# def play_output():


# @story_app.get("/")
# def get_content():
#     return {"message": get_prompt()}

# Install eleven labs 



