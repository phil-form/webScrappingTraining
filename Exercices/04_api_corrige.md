Corrige - 04_api

1) Auth headers
```python
import os
TOKEN = os.getenv('API_TOKEN', 'token_demo')
headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Accept': 'application/json',
}
print(headers)
```

2) REST URL
```python
from urllib.parse import urlparse, parse_qs
url = 'https://api.exemple.com/v1/tweets?limit=10&lang=fr'
p = urlparse(url)
print(p.scheme, p.netloc, p.path, parse_qs(p.query))
```

3) Retry
```python
import time

def retry(op, max_tries=3, base_delay=0.2):
    for i in range(1, max_tries + 1):
        try:
            return op()
        except Exception:
            if i == max_tries:
                raise
            time.sleep(base_delay * (2 ** (i - 1)))

n = {'c': 0}

def unstable():
    n['c'] += 1
    if n['c'] < 3:
        raise RuntimeError('temp')
    return 'OK'

print(retry(unstable))
```

4) Rate limiting
```python
import time

class SimpleRateLimiter:
    def __init__(self, rps):
        self.min_interval = 1.0 / rps
        self._last = 0.0
    def wait(self):
        elapsed = time.time() - self._last
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self._last = time.time()

limiter = SimpleRateLimiter(3)
for i in range(6):
    limiter.wait()
    print(i, round(time.time(), 2))
```

5) Errors
```python
class ApiError(Exception):
    pass
class ClientError(ApiError):
    pass
class ServerError(ApiError):
    pass

def handle(code):
    if 400 <= code < 500:
        raise ClientError(code)
    if 500 <= code < 600:
        raise ServerError(code)
    return 'OK'

try:
    handle(404)
except ApiError as e:
    print('error', e)
```

6) Logging
```python
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')
log = logging.getLogger('api')
log.debug('debug')
log.info('info')
log.warning('warn')
```

7) Client API
```python
import requests
import time

class Client:
    def __init__(self, base):
        self.base = base
    def get(self, path, retries=3):
        url = self.base + path
        for i in range(retries):
            r = requests.get(url, timeout=5)
            if r.status_code in (429, 503):
                time.sleep(0.5)
                continue
            r.raise_for_status()
            return r.json()
        raise RuntimeError('retry failed')

c = Client('https://jsonplaceholder.typicode.com')
print(c.get('/posts/1')['id'])
```

