Corrige - 01_file_management

1) Parcours et filtres
```python
import os

base = 'example'
for root, _, files in os.walk(base):
    for name in files:
        if not name.endswith('.txt'):
            rel_path = os.path.relpath(os.path.join(root, name), start=base)
            print(rel_path)
```

2) Encodage
```python
text = 'Bonjour ete 😀'
path = 'exemple_unicode.txt'
with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()
print(len(content))
```

3) CSV
```python
import csv
rows = [
    ['id', 'nom', 'ville'],
    [1, 'Alice', 'Paris'],
    [2, 'Bob', 'Lyon'],
]
with open('personnes.csv', 'w', newline='', encoding='utf-8') as f:
    csv.writer(f).writerows(rows)

with open('personnes.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = [{'id': int(r['id']), 'nom': r['nom'], 'ville': r['ville']} for r in reader]
print(data)
```

4) JSON
```python
import json
payload = {'personnes': [
    {'nom': 'A', 'age': 25},
    {'nom': 'B', 'age': 35},
    {'nom': 'C', 'age': 40},
]}
with open('personnes.json', 'w', encoding='utf-8') as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)
with open('personnes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
print([p for p in data['personnes'] if p['age'] > 30])
```

5) XML
```python
import xml.etree.ElementTree as ET

root = ET.Element('produits')
for nom, prix in [('A', '9.99'), ('B', '4.50'), ('C', '12.00')]:
    p = ET.SubElement(root, 'produit')
    ET.SubElement(p, 'nom').text = nom
    ET.SubElement(p, 'prix').text = prix

ET.ElementTree(root).write('produits.xml', encoding='utf-8', xml_declaration=True)

root = ET.parse('produits.xml').getroot()
for p in root.findall('produit'):
    print(p.find('nom').text, p.find('prix').text)
```

6) Generateurs
```python
def lignes_non_vides(path):
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                yield line

print(list(lignes_non_vides('exemple.txt')))
```

