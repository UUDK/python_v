# Read the file and place the data in a list of tuples

from pprint import pprint

with open("passwd.txt", "r", encoding="utf-8") as f:
    data_list = []
    for line in f:
        line = line.rstrip()
        # print(line)
        record = tuple(line.split(":"))
        data_list.append(record)

pprint(data_list, width=120)
