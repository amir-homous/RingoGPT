# RingoGPT

A lightweight AI-powered CLI assistant that converts natural language into Linux shell commands.

RingoGPT lets you ask for terminal commands in plain English or Persian, reviews the command with an explanation and risk level, and only runs it after your confirmation.

> Built for people who use Linux often, but do not want to memorize every command.

---

## What it does

Instead of searching for a command manually, you can ask:

```bash
ringogpt "show hidden files in the current directory"
```

or:

```bash
soal "find all .log files in this folder"
```

RingoGPT returns:

```text
Command:
find . -name "*.log"

Explanation:
This command searches the current directory and all subdirectories for files ending in .log.

Danger: LOW

Run command? (y/N):
```

---

## Features

* Convert natural language into Linux shell commands
* Works with English and Persian requests
* Shows the generated command before running it
* Explains what the command does
* Classifies command risk as low, medium, or high
* Requires confirmation before execution
* Uses stricter confirmation for high-risk commands
* Supports local response caching
* Supports OpenAI-compatible API providers
* Lightweight Python package with simple CLI commands

---

## Safety-first behavior

RingoGPT does **not** silently execute generated commands.

Every generated command is shown first with:

* the command
* an explanation
* a danger level
* a confirmation prompt

For high-risk commands, RingoGPT requires stronger confirmation.

Example high-risk categories include:

* deleting files
* changing permissions recursively
* formatting disks
* shutting down or rebooting
* modifying system files

Even with these protections, always review commands before running them.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/amir-homous/ringogpt.git
cd ringogpt
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
ringogpt "list files in current directory"
```

```bash
soal "list files in current directory"
```

---

## Configuration

RingoGPT reads configuration from environment variables or a `.env` file.

Create a `.env` file:

```bash
cp .env.example .env
```

Then edit it:

```bash
nano .env
```

Example:

```env
RINGOGPT_API_KEY=your_api_key_here
RINGOGPT_BASE_URL=https://api.openai.com/v1
RINGOGPT_MODEL=gpt-4o-mini
RINGOGPT_CACHE_FILE=~/.ringogpt_cache.json
```

---

## API providers

RingoGPT is designed to work with OpenAI-compatible API providers.

You can use providers such as:

* OpenAI
* OpenRouter
* Groq
* Gemini OpenAI-compatible endpoint
* GapGPT or other compatible providers
* Any custom OpenAI-compatible endpoint

Example OpenRouter configuration:

```env
RINGOGPT_API_KEY=your_openrouter_api_key_here
RINGOGPT_BASE_URL=https://openrouter.ai/api/v1
RINGOGPT_MODEL=your_model_slug_here
```

Example Groq configuration:

```env
RINGOGPT_API_KEY=your_groq_api_key_here
RINGOGPT_BASE_URL=https://api.groq.com/openai/v1
RINGOGPT_MODEL=your_model_slug_here
```

Example custom provider:

```env
RINGOGPT_API_KEY=your_api_key_here
RINGOGPT_BASE_URL=https://your-provider.example.com/v1
RINGOGPT_MODEL=your-model-name
```

Do not commit your `.env` file.

---

## Usage

Basic command:

```bash
ringogpt "show hidden files"
```

Persian example:

```bash
soal "فایل های مخفی این پوشه رو نشون بده"
```

Another example:

```bash
ringogpt "find large files bigger than 100MB"
```

RingoGPT will show the command, explanation, and risk level before asking whether to run it.

---

## Cache

RingoGPT stores previous responses in a local cache file to reduce repeated API requests.

Default cache path:

```text
~/.ringogpt_cache.json
```

You can change it:

```env
RINGOGPT_CACHE_FILE=~/.cache/ringogpt/cache.json
```

---

## Project structure

```text
ringogpt/
├── cli.py           # CLI entry point and command execution flow
├── gpt_client.py    # AI provider client, prompt, JSON parsing, validation
├── cache.py         # Local cache loading and saving
├── config.py        # Environment-based configuration
├── utils.py         # Terminal color helpers
└── __init__.py
```

---

## Development

Install locally in editable mode:

```bash
python -m pip install -e .
```

Run a syntax check:

```bash
python -m compileall ringogpt
```

Check Git status:

```bash
git status --short
```

---

## Roadmap

Planned improvements:

* Add `--no-execute` mode
* Add `--no-cache` option
* Add `--clear-cache`
* Add safer command pattern detection
* Add test suite
* Add provider presets
* Add better shell detection
* Add command history
* Add dry-run mode
* Improve Persian output formatting

---

## Why I built this

I built RingoGPT because I often know what I want to do in Linux, but I do not always remember the exact command.

The goal is not to replace learning Linux.

The goal is to make the command line easier, safer, and faster for everyday tasks.

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

AI-generated commands can be wrong, incomplete, or dangerous.

Always review commands before running them. You are responsible for what you execute on your system.
