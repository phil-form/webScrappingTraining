Corrige - wikipedia

1) Requete avec User-Agent
```python
import requests
url = 'https://en.wikipedia.org/wiki/Internet'
headers = {'User-Agent': 'formation-wiki-scraper'}
resp = requests.get(url, headers=headers, timeout=10)
resp.raise_for_status()
html = resp.text
```

2) Parsing
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
page_title = soup.title.text
h2 = [t.get_text(strip=True) for t in soup.find_all('h2')]
h3 = [t.get_text(strip=True) for t in soup.find_all('h3')]
print(page_title)
```

3) Nettoyage
```python
titles = [t for t in h2 + h3 if t]
print(len(titles))
```

4) Sauvegarde
```python
import csv
rows = [['niveau', 'texte']] + [['h2', t] for t in h2] + [['h3', t] for t in h3]
with open('wiki_titles.csv', 'w', newline='', encoding='utf-8') as f:
    csv.writer(f).writerows(rows)
```

5) Regex
```python
import re
text = soup.get_text(' ', strip=True)
years = re.findall(r'\b(19|20)\d{2}\b', text)
print(len(years))
```

