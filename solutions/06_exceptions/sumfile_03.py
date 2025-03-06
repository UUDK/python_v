# (Create a function that reads the `numbers.txt` file, adds the numbers, and returns the sum of the numbers.)
# (Add error handling so that the lines that are not numbers are ignored.)
# Create a main part that asks for the filename and handles if the filename does not exist.

def sum_file(filename):
    sum = 0
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip()
            try:
                val = int(line)
                sum += val
            except ValueError:
                pass
    return sum


if __name__ == "__main__":
    while True:
        filename = input("Which file to sum : ")
        if not filename:
            break
        try:
            sum = sum_file(filename)
        except OSError as e:
            print(f"The file could not be read {e}")
        else:
            print(f"The sum of the numbers is : {sum}")
            break
