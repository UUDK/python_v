import xml.etree.ElementTree as ET
from pprint import pprint

persons: list[dict[str, str]] = []
books: list[dict[str, str]] = []

tree = ET.parse('sample2.xml')
root = tree.getroot()

for element in root:
    d = {}
    for field in element:
        d[field.tag] = field.text
    if element.tag == 'book':
        books.append(d)
    else:  # element.tag == 'person'
        persons.append(d)

pprint(persons)
pprint(books)

# root = ET.fromstring("<a></a>")