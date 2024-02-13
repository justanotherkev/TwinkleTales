import pyttsx3

#library intialization to a variable
tts = pyttsx3.init()
voices = tts.getProperty('voices')

tts.setProperty('voice', voices[1].id)
tts.setProperty('r

tts.say("What are the characters are in your story?")
tts.say("Where is the story taking place?")
tts.say("What is the weather like today?")
tts.say("what is your favourite sport?")
tts.runAndWait()