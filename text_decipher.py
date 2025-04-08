import wave
import json
from vosk import Model, KaldiRecognizer

def speech_to_text(record_loc):
    # Load your downloaded model
    model = Model("vosk-model-small-en-us-0.15")

    # Open audio file (WAV format)
    wf = wave.open(record_loc, "rb")

    # Initialize recognizer
    rec = KaldiRecognizer(model, wf.getframerate())

    # Read audio in chunks and print results
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())

    final_result = json.loads(rec.FinalResult())
    print("Transcription:", final_result['text'])
    return(final_result['text'])
