import os
import subprocess
import sys
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, "bot_console.log")


def main():
    while True:
        with open(LOG_PATH, "ab", 0) as log:
            print("Starting bot...", flush=True)
            proc = subprocess.Popen(
                [sys.executable, "bot.py"],
                cwd=BASE_DIR,
                stdout=log,
                stderr=subprocess.STDOUT,
            )
            code = proc.wait()
        print(f"Bot exited with code {code}. Restarting in 5s...", flush=True)
        time.sleep(5)


if __name__ == "__main__":
    main()
