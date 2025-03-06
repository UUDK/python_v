# Create a script that gets a filename from commandline and reads it in as either JSON, CSV, or Pickle depending on the filename extension

import csv
import json
import pickle
import sys

from pprint import pprint

filename = sys.argv[1]

if filename.endswith(".json"):
    with open(filename, "r") as f:
        data = json.load(f)
elif filename.endswith(".csv"):
    with open(filename, "r", newline="") as f:
        reader = csv.DictReader(f)
        data = list(reader)
elif filename.endswith(".pickle"):
    with open(filename, "rb") as f:
        data = pickle.load(f)
else:
    print("Invalid file format: must be JSON, CSV, or Pickle")
    sys.exit(1)

pprint(data)
