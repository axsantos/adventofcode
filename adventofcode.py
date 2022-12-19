import requests
from pathlib import Path

def get_puzzle_input(year, day):
    p = Path(".")
    in_f = p / "input.txt"
    token_f = p / "token.txt"
    session_key = token_f.open().read().strip()

    if not in_f.exists():
        print("Downloading...")
        cookie={"session": session_key}
        res=requests.get(
            f"https://adventofcode.com/{year}/day/{day}/input", cookies = cookie)

        in_f.open("w").write(res.text)
    else:
        print("Using cached input")

get_puzzle_input(2022, 9)
