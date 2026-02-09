Corrige - 03_threading

1) Threads I/O
```python
import threading, time, random

start = time.time()

def worker(i):
    time.sleep(random.uniform(0.2, 0.6))
    print('done', i)

threads = [threading.Thread(target=worker, args=(i,)) for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()
print('elapsed', round(time.time() - start, 2))
```

2) Multiprocessing
```python
from multiprocessing import Process
import time

def cpu_task():
    return sum(i*i for i in range(10**6))

def run_mp():
    procs = [Process(target=cpu_task) for _ in range(2)]
    for p in procs: p.start()
    for p in procs: p.join()

start = time.time(); run_mp(); print('mp', round(time.time()-start,2))
start = time.time(); cpu_task(); cpu_task(); print('seq', round(time.time()-start,2))
```

3) Asyncio
```python
import asyncio, time

async def job(i):
    await asyncio.sleep(1)
    return i

start = time.time()
asyncio.run(asyncio.gather(*(job(i) for i in range(3))))
print('elapsed', round(time.time()-start,2))
```

4) Rate limiting
```python
import time

class SimpleRateLimiter:
    def __init__(self, max_per_sec):
        self.min_interval = 1.0 / max_per_sec
        self._last = 0.0
    def wait(self):
        elapsed = time.time() - self._last
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self._last = time.time()

limiter = SimpleRateLimiter(5)
for i in range(10):
    limiter.wait()
    print(i, round(time.time(), 2))
```

5) Cache
```python
import pickle, os

path = 'cache.pkl'
cache = {}
if os.path.exists(path):
    with open(path, 'rb') as f:
        cache = pickle.load(f)

cache['new_key'] = {'value': 123}
with open(path, 'wb') as f:
    pickle.dump(cache, f)

print('keys', list(cache.keys()))
```

