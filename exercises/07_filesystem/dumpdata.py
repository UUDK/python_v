# Create a script that dumps the above data to three files named `data.json`, `data.csv` and `data.pickle`.

import csv
import json
import pickle

data = [
    {"name": "Andrew", "age": 34, "height": 1.82},
    {"name": "Ben", "age": 51, "height": 1.81},
    {"name": "Charlie", "age": 72, "height": 1.84},
    {"name": "Dennis", "age": 31, "height": 1.78},
    {"name": "Eric", "age": 45, "height": 1.83},
]

with open("data.json", "w") as f:
    ...

with open("data.csv", "w", newline="") as f:
    ...

with open("data.pickle", "wb") as f:
    ...
