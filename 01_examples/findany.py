import sys

if len(sys.argv) != 3:
    print("Usage: python findany.py <searchtext> <filename>")
    sys.exit(1)
searchtext = sys.argv[1]
filename = sys.argv[2]

with open(filename, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip()
        if searchtext.lower() in line.lower():
            print(line)
