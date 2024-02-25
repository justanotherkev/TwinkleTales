import whisper
import numpy as np
import pyaudio
import keyboard
from langdetect import detect


pa = pyaudio.PyAudio()

RATE = 16000
CHUNK = 1024
RECORD_SECONDS = 5

stream = pa.open(format=pyaudio.paInt16,
                 channels=1,
                 rate=16000,
                 input=True,
                 frames_per_buffer=1024)

print("Please press R to record and Q to stop : ")
print(keyboard.read_key())

frames = []
def recordAudio(frames):

    print("Please speak")

    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

def stopRecording():
    stream.stop_stream()
    stream.close()
    pa.terminate()
    print("Recording finished.")

if keyboard.is_pressed('r'):
    recordAudio(frames)
elif keyboard.is_pressed('q'):
    stopRecording()

audioData = np.frombuffer(b''.join(frames), dtype=np.int16)

audioData = audioData.astype(np.float32) / np.iinfo(np.int16).max

STT = whisper.load_model('base')
result = STT.transcribe(audioData, fp16=False)
print(result['text'])


#
# print(detect(result['text']))
# if detect(result['text']) == 'en':
#     print(result['text'])
#
# else:
#     print("Sorry, I didn't understand")

#previous code
# import whisper
# import speech_recognition as stt
# import numpy as np
#
# recognizer = stt.Recognizer()
# with stt.Microphone() as source:
#     recognizer.adjust_for_ambient_noise(source)
#     print("talk now")
#     audio = recognizer.listen(source)
#     audioData = np.frombuffer(audio.frame_data, dtype=np.int16)
# STT = whisper.load_model('base')
# # result = STT.transcribe('speech.mp3',fp16=False)
# result = STT.transcribe(audioData, fp16=False)
# print(result['text'])


