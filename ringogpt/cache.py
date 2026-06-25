import json
import os

from .config import CACHE_FILE


def load_cache():
    if not os.path.exists(CACHE_FILE):
        return {}

    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, dict):
            return data

        return {}

    except (OSError, json.JSONDecodeError):
        return {}


def save_cache(cache):
    cache_dir = os.path.dirname(CACHE_FILE)

    if cache_dir:
        os.makedirs(cache_dir, exist_ok=True)

    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)
