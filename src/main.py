from model.chat import chat
from pathlib import Path
from utils.utils import write_file, read_file
from fire import Fire

BABEL_PROMPT_PATH = Path(__file__).parent.parent / "data" / "prompt" / "babel.txt"
OUTPUT_PATH = Path(__file__).parent.parent / "data" / "output" / "output.txt"


def main():
    prompt = read_file(BABEL_PROMPT_PATH)
    response = chat(prompt)
    write_file(OUTPUT_PATH, response)

if __name__ == "__main__":
    Fire(main)
    
