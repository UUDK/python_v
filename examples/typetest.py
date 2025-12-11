from typing import List

def process_strings(data: List[str]) -> List[str]:
    """Process a list of strings and return a sorted list of strings."""
    if not data:
        return "No data"
    return sorted(data)

if __name__ == "__main__":
    sample1: List[str] = ["banana", "apple", "cherry"]
    result1: List[str] = process_strings(sample1)
    for item in result1:
        print(item)
    sample2: List[str] = []
    result2: List[str] = process_strings(sample2)
    for item in result2:
        print(item)