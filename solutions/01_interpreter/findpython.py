# Create a script that can find all lines in the file
# pythonbeginners.txt that has the word "python" in it

with open("pythonbeginners.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.rstrip()
        if "python" in line.lower():
            print(line)
