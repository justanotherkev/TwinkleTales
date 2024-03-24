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


# Post method to recive the prompts for the story generation
@story_app.post("/")
async def start_content_generation(request: Request):
    print("\n[integration.py] - start_content_generation() running...")
    list_str = await request.json()
    return {"message": set_output(list_str)}


# Inside this function all the functions nessersary for story gen, image gen and 
def set_output(speech_inputs):

    story = story_generator(speech_inputs)

    # Creates the mp3 file containing the narration
    generate_narration_audio_file(story,"narration_output.mp3")

    # Call the function to get the duration one image should last
    time_per_image = duration_per_image("narration_output.mp3")

    sentences = story_summerizer(story)

    ending = (
        "in a colourful 3D-cartoon children's story animation style without any texts."
    )
    image_prompts = []

    for i in sentences:
        i = str(i).replace(".", " ")
        i = i + ending
        image_prompts.append(i)
    
    # print("\n[integration.py] - Image prompts", image_prompts)
 
    generate_images(image_prompts)
    images = return_urls()
    print("\n[integration.py] - Received images", images)

    randomUrl = get_random_audio_url()

    return [images, time_per_image,randomUrl]


def get_random_audio_url():
    all_audio_urls = list_serial()

    print("The audio URLs being fetched from the DB: ",all_audio_urls)
    if len(all_audio_urls) > 0:
        random_index = random.randint(0, len(all_audio_urls) - 1)
        randomdict =  all_audio_urls[random_index]
        return randomdict["audio_url"]
    else:
        print("No audio files found")





        
