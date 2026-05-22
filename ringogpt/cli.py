import sys
import subprocess
from .gpt_client import ask_command
from .cache import load_cache, save_cache
from .utils import green, red, yellow


def main():

    if len(sys.argv) < 2:
        print('Usage: ringogpt "your request"')
        return

    question = " ".join(sys.argv[1:])

    cache = load_cache()

    if question in cache:
        result = cache[question]
        print("(cached result)\n")
    else:
        print("Asking RingoGPT...\n")
        result = ask_command(question)
        cache[question] = result
        save_cache(cache)

    command = result["command"]
    explanation = result["explanation"]
    danger = result["danger"]

    print(green("Command:"))
    print(command)
    print()

    print("Explanation:")
    print(explanation)
    print()

    if danger == "high":
        print(red("Danger: HIGH"))
    elif danger == "medium":
        print(yellow("Danger: MEDIUM"))
    else:
        print(green("Danger: LOW"))

    print()

    run = input("Run command? (y/n): ")

    if run.lower() == "y":
        subprocess.run(command, shell=True)
