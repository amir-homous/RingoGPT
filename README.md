# RingoGPT

A lightweight AI-powered command-line assistant that converts natural language into Linux shell commands.

RingoGPT helps you describe what you want to do in the terminal, then generates a command, explains it, shows a risk level, and only runs it after your confirmation.

It is designed for people who use Linux but do not always remember the exact command.

---

## Quick example

```bash
ringogpt "show hidden files in the current directory"
```

Example output:

```text
Command:
ls -a

Explanation:
Lists all files in the current directory, including hidden files.

Danger: LOW

Run command? (y/N):
```

Persian also works:

```bash
soal "فایل های مخفی این پوشه رو نشون بده"
```

---

## Why this project exists

Sometimes you know what you want to do, but you do not remember the exact Linux command.

RingoGPT helps with that.

The goal is not to replace learning Linux.

The goal is to make the terminal easier, faster, and safer for everyday tasks.

---

## Features

* Convert natural language into Linux shell commands
* Works with English and Persian prompts
* Shows the command before execution
* Explains what the command does
* Classifies risk as `LOW`, `MEDIUM`, or `HIGH`
* Requires user confirmation before running anything
* Uses stricter confirmation for high-risk commands
* Caches previous responses locally
* Supports OpenAI-compatible API providers
* Works with both `ringogpt` and `soal` commands
* Designed to be lightweight and easy to extend

---

## Safety behavior

RingoGPT does not silently execute commands.

Before anything runs, you see:

* the generated command
* a plain explanation
* the danger level
* a confirmation prompt

For high-risk commands, RingoGPT requires stronger confirmation.

Examples of high-risk actions:

* deleting files
* formatting disks
* changing ownership or permissions recursively
* shutting down or rebooting
* modifying system files

Always review AI-generated commands before running them.

---

## How it works

RingoGPT follows this flow:

```text
User prompt
   ↓
Check local cache
   ↓
Send request to AI provider
   ↓
Receive JSON response
   ↓
Validate command, explanation, and danger level
   ↓
Show result to user
   ↓
Ask for confirmation
   ↓
Run command only if approved
```

The model response is expected to be JSON:

