import os
from pathlib import Path
from dotenv import dotenv_values


def _load_config():
    """
    Load configuration from multiple places.

    Priority, lowest to highest:
    1. ~/.config/ringogpt/.env
    2. ~/.ringogpt.env
    3. .env in the current working directory
    4. real environment variables
    """
    config = {}

    config_paths = [
        Path.home() / ".config" / "ringogpt" / ".env",
        Path.home() / ".ringogpt.env",
        Path.cwd() / ".env",
    ]

    for path in config_paths:
        if path.exists():
            config.update(
                {
                    key: value
                    for key, value in dotenv_values(path).items()
                    if value is not None
                }
            )

    config.update(os.environ)
    return config


def _env_int(config, name, default):
    value = config.get(name)

    if value is None:
        return default

    try:
        return int(value)
    except ValueError:
        return default


CONFIG = _load_config()

API_KEY = CONFIG.get("RINGOGPT_API_KEY")

BASE_URL = CONFIG.get("RINGOGPT_BASE_URL", "https://api.openai.com/v1")

MODEL = CONFIG.get("RINGOGPT_MODEL", "gpt-4o-mini")

CACHE_FILE = os.path.expanduser(
    CONFIG.get("RINGOGPT_CACHE_FILE", "~/.ringogpt_cache.json")
)

COMMAND_TIMEOUT = _env_int(CONFIG, "RINGOGPT_TIMEOUT", 30)

DEBUG = CONFIG.get("RINGOGPT_DEBUG", "false").lower() == "true"
