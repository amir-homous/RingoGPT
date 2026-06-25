import os
from dotenv import load_dotenv

load_dotenv()


def _env_int(name, default):
    value = os.getenv(name)

    if value is None:
        return default

    try:
        return int(value)
    except ValueError:
        return default


API_KEY = os.getenv("RINGOGPT_API_KEY")

BASE_URL = os.getenv("RINGOGPT_BASE_URL", "https://api.openai.com/v1")

MODEL = os.getenv("RINGOGPT_MODEL", "gpt-4o-mini")

CACHE_FILE = os.path.expanduser(
    os.getenv("RINGOGPT_CACHE_FILE", "~/.ringogpt_cache.json")
)

COMMAND_TIMEOUT = _env_int("RINGOGPT_TIMEOUT", 30)

DEBUG = os.getenv("RINGOGPT_DEBUG", "false").lower() == "true"
