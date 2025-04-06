# Create a function that reads the `numbers.txt` file, adds the numbers, and returns the sum of the numbers.

def sum_file(filename):
    sum = 0
    with open(filename, "r", encoding="utf-8") as f:
        ...
    return sum


if __name__ == "__main__":
    sum = sum_file("numbers.txt")
    print(f"The sum of the numbers is : {sum}")

