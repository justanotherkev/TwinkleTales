from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import elevenlabs
import speech_recognition as stt
import time
from textblob import TextBlob


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


def speak(text1):
    tts = elevenlabs.generate(
        # text=text1, voice="Dorothy", api_key="8ed01eb7ff0517ca565a17d18035be76" # OLD API KEY (Credits: 0)
        # text=text1, voice="Dorothy", api_key="db01e5e210bf5c2e59fad426228999c9",  # OLD API KEY (Credits: 0)
        text=text1,
        voice="Dorothy",
        api_key="477cba5a374f602e2a147516b64c6608",  # NEW API KEY
        # text=text1, voice="Dorothy", api_key="d8613a6881457e59de8990ac407ee004" # NEW API KEY
        # text=text1, voice="Dorothy", api_key="ac764488fbfd187d77d484e08b31293a" # PREMIUM API KEY
    )
    elevenlabs.play(tts)


# for i in range(len(elevenlabs.voices())):
#     print(i)

answers = ["", "", "", "", ""]

count = -1


def speechToText():
    global count
    recognizer = stt.Recognizer()
    with stt.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
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
            if count == -1:
                count = 0
                return [questions[0], ""]

            if count == 0:
                if not afterError:
                    speak(questions[0])
                    # print(questions[0])

                speechToText()
                # time.sleep(4)
                # answers[0] = "David"
                afterError = False
                count = 1
                questions[1] = (
                    f"Hmm, {answers[0].capitalize()} is a really nice name. Can you tell me where {answers[0].capitalize()} lives?"
                )
                error_questions[1] = f"Where does {answers[0].capitalize()} live?"
                return [questions[1], "Your last answer: " + answers[0]]

            if count == 1:
                if not afterError:
                    speak(questions[1])
                    # print(questions[1])

                speechToText()
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

            if count == 2:
                if not afterError:
                    speak(questions[2])
                    # print(questions[2])

                speechToText()
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

            if count == 3:
                if not afterError:
                    speak(questions[3])
                    # print(questions[3])

                speechToText()
                # time.sleep(4)
                # answers[3] = "in the park"
                afterError = False
                count = 4
                questions[4] = f"What is the weather like in {answers[1].capitalize()}?"
                error_questions[4] = (
                    f"What is the weather like in {answers[1].capitalize()}?"
                )
                return [questions[4], "Your last answer: " + answers[3]]

            if count == 4:
                if not afterError:
                    speak(questions[4])
                    # print(questions[4])

                speechToText()
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


@app.get("/")
def get_content():
    return {"message": get_prompt()}


# import openai

# openai.api_key = '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'

# def generate_story(sport, food, weather, characters, place):
#     prompt = f"Once upon a time, in a land far away called {place}, the weather was {weather}. "
#     prompt += f"There were characters named {', '.join(characters)}. They loved to play {sport} and eat {food}. "
#     prompt += "They went on an adventure and..."

#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=prompt,
#         temperature=0.7,
#         max_tokens=150
#     )

#     story = response.choices[0].text.strip()
#     return story

# # Example user inputs
# sport = input("What is your favorite sport? ")
# food = input("What is your favorite food? ")
# weather = input("What is the weather like in the story? ")
# characters = input("Who are the characters in the story? (Separate with commas) ").split(',')
# place = input("What is the name of the place in the story? ")

# # Generate the story
# generated_story = generate_story(sport, food, weather, characters, place)

# print("\nGenerated Story:")
# print(generated_story)


# import os
# from openai import OpenAI

# client = OpenAI(
#     # This is the default and can be omitted
#     api_key="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",
# )

# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Say this is a test",
#         }
#     ],
#     model="gpt-3.5-turbo",
# )
