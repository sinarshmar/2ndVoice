WATCHED_DIR = "/Users/kumarutkarshsingh/newLife/2ndVoice/recordings"

API_KEY = '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'

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "X-Title": "2ndVoice",
    "Referer": "http://localhost"
}

LLM_ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "nvidia/llama-3.1-nemotron-nano-8b-v1:free"