# Read in the file passwd.txt and print the lines

with open("passwd.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.rstrip()
        print(line)
