Corrige - 02_web_scrapping_base

1) HTTP basics
```python
from urllib.parse import urlparse, parse_qs

def describe(url):
    p = urlparse(url)
    return {
        'schema': p.scheme,
        'host': p.netloc,
        'path': p.path,
        'params': parse_qs(p.query),
    }

print(describe('https://example.com/a?x=1&y=2'))
print(describe('http://api.test.local/v1/items?id=9'))
```

2) Requests GET + timeout
```python
import requests
url = 'https://jsonplaceholder.typicode.com/posts/1'
resp = requests.get(url, timeout=5)
resp.raise_for_status()
print(resp.json()['id'])
```

3) Requests params + headers
```python
import requests
url = 'https://jsonplaceholder.typicode.com/posts'
params = {'userId': 1}
headers = {'User-Agent': 'formation-scraping'}
resp = requests.get(url, params=params, headers=headers, timeout=5)
resp.raise_for_status()
print(len(resp.json()))
```

4) SQLAlchemy CRUD
```python
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    body = Column(Text)

engine = create_engine('sqlite:///ex_posts.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()
posts = [
    Post(id=1, title='A', body='Body A'),
    Post(id=2, title='B', body='Body B'),
    Post(id=3, title='C', body='Body C'),
]
session.add_all(posts)
session.commit()

print([p.title for p in session.query(Post).all()])
```

5) BeautifulSoup
```python
from bs4 import BeautifulSoup
html = '<a href="https://example.com">A</a><a href="/b">B</a>'
soup = BeautifulSoup(html, 'html.parser')
links = [a['href'] for a in soup.find_all('a')]
print([l for l in links if 'example' in l])
```

6) Scraping responsable
```python
import time

def safe_get(url, delay=1):
    time.sleep(delay)
    # ici on ferait requests.get(url)
    return url

print(safe_get('https://example.com'))
```

