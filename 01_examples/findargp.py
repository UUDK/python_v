import argparse

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Finds text in file")
    parser.add_argument('--linenumbers', '-l', help='Print the line number', action="store_true")
    parser.add_argument('searchtext', help='The search text', type=str)
    parser.add_argument('filename', help='File to search', type=str)
    args = parser.parse_args()

    lineno = 0
    with open(args.filename, 'r', encoding='utf-8') as f:
        for line in f:
            lineno += 1
            line = line.rstrip()
            if args.searchtext.lower() in line.lower():
                if args.linenumbers:
                    print(f"{lineno:5d} ", end="")
                print(line)
