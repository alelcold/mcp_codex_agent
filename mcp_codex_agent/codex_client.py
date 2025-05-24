import requests
from .config import API_URL

def call_codex(prompt: str, path: str):
    payload = {"prompt": prompt, "path": path}
    resp = requests.post(f"{API_URL}/agent/codex", json=payload)
    return resp.json()
