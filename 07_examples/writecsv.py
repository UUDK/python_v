import csv

data = [
    {'name': 'Anders', 'age': 34, 'height': 1.82},
    {'name': 'Benny', 'age': 51, 'height': 1.81},
    {'name': 'Charlie', 'age': 72, 'height': 1.84},
    {'name': 'Dennis', 'age': 31, 'height': 1.78},
    {'name': 'Eric', 'age': 45, 'height': 1.83},
]

with open('data.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, dialect=csv.excel, quoting=csv.QUOTE_NONNUMERIC)
    spamwriter.writerow(list(data[0].keys()))
    for person in data:
        spamwriter.writerow(list(person.values()))
