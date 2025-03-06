# Create a script that finds all python files and prints the filenames and the number of lines in the file

from pathlib import Path

for file in Path().rglob("*.py"):
    with file.open("r", encoding="utf-8") as f:
        count = 0
        for _ in f:
            count += 1
        print(f"{file.name} has {count} lines")
