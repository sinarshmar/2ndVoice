import time as t
from text_decipher import speech_to_text
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from collections import deque
from llm_client import create_payload, send_request
from constants import WATCHED_DIR

convo = deque(maxlen=4)


def compile_message(convo_deque):

    message_list=list(convo_deque)
    # Add a final user message to prompt the LLM to reply
    message_list.append({
        "role": "user",
        "content": "Please continue this conversation with the next assistant response."
    })
    return message_list


class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            t1 = t.time()
            print(f"New file detected: {event.src_path}")
            # Call your function here, e.g., transcribe_audio(event.src_path)
            # You can filter file types too:
            if event.src_path.endswith(".wav"):
                print("WAV file detected. Running Vosk transcription..")
                # Example placeholder for your custom function
                result = speech_to_text(event.src_path)
                # result = speech_to_text("/Users/kumarutkarshsingh/newLife/2ndVoice/recordings/1New Recording copy.wav")
                convo.append({"role": "user", "content": result})
                # messages = compile_message(convo)
                messages = list(convo)

                try:
                    reply = send_request(create_payload(messages))
                    print("LLM reply:", reply)
                    convo.append({"role": "assistant", "content": reply})
                except Exception as e:
                    print("Error contacting LLM:", e)

                print("time taken",t.time() -t1)



if __name__ == "__main__":

    event_handler = NewFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=WATCHED_DIR, recursive=False)
    observer.start()
    print(f"Watching directory: {WATCHED_DIR}")

    try:
        while True:
            t.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()



