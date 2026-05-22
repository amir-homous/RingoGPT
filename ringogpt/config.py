import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RINGOGPT_API_KEY")

BASE_URL = "https://api.gapgpt.app/v1"

MODEL = "gapgpt-qwen-3.5"

CACHE_FILE = os.path.expanduser("~/.ringogpt_cache.json")

