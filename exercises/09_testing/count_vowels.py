# Write script with a function that counts the number of vowels (a, e, i, o, u, y) in a text


def count_vowels(text):
    vowels = {"a", "e", "i", "o", "u", "y"}
    ...

if __name__ == "__main__":
    filename = "pythonbeginners.txt"
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    print(count_vowels(text))

