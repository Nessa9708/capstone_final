import os
import requests
from django.conf import settings

BACKEND_URL = os.getenv("backend_url", "http://localhost:3030").rstrip("/")
SENTI_URL   = os.getenv("sentiment_analyzer_url", "").rstrip("/")

def get_request(endpoint, **kwargs):
    """GET to the Node backend with optional query params."""
    # build URL with optional query string
    url = f"{BACKEND_URL}{endpoint}"
    if kwargs:
        qs = "&".join(f"{k}={v}" for k, v in kwargs.items())
        url = f"{url}?{qs}"
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        return res.json()
    except Exception as err:
        print("Network exception:", err)
        return {"status": 500, "message": "backend-error"}

def analyze_review_sentiments(text: str) -> str:
    """Call the sentiment analyzer. Returns 'positive', 'neutral' or 'negative'."""
    if not SENTI_URL:
        return "neutral"  # safe default if not deployed
    try:
        # most labs expose GET /analyze/<text>
        url = f"{SENTI_URL}/analyze/{text}"
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        data = res.json()
        # normalize common payloads
        return (data.get("label") or data.get("sentiment") or "neutral").lower()
    except Exception as err:
        print("Sentiment error:", err)
        return "neutral"

def post_review(data_dict: dict):
    """POST a review to the Node backend."""
    try:
        url = f"{BACKEND_URL}/insert_review"
        res = requests.post(url, json=data_dict, timeout=10)
        res.raise_for_status()
        return res.json()
    except Exception as err:
        print("POST review error:", err)
        return {"status": 500, "message": "backend-error"}
