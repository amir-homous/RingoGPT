import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RINGOGPT_API_KEY")

BASE_URL = os.getenv("RINGOGPT_BASE_URL", "https://api.openai.com/v1")

MODEL = os.getenv("RINGOGPT_MODEL", "gpt-4o-mini")

CACHE_FILE = os.path.expanduser(
    os.getenv("RINGOGPT_CACHE_FILE", "~/.ringogpt_cache.json")
)
