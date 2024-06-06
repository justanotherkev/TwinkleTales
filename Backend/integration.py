# Run on PORT 8001

import random
from storyGenerator.story_gen import story_generator
from storySummerizer.summerizer import story_summerizer
from imageGenerator.image_gen import generate_images
from imageGenerator.image_gen import return_urls
from speechInputHandler.speech_input_handler import generate_narration_audio_file
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from speechInputHandler.speech_input_handler import generate_narration_audio_file
from speechInputHandler.speech_input_handler import duration_per_image
from databaseAPI.database import list_serial


app = FastAPI()

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()

is_story_completed = False
time_per_image = 0
images = []
randomUrl = ""


# Inside this function all the functions nessersary for story gen, image gen and
def set_output(theme: str, speech_inputs):

    global time_per_image
    global images
    global randomUrl
    global is_story_completed

    theme = theme.replace('"', "")
    print("\n[integration.py] - Theme: ", theme)
    print("\n[integration.py] - Speech inputs: ", speech_inputs)

    story = story_generator(theme, speech_inputs)
    # story = "Once upon a time, there was a boy named testinputs. He was very happy and he lived happily ever after."

    audio_file_path = "../Frontend/public/narration_audio.mp3"

    # Creates the mp3 file containing the narration
    generate_narration_audio_file(story, audio_file_path)

    # Call the function to get the duration one image should last
    time_per_image = duration_per_image(audio_file_path)

    # Summerizes the story
    sentences = story_summerizer(story)

    ending = (
        "in a colourful 3D-cartoon children's story animation style without any texts."
    )
    image_prompts = []

    # sentences are used to generate the image prompts
    for i in sentences:
        i = str(i).replace(".", " ")
        i = i + ending
        image_prompts.append(i)
    # print("\n[integration.py] - Image prompts", image_prompts)

    generate_images(image_prompts)
    images = return_urls()
    # print("\n[integration.py] - Received images", images)

    # retrieves a link to a random audio file in MongoDB to play in the background
    randomUrl = get_random_audio_url()

    is_story_completed = True
    return "done"


# Determines a random URL from the list of URLs in MongoDB
def get_random_audio_url():
    all_audio_urls = list_serial()

    print("The audio URLs being fetched from the DB: ", all_audio_urls)
    if len(all_audio_urls) > 0:
        random_index = random.randint(0, len(all_audio_urls) - 1)
        randomdict = all_audio_urls[random_index]
        return randomdict["audio_url"]
    else:
        print("No audio files found")


# Post method to recive the prompts for the story generation
@app.post("/{theme}")
async def start_content_generation(theme: str, request: Request):
    print("\n[integration.py] - start_content_generation() running...")
    list_str = await request.json()
    return set_output(theme, list_str)


@app.get("/")
async def play_story():
    if is_story_completed:
        return [images, randomUrl, time_per_image]
    else:
        return []
