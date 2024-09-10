import csv

def clean_pop(city):
    val = city['population']
    try:
        return int(float(val))
    except ValueError:
        return 0
        
cities = []

with open('worldcities.csv', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, dialect=csv.excel)
    header = None
    for row in spamreader:
            if header is None:
                header = row
            else:
                city = dict(zip(header, row))
                cities.append(city)



cities.sort(key=clean_pop)
print(cities[0], cities[-1])

count = 1
start = 0
step = 1000
while start < len(cities):
    filename = f"city{count:04d}.csv"
    with open(filename, 'w', encoding='utf-8', newline='') as csv_out:
        fieldnames = list(cities[0].keys())
        writer = csv.DictWriter(csv_out, fieldnames=fieldnames,
                                dialect=csv.excel, quoting=csv.QUOTE_NONNUMERIC)
        for city in cities[start:start + step]:
            writer.writerow(city)
    start += step
    count += 1
               
