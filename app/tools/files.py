""" File system tools

this module contains safe, read-only operations that allow 
sherlsky to inspect projects without modifying them

IMPORTANT 
this function does not write to disk.
they only read information
"""

from pathlib import Path

def read_file(path: str) -> str:
    
    file = Path(path)

    if not file.exists():
        raise FileNotFoundError(f"{path} does not exist")
    
    if not file.is_file():
        raise ValueError(f"{path} is not a file.")

    return file.read_text(encoding="utf-8")

def list_directory(path: str) -> list[str]:
    """
    return every file and folder in the directory
    hidden folders like .git are ignored
    """
    directory = Path(path)

    if not directory.exists():
        raise FileNotFoundError(path)
    
    ignored = {
        ".git",
        ".venv",
        "__pycache__",
        "node modules",
    }

    items = []

    for item in directory.iterdir():

        if item.name in ignored:
            continue

        items.append(item.name)

    return sorted(items)
