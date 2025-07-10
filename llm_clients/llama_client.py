# llm_clients/llama_client.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("GITHUB_TOKEN_LLAMA")

HEADERS = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

ENDPOINT = "https://models.github.ai/inference/chat/completions"

def call_llama(messages):
    payload = {
        "model": "meta/Llama-4-Scout-17B-16E-Instruct",
        "messages": messages,
        "temperature": 1.0,
        "top_p": 1.0,
        "max_tokens": 1000
    }

    response = requests.post(ENDPOINT, json=payload, headers=HEADERS)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
