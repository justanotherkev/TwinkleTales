import elevenlabs
import ffmpeg
print(elevenlabs.voices())
tts = elevenlabs.generate(
    text = "what are the characters are in the story!"+"Where is the story taking place?"+"What is the weather like today?"+"what is your favourite sport?",
    voice= "Domi",

)


elevenlabs.play(tts)
