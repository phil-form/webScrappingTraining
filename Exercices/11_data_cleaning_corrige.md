Corrige - Exercices pratiques (Nettoyage de donnees)

Donnees d exemple
```python
rows = [
    {'nom': ' Alice ', 'age': '30', 'ville': 'Paris', 'salaire': 3200, 'date': '2024-01-10'},
    {'nom': 'Bob', 'age': None, 'ville': 'Lyon', 'salaire': 8000, 'date': '2023-12-01'},
    {'nom': '  Clara', 'age': '25', 'ville': None, 'salaire': 2500, 'date': '2024-02-05'},
    {'nom': 'David', 'age': '40', 'ville': 'Paris', 'salaire': None, 'date': '2024-03-20'},
]
```

1) Suppression des valeurs manquantes
```python
clean = [r for r in rows if all(v is not None for v in r.values())]
print(clean)
```

2) Remplacement des valeurs manquantes
```python
ages = [int(r['age']) for r in rows if r['age'] is not None]
mean_age = sum(ages) / len(ages)

for r in rows:
    if r['age'] is None:
        r['age'] = int(mean_age)
    if r['ville'] is None:
        r['ville'] = 'inconnu'
    if r['salaire'] is None:
        r['salaire'] = 0
```

3) Nettoyage et standardisation des chaines
```python
for r in rows:
    r['nom'] = r['nom'].strip().lower()
```

4) Conversion des types
```python
from datetime import datetime
for r in rows:
    r['age'] = int(r['age'])
    r['date'] = datetime.strptime(r['date'], '%Y-%m-%d').date()
```

5) Traitement des valeurs extremes (outliers)
```python
filtered_salary = [r for r in rows if 1000 <= r['salaire'] <= 5000]
print(filtered_salary)
```

6) Encodage des variables categorielles
```python
villes = sorted({r['ville'] for r in rows})
city_to_code = {v: i for i, v in enumerate(villes)}
for r in rows:
    r['ville_code'] = city_to_code[r['ville']]
print(city_to_code)
```

7) Filtrage et tri des donnees
```python
filtered = [r for r in rows if r['age'] >= 30]
filtered.sort(key=lambda r: (r['age'], r['nom']))
print(filtered)
```

