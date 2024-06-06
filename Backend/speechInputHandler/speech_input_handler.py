# Run on PORT 8000

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import elevenlabs
import speech_recognition as stt
import audioread
from sympy import false
from textblob import TextBlob
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()


def extract_nouns(text):
    blob = TextBlob(text)
    return [word for word, pos in blob.tags if pos in ["NN", "NNS"]]


profanity_stop_words = [
    "ass",
    "rot",
    "git",
    "bum",
    "arse",
    "bunk",
    "bosh",
    "bint",
    "chav",
    "cock",
    "crap",
    "cunt",
    "damn",
    "dick",
    "dolt",
    "dyke",
    "fuck",
    "hell",
    "twat",
    "shit",
    "slut",
    "wife",
    "knob",
    "fool",
    "jerk",
    "guff",
    "jive",
    "piss",
    "muck",
    "blah",
    "feck",
    "bull",
    "tosh",
    "wank",
    "bitch",
    "pussy",
    "minge",
    "whore",
    "hooey",
    "tripe",
    "hokum",
    "trash",
    "crock",
    "crazy",
    "idiot",
    "loser",
    "prick",
    "pissy",
    "nonce",
    "bilge",
    "moron",
    "bogus",
    "sucky",
    "hooch",
    "whack",
    "retard",
    "phooey",
    "jabber",
    "minger",
    "nigger",
    "bloody",
    "crappy",
    "shitty",
    "tosser",
    "douche",
    "stupid",
    "faggot",
    "feckin",
    "drivel",
    "crikey",
    "bungle",
    "numpty",
    "effing",
    "gibber",
    "bugger",
    "wanker",
    "piffle",
    "waffle",
    "muddle",
    "bunkum",
    "asshat",
    "flannel",
    "hogwash",
    "blarney",
    "asshole",
    "asswipe",
    "pillock",
    "twattle",
    "dumbass",
    "bellend",
    "scumbag",
    "garbage",
    "husband",
    "sodding",
    "schmuck",
    "freakin",
    "fecking",
    "bastard",
    "suck my",
    "baloney",
    "spastic",
    "goddamn",
    "friggin",
    "rubbish",
    "cripple",
    "sod off",
    "twaddle",
    "wanksta",
    "blather",
    "jackass",
    "bollocks",
    "bullshit",
    "brouhaha",
    "arsehole",
    "freaking",
    "knobhead",
    "nonsense",
    "claptrap",
    "piss off",
    "dickhead",
    "fricking",
    "malarkey",
    "flimflam",
    "flipping",
    "ballyhoo",
    "poppycock",
    "flim-flam",
    "gibbering",
    "douchebag",
    "silliness",
    "horseshit",
    "gibberish",
    "balderdash",
    "codswallop",
    "tomfoolery",
    "flapdoodle",
    "shenanigans",
    "hocus-pocus",
    "mumbo-jumbo",
    "mumbo jumbo",
    "gobbledygook",
    "motherfucker",
    "fiddlesticks",
    "motherfucking",
    "fiddle-faddle",
    "son of a bitch",
]

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# state to determine whether the speak() function should run
class State(BaseModel):
    running: bool = false


stop_app = False

recognizer = stt.Recognizer()


# generates narration into an audio file
def generate_narration_audio_file(text1, file_path):
    print("[speech_input_handler.py] - generate_narration_audio_file() running...")
    tts = elevenlabs.generate(
        text=text1,
        voice="Charlotte",
        api_key=os.getenv("ELEVEN_LABS_API"),
    )
    with open(file_path, "wb") as audio_file:
        audio_file.write(tts)


# calculates the time duration of each image
def duration_per_image(audio_file_path):
    with audioread.audio_open(audio_file_path) as f:
        duration_seconds = f.duration
        duration_milliseconds = duration_seconds * 1000
        duration_per_image = duration_milliseconds / 6
    return duration_per_image


def adjust_bg_noise(adjustment_duration):
    print("[speech_input_handler.py] - adjust_bg_noise() running...")
    print("Recognizer properties (before):")
    for key, value in recognizer.__dict__.items():
        print(f"{key}: {value}")
    print("\n")

    with stt.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=adjustment_duration)

    print("Recognizer properties (after):")
    for key, value in recognizer.__dict__.items():
        print(f"{key}: {value}")
    print("\n")


answers_list = ["0", "1", "2", "3", "4"]


def error_question_list_selector(theme: str, answers_list: list):
    if theme.lower() == "superhero":
        return [
            "What is the name of the brave superhero in our story?",
            f"What is {answers_list[0].capitalize()}'s strongest power?",
            f"Who is {answers_list[0].capitalize()}'s arch-nemesis?",
            f"What is {answers_list[2].capitalize()}'s biggest weakness?",
            f"Which city does {answers_list[0].capitalize()} protect?",
        ]
    elif theme.lower() == "adventure":
        return [
            "What is the name of the fearless adventurer in our story?",
            f"Where does {answers_list[0].capitalize()}'s journey start?",
            f"What obstacle does {answers_list[0].capitalize()} face early in the adventure?",
            f"Who is the mysterious guide {answers_list[0].capitalize()} encounters?"
            f"What legendary treasure does {answers_list[0].capitalize()} seek?",
        ]
    elif theme.lower() == "fairy tale":
        return [
            "What is the name of the main character in our story?",
            f"where does {answers_list[0].capitalize()} live?",
            f"What magical creature does {answers_list[0].capitalize()} find in {answers_list[1].capitalize()}?",
            f"Who is {answers_list[0].capitalize()}'s loyal companion? ",
            f"What is the goal of {answers_list[0].capitalize()}'s adventure?",
        ]
    elif theme.lower() == "sports":
        return [
            "What is the name of the star athlete in our story?",
            f"Which city does {answers_list[0].capitalize()} live in?",
            f"What sport does {answers_list[0].capitalize()} play?",
            f"Who is {answers_list[0].capitalize()}'s biggest rival on the field?",
            f"What championship does {answers_list[0].capitalize()} want to win?",
        ]


