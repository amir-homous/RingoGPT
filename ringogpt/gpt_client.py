from openai import OpenAI
import json
from .config import API_KEY, BASE_URL, MODEL


client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)


def ask_command(question):

    prompt = f"""
User wants a useful Linux terminal command.

Request:
{question}

Return ONLY JSON:

{{
 "command": "...",
 "explanation": "...",
 "danger": "low | medium | high"
}}
"""

    response = client.responses.create(
        model=MODEL,
        input=prompt
    )

    text = response.output_text.strip()

    return json.loads(text)

