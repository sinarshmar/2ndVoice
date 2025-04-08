import requests
from constants import HEADERS, LLM_ENDPOINT, DEFAULT_MODEL

def create_payload(messages, model=DEFAULT_MODEL):
    return {
        "model": model,
        "messages": messages
    }
def send_request(payload):
    response = requests.post(LLM_ENDPOINT, headers=HEADERS, json=payload)
    return handle_response(response)

def handle_response(response):
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")