```json
{
  "command": "ls -a",
  "explanation": "Lists all files, including hidden files.",
  "danger": "low"
}
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/amir-homous/RingoGPT.git
cd RingoGPT
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Install RingoGPT locally

```bash
python -m pip install -e .
```

After installation, both commands should work:

```bash
ringogpt "show hidden files"
```

```bash
soal "show hidden files"
```

---

## Configuration

RingoGPT uses environment variables.

Create a `.env` file:

```bash
cp .env.example .env
```

Then edit it:

```bash
nano .env
```

Basic example:

```env
RINGOGPT_API_KEY=your_api_key_here
RINGOGPT_BASE_URL=https://api.openai.com/v1
RINGOGPT_MODEL=gpt-4o-mini
RINGOGPT_CACHE_FILE=~/.ringogpt_cache.json
RINGOGPT_TIMEOUT=30
RINGOGPT_DEBUG=false
```

Do not commit your `.env` file.

---


## Global usage with pipx

If you want to use RingoGPT from anywhere in your terminal, install it with `pipx`.

```bash
sudo apt update
sudo apt install -y pipx
pipx ensurepath
```

Restart your terminal, then install RingoGPT:

```bash
cd RingoGPT
pipx install .
```

After that, these commands should be available globally:

```bash
ringogpt "show hidden files"
soal "show hidden files"
```

---

## Global configuration file

For global usage, RingoGPT can read configuration from:

```text
~/.config/ringogpt/.env
```

Create it:

```bash
mkdir -p ~/.config/ringogpt
nano ~/.config/ringogpt/.env
```

Example:

```env
RINGOGPT_API_KEY=your_api_key_here
RINGOGPT_BASE_URL=https://openrouter.ai/api/v1
RINGOGPT_MODEL=openrouter/free
RINGOGPT_CACHE_FILE=~/.ringogpt_cache.json
RINGOGPT_TIMEOUT=30
RINGOGPT_DEBUG=false
```

Protect the file:

```bash
chmod 600 ~/.config/ringogpt/.env
```

RingoGPT loads configuration from these places:

```text
1. ~/.config/ringogpt/.env
2. ~/.ringogpt.env
3. .env in the current working directory
4. real shell environment variables
```

Shell environment variables have the highest priority.

This means beginners do not need to edit `.zshrc` or `.bashrc`. They can use a normal config file instead.


## Free or low-cost API options

RingoGPT does not include a shared API key.

Each user needs to bring their own API key from an AI provider.

This keeps the project safe, open-source friendly, and easy to customize.

Free tiers and free models can change over time, so always check the provider dashboard before relying on them for production work.

---

## Option 1: OpenRouter free models

OpenRouter is a good first option for testing because it supports OpenAI-compatible APIs and has free model routing.

Example `.env`:

```env
RINGOGPT_API_KEY=your_openrouter_api_key_here
RINGOGPT_BASE_URL=https://openrouter.ai/api/v1
RINGOGPT_MODEL=openrouter/free
RINGOGPT_CACHE_FILE=~/.ringogpt_cache.json
RINGOGPT_TIMEOUT=30
RINGOGPT_DEBUG=false
```

Then test:

```bash
ringogpt "show hidden files in the current directory"
```

---

## Option 2: Gemini API

Gemini API can also be used through an OpenAI-compatible endpoint.

Example `.env`:

```env
RINGOGPT_API_KEY=your_gemini_api_key_here
RINGOGPT_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
RINGOGPT_MODEL=gemini-2.5-flash
RINGOGPT_CACHE_FILE=~/.ringogpt_cache.json
RINGOGPT_TIMEOUT=30
RINGOGPT_DEBUG=false
```

Then test:

```bash
ringogpt "show disk usage in human readable format"
```

---

## Option 3: Groq

Groq is another OpenAI-compatible option and is known for fast inference.

Example `.env`:

```env
RINGOGPT_API_KEY=your_groq_api_key_here
RINGOGPT_BASE_URL=https://api.groq.com/openai/v1
RINGOGPT_MODEL=llama-3.1-8b-instant
RINGOGPT_CACHE_FILE=~/.ringogpt_cache.json
RINGOGPT_TIMEOUT=30
RINGOGPT_DEBUG=false
```

Then test:

```bash
ringogpt "find all python files in this project"
```

---

## Usage examples

Show hidden files:

```bash
ringogpt "show hidden files here"
```

Find large files:

```bash
ringogpt "find files bigger than 100MB in this directory"
```

Create folders:

```bash
ringogpt "create a folder named amir here and create folders 1 2 3 inside it"
```

Expected command:

```bash
mkdir -p amir/1 amir/2 amir/3
```

Check disk usage:

```bash
ringogpt "show disk usage in human readable format"
```

Find running Python processes:

```bash
ringogpt "show running python processes"
```

Persian example:

```bash
soal "فایل های بزرگتر از ۱۰۰ مگابایت رو پیدا کن"
```

---

## Cache

RingoGPT stores previous AI responses in a local cache file.

Default cache path:

```text
~/.ringogpt_cache.json
```

This helps reduce repeated API calls for the same request.

To clear the cache manually:

```bash
rm -f ~/.ringogpt_cache.json
```

You can change the cache path in `.env`:

```env
RINGOGPT_CACHE_FILE=~/.cache/ringogpt/cache.json
```

---

## Command timeout

RingoGPT supports a command execution timeout.

Default:

```env
RINGOGPT_TIMEOUT=30
```

If a command runs longer than the timeout, RingoGPT stops waiting and reports a timeout error.

---

## Project structure

```text
ringogpt/
├── cli.py           # CLI entry point and command execution flow
├── gpt_client.py    # AI client, prompt, JSON parsing, validation
├── cache.py         # Local cache loading and saving
├── config.py        # Environment-based configuration
├── utils.py         # Terminal color helpers
└── __init__.py
```

Other important files:

```text
README.md            # Project documentation
requirements.txt     # Python dependencies
setup.py             # Package setup and CLI entry points
.env.example         # Example environment configuration
assets/              # Project assets
```

---

## Development

Install in editable mode:

```bash
python -m pip install -e .
```

Run syntax check:

```bash
python -m compileall ringogpt
```

Check which command is being used:

```bash
which -a ringogpt
which -a soal
```

Check Git status:

```bash
git status --short
```

---

## Troubleshooting

### `command not found: python`

Use:

```bash
python3 --version
```

Then create the virtual environment with:

```bash
python3 -m venv .venv
```

---

### `Missing or placeholder API key`

Your `.env` file still has a placeholder key.

Open `.env`:

```bash
nano .env
```

Replace:

```env
RINGOGPT_API_KEY=your_api_key_here
```

with your real provider API key.

---

### `401 invalid token`

The API provider rejected your key.

Possible reasons:

* the key is wrong
* the key expired
* the key has no credit or access
* the key belongs to a different provider
* the base URL and key do not match

Check your provider dashboard and `.env` values.

---

### `405 Not Allowed`

This usually means the base URL is wrong or the provider endpoint is not compatible with the request format.

Check:

```env
RINGOGPT_BASE_URL=...
```

For OpenRouter:

```env
RINGOGPT_BASE_URL=https://openrouter.ai/api/v1
```

For Groq:

```env
RINGOGPT_BASE_URL=https://api.groq.com/openai/v1
```

For Gemini:

```env
RINGOGPT_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
```

---

### `soal` runs the wrong version

You may have an old global script installed.

Check:

```bash
which -a soal
which -a ringogpt
```

If an old global version appears in `~/.local/bin`, remove it:

```bash
rm -f ~/.local/bin/soal ~/.local/bin/ringogpt
hash -r
python -m pip install -e .
```

---

## Roadmap

Possible future improvements:

* Add `--no-execute` mode
* Add `--no-cache`
* Add `--clear-cache`
* Add provider presets
* Add safer command pattern detection
* Add test suite
* Add command history
* Add dry-run mode
* Add shell selection
* Add stronger protection for destructive commands
* Add better Persian output formatting
* Add a package release workflow
* Add examples gallery
* Add plugin system for custom command policies

---

## Ideas for contributors

This project can be extended in many directions:

* improve prompt reliability
* add unit tests
* add shell-specific modes
* add safer command validators
* add provider setup presets
* improve JSON parsing
* add CLI flags
* add logging and debug mode
* add support for local LLMs
* add offline command templates
* add a small TUI interface
* add documentation for beginners

---

## Portfolio note

RingoGPT is a small but practical AI developer tool.

It combines:

* Python packaging
* Linux CLI workflows
* OpenAI-compatible APIs
* prompt engineering
* command safety
* local caching
* environment-based configuration
* human-in-the-loop execution

The project is intentionally simple, but it shows how AI can be used as a focused utility rather than a large application.

---

## Author

Created by Amir Hossein Mousavi — Homous

Creative Technologist & Visual Problem Solver

---

## License

MIT License

---

## Disclaimer

RingoGPT generates shell commands using AI.

AI-generated commands can be wrong, incomplete, unsafe, or destructive.

Always review commands before running them.

You are responsible for what you execute on your system.
