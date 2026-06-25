import sys
import subprocess

from .gpt_client import ask_command, RingoGPTError
from .cache import load_cache, save_cache
from .utils import green, red, yellow


def _print_usage():
    print('Usage: ringogpt "your request"')
    print('   or: soal "your request"')


def _print_danger(danger):
    if danger == "high":
        print(red("Danger: HIGH"))
    elif danger == "medium":
        print(yellow("Danger: MEDIUM"))
    else:
        print(green("Danger: LOW"))


def _confirm_execution(danger):
    if danger == "high":
        print()
        print(red("This command is marked as HIGH risk."))
        print(red('Type "RUN" exactly if you still want to execute it.'))
        return input("Confirm: ").strip() == "RUN"

    answer = input("Run command? (y/N): ").strip().lower()
    return answer == "y"


def main():
    if len(sys.argv) < 2:
        _print_usage()
        return 1

    question = " ".join(sys.argv[1:]).strip()

    if not question:
        _print_usage()
        return 1

    cache = load_cache()

    try:
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

    except RingoGPTError as exc:
        print(red("RingoGPT error:"))
        print(exc)
        return 1
    except Exception as exc:
        print(red("Unexpected error:"))
        print(exc)
        return 1

    print(green("Command:"))
    print(command)
    print()

    print("Explanation:")
    print(explanation)
    print()

    _print_danger(danger)
    print()

    if _confirm_execution(danger):
        print()
        print(yellow("Running command..."))
        completed = subprocess.run(command, shell=True)
        return completed.returncode

    print("Command not executed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
