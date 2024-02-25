import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import speech_recognition as sr
import io
from pydub import AudioSegment
from transformers import AutoProcessor, AutoModelForCTC

tokenizer = AutoProcessor.from_pretrained("facebook/wav2vec2-base-960h")
model = AutoModelForCTC.from_pretrained("facebook/wav2vec2-base-960h")

r = sr.Recognizer()

with sr.Microphone(sample_rate=16000) as source:
    print("Start speaking now: ")
    while True:
        audio = r.listen(source)  # py audio object
        data = io.BytesIO(audio.get_wav_data())  # array of bytes
        clip = AudioSegment.from_file(data)  # numpy array
        x = torch.FloatTensor(clip.get_array_of_samples())  # tensor

        inputs = tokenizer(x, sampling_rate=16000, return_tensors='pt', padding='longest').input_values
        logits = model(inputs).logits
        tokens = torch.argmax(logits, axis=-1)
        text = tokenizer.batch_decode(tokens)

        print("You said: ", str(text).lower())

