import elevenlabs
import speech_recognition as stt


# to get an idea what are the available voices in elevenlabs
print(elevenlabs.voices())

# text to speech
# used Domi
# taking parameters that includes the question
list = []


def speak(text1):
    tts = elevenlabs.generate(
        text=text1, voice="Domi", api_key="ac764488fbfd187d77d484e08b31293a"
    )
    elevenlabs.play(tts)


# converting speech to text
def speechToText():
    recognizer = stt.Recognizer()
    with stt.Microphone() as source:
        print("speak now")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        answer1 = recognizer.recognize_google(audio)
        list.append(answer1)
        print(list)


# passing arguments into text to speech funtion and calling sppech to text funtion
def main():
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
        except Exception as e:
            print(f"Caught an exception: {e}")


if __name__ == "__main__":
    main()



# Caught an exception: ffplay from ffmpeg not found, necessary to play audio. On mac you can install it with 'brew install ffmpeg'. On linux and windows you can install it from https://ffmpeg.org/