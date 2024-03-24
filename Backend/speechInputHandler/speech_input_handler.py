import re
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import elevenlabs
import speech_recognition as stt
import time
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
    "flannel",
    "hogwash",
    "blarney",
    "asshole",
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


class State(BaseModel):
    running: bool = false


def speak(text1):
    print("[speech_input_handler.py] - speak() running...")
    # print(text1)
    tts = elevenlabs.generate(
        text=text1,
        voice="Charlotte",
        api_key=os.getenv("ELEVEN_LABS_API"),  # NEW API KEY
    )
    elevenlabs.play(tts)


# generates narration into an audio file
def generate_narration_audio_file(text1, file_path):
    print("[speech_input_handler.py] - generate_narration_audio_file() running...")
    tts = elevenlabs.generate(
        text=text1,
        voice="Charlotte",
        api_key=os.getenv("ELEVEN_LABS_API"),  # NEW API KEY
    )
    with open(file_path, "wb") as audio_file:
        audio_file.write(tts)


# calculates the timestamp beetween images
def duration_per_image(audio_file_path):
    with audioread.audio_open(audio_file_path) as f:
        duration_seconds = f.duration
        duration_milliseconds = duration_seconds * 1000
        duration_per_image = duration_milliseconds / 6
    return duration_per_image


answers = ["", "", "", "", ""]

count = -1


def speech_to_text():
    global count
    recognizer = stt.Recognizer()
    with stt.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=5)
        print("speak now")
        audio = recognizer.listen(source)
        answer_raw = recognizer.recognize_google(audio)
        print("answer recieved")
        # answers[count] = (extract_nouns(answer_raw))  # THIS NEEDS TO BE FIXED
        answers[count] = answer_raw
        print(answers)


questions = [
    "So, tell me, what is the name of the character in today's story?",
    "2. Question",
    "3. Question",
    "4. Question",
    "5. Question",
    "6. Question",
]

error_questions = [
    "What is the name of the character in today's story?",
    "2. ErrorQuestion",
    "3. ErrorQuestion",
    "4. ErrorQuestion",
    "5. ErrorQuestion",
    "6. ErrorQuestion",
]


def get_prompt():
    count_break = 0
    global answers
    global count
    afterError = False
    while count_break < 8:
        count_break += 1
        try:
            if count == -1 and state:
                count = 0
                return [questions[0], ""]

            if count == 0 and state:
                if not afterError:
                    speak(questions[0])
                    # print(questions[0])

                speech_to_text()
                # time.sleep(4)
                # answers[0] = "David"
                afterError = False
                count = 1
                questions[1] = (
                    f"Hmm, {answers[0].capitalize()} is a really nice name. Can you tell me where {answers[0].capitalize()} lives?"
                )
                error_questions[1] = f"Where does {answers[0].capitalize()} live?"
                return [questions[1], "Your last answer: " + answers[0]]

            if count == 1 and state:
                if not afterError:
                    speak(questions[1])
                    # print(questions[1])

                speech_to_text()
                # time.sleep(4)
                # answers[1] = "London"
                afterError = False
                count = 2
                questions[2] = (
                    f"{answers[1].capitalize()} must be a wonderful place. Could you tell me what sport {answers[0].capitalize()} likes to play?"
                )
                error_questions[2] = (
                    f"What sport does {answers[0].capitalize()} like to play?"
                )
                return [questions[2], "Your last answer: " + answers[1]]

            if count == 2 and state:
                if not afterError:
                    speak(questions[2])
                    # print(questions[2])

                speech_to_text()
                # time.sleep(4)
                # answers[2] = "Soccer"
                afterError = False
                count = 3
                questions[3] = (
                    f"{answers[2].capitalize()} sounds like a fun sport! Where does {answers[0].capitalize()} play {answers[2].lower()}?"
                )

                error_questions[3] = (
                    f"Where does {answers[0].capitalize()} play {answers[2].lower()}?"
                )
                return [questions[3], "Your last answer: " + answers[2]]

            if count == 3 and state:
                if not afterError:
                    speak(questions[3])
                    # print(questions[3])

                speech_to_text()
                # time.sleep(4)
                # answers[3] = "in the park"
                afterError = False
                count = 4
                questions[4] = f"What is the weather like in {answers[1].capitalize()}?"
                error_questions[4] = (
                    f"What is the weather like in {answers[1].capitalize()}?"
                )
                return [questions[4], "Your last answer: " + answers[3]]

            if count == 4 and state:
                if not afterError:
                    speak(questions[4])
                    # print(questions[4])

                speech_to_text()
                # time.sleep(4)
                # answers[4] = "sunny"
                afterError = False
                count = -1
                count_break = 0
                return [
                    "Creating your story...",
                    "Your last answer: " + answers[4],
                    answers,
                ]

        except Exception as e:
            afterError = True
            print(f"Caught an exception: {e}")
            speak(
                "I'm sorry, I couldn't hear what you said. Please try again."
                + error_questions[count]
            )
            # print(
            #     "I'm sorry, I couldn't hear what you said. Please try again."
            #     + error_questions[count]
            # )


state = State()


@app.get("/")
def get_content():
    state.running = True
    return {"message": get_prompt()}


@app.get("/reset")
def reset_content():
    global answers
    global count
    answers = ["", "", "", "", ""]
    count = -1
    state.running = False
