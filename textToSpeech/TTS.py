import elevenlabs
import speech_recognition as stt


#to get an idea what are the available voices in elevenlabs
print(elevenlabs.voices())

#text to speech
#used Domi
#taking parameters that includes the question
list = []
def speak(text1):
<<<<<<< Updated upstream
    tts = elevenlabs.generate(
        text = text1,
        voice= "Domi",
        api_key = "ac764488fbfd187d77d484e08b31293a"
    )
    elevenlabs.play(tts)
=======
    try:
        tts = elevenlabs.generate(
            text = text1,
            voice= "Freya",
            api_key = "ac764488fbfd187d77d484e08b31293a"
        )
        elevenlabs.play(tts)
    except stt.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except stt.RequestError as e:
        print("Sorry, an error occurred. {0}".format(e))
>>>>>>> Stashed changes

#converting speech to text
def speechToText():
    recognizer = stt.Recognizer()
    with stt.Microphone() as source:
        print("Please wait, Adjusting to background noices")
        recognizer.adjust_for_ambient_noise(source, duration=5)
        print("speak now")
        audio = recognizer.listen(source)
        answer1 = recognizer.recognize_google(audio)
        list.append(answer1)
        print(list)

#passing arguments into text to speech funtion and calling sppech to text funtion
<<<<<<< Updated upstream
while True:
    try:
        speak("what are the characters are in your story?")
        speechToText()
        speak("Where is the story taking place?")
        speechToText()
        speak("What is the weather like today?")
        speechToText()
        speak("what is your favourite sport?")
        speechToText()
        break
    except:
        print("Sorry, I didn't understand")
=======
def main():
    try:
        speak("So tell me---, what are the characters--- in today's story---?")
        speechToText()
        speak("Oh wow --- that sounds really nice")
        speak("   ---Can you tell me where they live?")
        speechToText()
        speak("I can already tell that this is going to be a really interesting story. So, can you tell me what they like doing the most?")
        speechToText()
        speak("This sounds like a great start. Let's see where today's story takes us.")
    except Exception as e:
        print("Sorry, an error occurred:", e)
>>>>>>> Stashed changes

