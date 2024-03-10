from storyGenerator.storyGen import storyGenerator
from storySummerizer.summerizer import storySummerizer
from ImageGenerator.imageGen import generateImages
# from UI.api.main import speak
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# origins = ["*"]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

def play_output():
    story = storyGenerator()

    print()

    sentences = storySummerizer(story=story)

    print()

    ending = "in a colourful children's story animation style with out any texts."
    image_prompts = []

    for i in sentences:
        i = str(i).replace("."," ")
        i = i+ending
        image_prompts.append(i)

    print("The image prompts after editing: ")
    print(image_prompts)
    print()

    print("Print from the function:")
    images = generateImages(image_prompts)
    print()

    print("Print images:")
    print(images)
    # speak(story)

play_output()

# @app.get("/")
# def get_content():
#     return {"message": get_prompt()}

# Install eleven labs 



