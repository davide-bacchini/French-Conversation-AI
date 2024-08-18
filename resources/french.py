import torch
import wavio as wv
import sounddevice as sd
import numpy as np
import scipy.io.wavfile

from scipy.io.wavfile import write
from playsound import playsound
from transformers import VitsModel, AutoTokenizer

from resources.large_v3 import transcribe
from resources.LLAMA import answer


def conversation(messages, freq, duration):
    print("Recording...")
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    sd.wait()

    write("recording0.wav", freq, recording)
    wv.write("recording1.wav", recording, freq, sampwidth=2)

    model = VitsModel.from_pretrained("facebook/mms-tts-fra")
    tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-fra")

    result = transcribe("recording1.wav")
    french_text = answer(result["text"], messages)
    print(french_text)

    inputs = tokenizer(french_text, return_tensors="pt")
    input_ids = inputs.input_ids.long()
    attention_mask = inputs.attention_mask.long()

    with torch.no_grad():
        if input_ids.size(1) > 0 and attention_mask.size(1) > 0:
            output = model(input_ids=input_ids, attention_mask=attention_mask).waveform
        else:
            print("No input detected, please try again.")

    output_np = output.squeeze().numpy()

    output_np = output_np / np.abs(output_np).max()

    output_pcm = (output_np * 32767).astype(np.int16)

    scipy.io.wavfile.write(
        "answer.wav", rate=model.config.sampling_rate, data=output_pcm
    )

    playsound("answer.wav")
