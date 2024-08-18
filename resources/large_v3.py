from transformers import pipeline


def transcribe(audio):
    pipe = pipeline(
        "automatic-speech-recognition", model="pierreguillou/whisper-medium-french"
    )
    result = pipe(audio)
    return result
