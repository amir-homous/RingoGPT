from openai import OpenAI
import json
import re

from .config import API_KEY, BASE_URL, MODEL


class RingoGPTError(RuntimeError):
    """Custom error for user-friendly CLI failures."""


SYSTEM_PROMPT = """
You are RingoGPT, a Linux command assistant.

Your job:
Convert the user's natural language request into ONE useful Linux shell command.

Rules:
- Return ONLY valid JSON.
- Do not use markdown.
- Do not wrap the JSON in code fences.
- Do not include extra text before or after the JSON.
- The command must be a Linux shell command.
- Prefer POSIX-compatible commands that work in /bin/sh.
- Avoid shell-specific features like brace expansion, aliases, zsh-only syntax, or interactive-only shortcuts.
- Prefer explicit safe commands over clever short commands.
- If the user says "here", "this folder", "current directory", or "in this directory", treat it as the current working directory. Do NOT create a folder literally named "here".
- If creating nested folders, use mkdir -p with explicit paths.
- If creating multiple subfolders inside a parent folder, repeat the parent path for each subfolder.
- Quote paths when they contain spaces or special characters.
- If the request is unclear, generate a safe inspection command or explain the assumption.
- Classify danger as one of: low, medium, high.

Correct examples:
User request: create a folder named amir here and create folders 1 2 3 inside it
Correct command: mkdir -p amir/1 amir/2 amir/3

User request: make a folder called my project here
Correct command: mkdir -p "my project"

User request: show hidden files here
Correct command: ls -a

Bad examples:
Bad command: mkdir -p amir here/1 2 3
Reason: The word "here" should not become a folder name.

Bad command: mkdir amir/{1,2,3}
Reason: Brace expansion is not POSIX-safe and may not work in /bin/sh.

Danger guidance:
- low: read-only commands like ls, pwd, cat, grep, find, du, df, ps, tree
- medium: commands that create or modify normal user files, create folders, install packages, move files, or change project content
- high: destructive or risky commands like rm, dd, mkfs, chmod -R, chown -R, shutdown, reboot, disk formatting, deleting system files

JSON schema:
{
  "command": "...",
  "explanation": "...",
  "danger": "low | medium | high"
}
""".strip()


def _get_client():
    if not API_KEY or API_KEY.strip() in {
        "your_api_key_here",
        "your_gapgpt_api_key_here",
        "your_openrouter_api_key_here",
        "your_gemini_api_key_here",
        "your_groq_api_key_here",
    }:
        raise RingoGPTError(
            "Missing or placeholder API key. Set a real RINGOGPT_API_KEY in your environment or .env file."
        )

    return OpenAI(
        api_key=API_KEY,
        base_url=BASE_URL,
    )


def _extract_json(text):
    cleaned = text.strip()

    # Handle accidental markdown code fences.
    cleaned = re.sub(r"^```(?:json)?", "", cleaned).strip()
    cleaned = re.sub(r"```$", "", cleaned).strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass

    # Fallback: try to extract the first JSON object from the response.
    start = cleaned.find("{")
    end = cleaned.rfind("}")

    if start == -1 or end == -1 or end <= start:
        raise RingoGPTError("Model response was not valid JSON.")

    try:
        return json.loads(cleaned[start : end + 1])
    except json.JSONDecodeError as exc:
        raise RingoGPTError(f"Could not parse model JSON response: {exc}") from exc


def _normalize_result(data):
    if not isinstance(data, dict):
        raise RingoGPTError("Model response JSON must be an object.")

    command = str(data.get("command", "")).strip()
    explanation = str(data.get("explanation", "")).strip()
    danger = str(data.get("danger", "medium")).strip().lower()

    if danger not in {"low", "medium", "high"}:
        danger = "medium"

    if not command:
        raise RingoGPTError("Model did not return a command.")

    if not explanation:
        explanation = "No explanation provided."

    return {
        "command": command,
        "explanation": explanation,
        "danger": danger,
    }


def ask_command(question):
    question = question.strip()

    if not question:
        raise RingoGPTError("Empty request. Please write what command you need.")

    client = _get_client()

    try:
        response = client.chat.completions.create(
            model=MODEL,
            temperature=0.1,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question},
            ],
        )
    except Exception as exc:
        raise RingoGPTError(f"API request failed: {exc}") from exc

    try:
        text = response.choices[0].message.content or ""
    except Exception as exc:
        raise RingoGPTError(f"Unexpected API response format: {exc}") from exc

    data = _extract_json(text)
    return _normalize_result(data)
