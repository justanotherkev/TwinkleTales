import elevenlabs
import speech_recognition as stt


#to get an idea what are the available voices in elevenlabs
print(elevenlabs.voices())

#text to speech
#used Domi
#taking parameters that includes the question
list = []
def speak(text1):
    tts = elevenlabs.generate(
        text = text1,
        voice= "Domi",
        api_key = "ac764488fbfd187d77d484e08b31293a"
    )
    elevenlabs.play(tts)

#converting speech to text
def speechToText():
    recognizer = stt.Recognizer()
    with stt.Microphone() as source:
        badWords = ["sex","fuck","motherfucker"]
        print("speak now")
        audio = recognizer.listen(source)
        answer1 = recognizer.recognize_google(audio)
        if answer1 in badWords:
            print("Please speak again with appropriate words")
        else:
            list.append(answer1)
            print(list)

#passing arguments into text to speech funtion and calling sppech to text funtion
speak("what are the characters are in your story?")
speechToText()
speak("Where is the story taking place?")
speechToText()
speak("What is the weather like today?")
speechToText()
speak("what is your favourite sport?")
speechToText()