def question_list_selector(theme: str, answers_list: list):
    if theme.lower() == "superhero":
        return [
            "What is the name of our brave superhero today?",
            f"What is {answers_list[0].capitalize()}'s strongest power?",
            f"{answers_list[1].capitalize()} sounds powerful! Who is {answers_list[0].capitalize()}'s arch-nemesis?",
            f"{answers_list[2].capitalize()} sounds scary! What is {answers_list[2].capitalize()}'s biggest weakness?",
            f"Which city does {answers_list[0].capitalize()} protect?",
        ]
    elif theme.lower() == "adventure":
        return [
            "What is the name of the fearless adventurer in our story?",
            f"Hmm, {answers_list[0].capitalize()} sounds like an adventurer! Tell me, where does {answers_list[0].capitalize()}'s journey start?",
            f"{answers_list[1].capitalize()} sounds mysterious. What obstacle does {answers_list[0].capitalize()} face early in the adventure?",
            f"Who is the mysterious guide {answers_list[0].capitalize()} encounters along the way?",
            f"What legendary treasure does {answers_list[0].capitalize()} seek?",
        ]
    elif theme.lower() == "fairy tale":
        return [
            "What's the name of the main character in our fairy tale?",
            f"Where does {answers_list[0].capitalize()} live?",
            f"{answers_list[1].capitalize()} must be a wonderful place! What magical creature does {answers_list[0].capitalize()} find in {answers_list[1].capitalize()}?",
            f"Who is {answers_list[0].capitalize()}'s loyal companion on the quest? ",
            f"What is the goal of {answers_list[0].capitalize()}'s adventure?",
        ]
    elif theme.lower() == "sports":
        return [
            "So, tell me, what is the name of the star athlete in today's story?",
            f"{answers_list[0].capitalize()} is a really nice name! Which city does {answers_list[0].capitalize()} live in?",
            f"Could you tell me what sport our star athlete {answers_list[0].capitalize()} plays?",
            f"Who is {answers_list[0].capitalize()}'s biggest rival on the field?",
            f"What championship does {answers_list[0].capitalize()} dream of winning?",
        ]


# Takes in a text and uses the ElevenLabs API to narrate
def speak(text):
    if not stop_app:
        # print("[speech_input_handler.py] - speak() running...")
        # tts = elevenlabs.generate(
        #     text=text,
        #     voice="Charlotte",
        #     api_key=os.getenv("ELEVEN_LABS_API"),  # NEW API KEY
        # )
        # elevenlabs.play(tts)
        print(text)


# Recognises speech and converts to text
def speech_to_text(theme: str, count: int):
    global answers_list

    print("Recognizer properties:")
    for key, value in recognizer.__dict__.items():
        print(f"{key}: {value}")
    print("\n")

    if not stop_app:

        with stt.Microphone() as source:
            while not stop_app:
                try:
                    print("speak now")
                    recognizer.adjust_for_ambient_noise(source, duration=0.2)
                    audio = recognizer.listen(source)
                    answer_raw = recognizer.recognize_google(audio)
                    # answer_raw = input(">>> ")
                    # Use only the first noun
                    # answer_raw = extract_nouns(answer_raw)[0]

                    # Throws an error if profanity is detected
                    if answer_raw in profanity_stop_words:
                        raise ValueError("Profanity detected in user input")
                    answers_list[count] = answer_raw
                    print(answers_list)
                    break

                except Exception as e:
                    print(f"Caught an exception: {e}")
                    if not stop_app:
                        speak(
                            "I'm sorry, I couldn't hear what you said. Please try again."
                            + error_question_list_selector(theme, answers_list)[count]
                        )


@app.get("/ask_question/{theme}/{question_number}")
def ask_question(theme: str, question_number: int):
    global answers_list
    global stop_app

    stop_app = False

    questions_list = question_list_selector(theme=theme, answers_list=answers_list)

    print("Iteration: " + str(question_number))
    if not stop_app:
        if question_number == 0:
            return [
                questions_list[question_number],
                "",
            ]
        else:
            speak(questions_list[question_number - 1])
            speech_to_text(theme, question_number - 1)
            questions_list = question_list_selector(
                theme=theme, answers_list=answers_list
            )

            if question_number < 5:
                return [
                    questions_list[question_number],
                    "Your last answer: "
                    + answers_list[question_number - 1].capitalize(),
                ]
            else:
                return [
                    "Creating your story...",
                    "Your last answer: "
                    + answers_list[question_number - 1].capitalize(),
                    answers_list,
                ]


@app.get("/adjust_noise")
def adjust_noise():
    adjust_bg_noise(20)
    return {"message": "Background noise adjusted"}


# Reset all global variables here
@app.get("/reset")
def reset_content():
    global stop_app
    global answers_list

    stop_app = True
    answers_list = ["", "", "", "", ""]
    return {"message": "App state has been reset"}
