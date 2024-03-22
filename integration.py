from storyGenerator.story_gen import story_generator
from storySummerizer.summerizer import story_summerizer
from imageGenerator.image_gen import generate_images
from imageGenerator.image_gen import return_urls
from speechInputHandler.speech_input_handler import generate_narration_audio_file
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
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
    generate_narration_audio_file(story)
    return {"message": "OK"}


def set_output(speech_inputs):
    global story
    story = story_generator(speech_inputs)

    sentences = story_summerizer(story)

    ending = (
        "in a colourful 3D-cartoon children's story animation style without any texts."
    )
    image_prompts = []

    for i in sentences:
        i = str(i).replace(".", " ")
        i = i + ending
        image_prompts.append(i)

    global images
    generate_images(image_prompts)
    images = return_urls()
    print("\n[integration.py] - Received images", images)

    return images
