# Create a script that gets a filename from commandline and reads it in as either JSON, CSV, or Pickle depending on the filename extension

import csv
import json
import pickle
import sys

from pprint import pprint

filename = sys.argv[1]

if filename.endswith(".json"):
    ...
    data = ...
elif filename.endswith(".csv"):
    ...
elif filename.endswith(".pickle"):
    ...
else:
    print("Invalid file format: must be JSON, CSV, or Pickle")
    sys.exit(1)

pprint(data)
