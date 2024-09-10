import csv

with open('data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, dialect=csv.excel)
    for row in spamreader:
            name = row[0]
            age = row[1]
            height = row[2]
            print(f"{name=} {age=} {height=}")
