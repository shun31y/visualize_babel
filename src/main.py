from pathlib import Path

from fire import Fire

from model.chat import chat
from utils.utils import read_file, write_file

BABEL_PROMPT_PATH = Path(__file__).parent.parent / "data" / "prompt" / "babel.txt"
OUTPUT_PATH = Path(__file__).parent.parent / "data" / "output" / "output.txt"


def main():
    prompt = read_file(BABEL_PROMPT_PATH)
    response = chat(prompt)
    write_file(OUTPUT_PATH, response)


if __name__ == "__main__":
    Fire(main)
