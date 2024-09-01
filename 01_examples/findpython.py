with open("pythonbeginners.txt", 'r', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip()
        if "python" in line.lower():
            print(line)
