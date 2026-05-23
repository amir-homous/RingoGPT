# 🚀 RingoGPT

RingoGPT is a lightweight command-line tool that converts natural language requests into Linux shell commands using GPT.

It helps you quickly generate commands, review them safely, and optionally execute them after your confirmation.

---

## ✨ Features

- 🗣️ Convert natural language into Linux commands  
- 🔒 JSON-only model responses for safer parsing  
- 💾 Local caching to avoid repeated API calls  
- 🖥️ Interactive CLI for reviewing commands before execution  
- 🌐 Configurable OpenAI-compatible API endpoint  
- 🧩 Simple and lightweight project structure  

---

## 📁 Project Structure

```text
ringogpt/
├── cli.py           # Command-line interface, input/output handling
├── gpt_client.py    # GPT API client, JSON parsing
├── cache.py         # Local cache management
├── config.py        # Configuration (API key, URL, model)
├── README.md        # This documentation
└── ...
```

## ⚙️ Requirements
- Python 3.9 or newer
- Valid API key
- Required Python packages (installed during setup)


## 🛠️ Installation


1. Clone the repo:

``` bash
git clone https://github.com/USERNAME/ringogpt.git
cd ringogpt
``` 


2.	Create and activate a virtual environment:
3. Clone the repo:
Linux / macOS:


```bash
python3 -m venv .venv
source .venv/bin/activate
Windows:
```

content_copy
bash

note_add
ویرایش با Canvas
python -m venv .venv
.venv\Scripts\activate
Install the project

content_copy
bash

note_add
ویرایش با Canvas
pip install -e .
🔧 Configuration
Settings are read from config.py.

API key must be set as an environment variable, e.g.:

content_copy
bash

note_add
ویرایش با Canvas
export RINGOGPT_API_KEY="your_api_key_here"
Base URL:

content_copy
python

note_add
ویرایش با Canvas
https://api.gapgpt.app/v1
Model:

content_copy
python

note_add
ویرایش با Canvas
gpt-4o
You may create a .env file by copying .env.example:


content_copy
bash

note_add
ویرایش با Canvas
cp .env.example .env
and then edit it to add your key.

🚀 Usage
Run the CLI with a natural language request:


content_copy
bash

note_add
ویرایش با Canvas
soal "list files in the current directory"
Example:


content_copy
bash

note_add
ویرایش با Canvas
soal "show hidden files only"
⚙️ How It Works
User input: cli.py reads your natural language request.
Cache lookup: Checks if the prompt response exists locally.
Model request: If no cached result, gpt_client.py calls GPT API.
JSON parsing: Parses JSON with:

content_copy
json

note_add
ویرایش با Canvas
{
  "command": "...",
  "explanation": "...",
  "danger": "LOW|MEDIUM|HIGH"
}
User confirmation: Shows command and explanation, asks to approve.
Execution: If approved, runs command via shell.
💾 Cache Behavior
Stores previous responses locally for speed and API usage reduction.
cache.py manages reading/writing JSON cache files.
⚠️ Safety Notes
Always review commands before running!
Avoid running unknown or destructive commands like rm -rf, chmod, dd, etc.
Model output must be valid JSON, else parsing fails.
🔍 Example Workflow

content_copy
bash

note_add
ویرایش با Canvas
soal "find all .log files in the current directory"
Output example:


content_copy
text

note_add
ویرایش با Canvas
Command: find . -name "*.log"
Explanation: This command searches for .log files recursively.
Danger: LOW

Run this command? [y/N]:
🛠️ Development
Adjust prompts or parsing in gpt_client.py
Modify CLI logic in cli.py
Improve cache code in cache.py
Update settings in config.py
❓ Troubleshooting
soal command not found:

Check $PATH. Add if needed (example for bash):


content_copy
bash

note_add
ویرایش با Canvas
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
JSON Parse errors:

Ensure model returns JSON only.
Enable debug if available.
Clear corrupted cache entries.
API Key issues:

Verify RINGOGPT_API_KEY is correctly set and has access.
🎯 Project Philosophy
Minimal and clean code
Lightweight dependencies
Safe default CLI flow
Efficient local caching
🙌 Contributing
Improve prompts, error handling, caching
Add tests and polish CLI output
Suggested workflow:

Fork
Branch
Code
Test
Pull request
📜 License
MIT License

❓ FAQ
Is it safe?

Shows command first; you must approve before running.

Can I change the model?

Yes, configure in config.py.

Is caching enabled?

Yes, responses are cached locally.

What if model output is invalid?

Parsing fails; check prompt instructions.

✒️ Author
[ homous ] Amir

⚠️ Disclaimer
The tool generates shell commands that can affect your system. Use it responsibly by reviewing commands before execution.


content_copy
text

---
