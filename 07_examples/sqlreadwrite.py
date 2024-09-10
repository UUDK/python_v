import sqlite3

data = [
    {'name': 'Anders', 'age': 34, 'height': 1.82},
    {'name': 'Benny', 'age': 51, 'height': 1.81},
    {'name': 'Charlie', 'age': 72, 'height': 1.84},
    {'name': 'Dennis', 'age': 31, 'height': 1.78},
    {'name': 'Eric', 'age': 45, 'height': 1.83},
]

con = sqlite3.connect("data.sqlite3")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS person")

cur.execute("""
    CREATE TABLE person (
        name VARCHAR(80),
        age INT,
        height real
    )
""")

for person in data:
    t = (person['name'], person['age'], person['height'])
    cur.execute("""
        INSERT INTO person
        (name, age, height)
        VALUES (?, ?, ?)
    """, t)

res = cur.execute("SELECT * FROM person ORDER BY name")
for row in res:
    print(row)

cur.close()
con.commit()
con.close()
