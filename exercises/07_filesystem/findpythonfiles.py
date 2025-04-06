# Create a script that finds all python files and prints the filenames and the number of lines in the file

from pathlib import Path

for file in Path().rglob("*.py"):
    ...
