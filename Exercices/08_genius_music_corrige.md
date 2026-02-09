Corrige - genius_music_scraping

1) Requete et headers
```python
import requests
url = 'https://genius.com/Coldplay-yellow-lyrics'
headers = {'User-Agent': 'formation-genius-scraper'}
resp = requests.get(url, headers=headers, timeout=10)
resp.raise_for_status()
html = resp.text
```

2) Extraction titres
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
# Selecteurs possibles, a ajuster selon la page.
track = soup.find('h1')
artist = soup.find('a', {'class': 'HeaderArtistAndTracklist__Artist'} )
print(track.get_text(strip=True) if track else None)
print(artist.get_text(strip=True) if artist else None)
```

3) Extraction paroles
```python
lyrics_blocks = soup.select('[data-lyrics-container="true"]')
lyrics = '\n'.join(b.get_text('\n', strip=True) for b in lyrics_blocks)
lines = [l for l in lyrics.split('\n') if l.strip()]
print(lines[:10])
```

4) Sauvegarde
```python
import json
with open('lyrics.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
meta = {'track': (track.get_text(strip=True) if track else ''), 'artist': (artist.get_text(strip=True) if artist else '')}
with open('meta.json', 'w', encoding='utf-8') as f:
    json.dump(meta, f, ensure_ascii=False, indent=2)
```

5) Respect du site
```python
import time
time.sleep(1)
```

