import wave
import json
from vosk import Model, KaldiRecognizer

def speech_to_text(record_loc):
    # Load your downloaded model (you can move this outside the function for speed if reused)
    model = Model("vosk-model-small-en-us-0.15")

    # Open WAV file
    wf = wave.open(record_loc, "rb")

    # Check WAV format (mono, PCM)
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        raise ValueError("Audio file must be WAV format: mono PCM 16-bit")

    # Setup recognizer
    rec = KaldiRecognizer(model, wf.getframerate())

    # Transcription result
    transcript = []

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            transcript.append(result.get('text', ''))

    # Append final result
    final_result = json.loads(rec.FinalResult())
    transcript.append(final_result.get('text', ''))

    full_transcription = ' '.join(transcript).strip()

    print("Transcription:", full_transcription)
    return full_transcription
