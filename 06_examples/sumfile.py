def sum_file(filename):
    sum = 0
    with open(filename, 'r', encoding='utf-8') as f:
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
        try:
            sum = sum_file(filename)
        except OSError as e:
            print("The file could not be read")
        else:
            print("The sum of the numbers is :", sum)
            break
