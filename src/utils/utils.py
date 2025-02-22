from pathlib import Path


def write_file(file_path: Path, content: str) -> None:
    with open(file_path, "w") as file:
        file.write(content)


def read_file(file_path: Path) -> str:
    with open(file_path, "r") as file:
        return file.read()
