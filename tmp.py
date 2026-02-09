# Performance and Async Processing Notebook
# Auteur: ChatGPT
# Sujet: Questions de performances dans le scraping

# ---
# 1. Threads et GIL
import threading
import time

# Exemple simple de thread

def travail(numero):
    print(f'Démarrage du travail {numero}')
    time.sleep(1)
    print(f'Fin du travail {numero}')

threads = []
for i in range(3):
    t = threading.Thread(target=travail, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Note: Python a le GIL (Global Interpreter Lock) qui empêche les threads CPU-bound d'être vraiment parallèles.


# ---
# 2. Utiliser plusieurs coeurs avec multiprocessing
from multiprocessing import Process, cpu_count

print('\nNombre de coeurs disponibles:', cpu_count())

def travail_cpu(numero):
    print(f'Traitement CPU {numero} démarré')
    total = sum(i*i for i in range(10**6))
    print(f'Traitement CPU {numero} terminé')

processes = []
for i in range(2):
    p = Process(target=travail_cpu, args=(i,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()


# ---
# 3. Programmation I/O asynchrone
import asyncio

async def tache_io(numero):
    print(f'Tâche {numero} démarrée')
    await asyncio.sleep(1)  # simule une I/O non bloquante
    print(f'Tâche {numero} terminée')

async def main():
    await asyncio.gather(*(tache_io(i) for i in range(3)))

asyncio.run(main())


# ---
# 4. Performances et éthique
# Toujours respecter les limites de requêtes des sites, utiliser delays, caches et vérifier robot.txt.

# ---
# 5. Utilisation d’une forme de cache
import os
import pickle
import random

cache_file = 'cache.pkl'

# Exemple simple de cache disque
if os.path.exists(cache_file):
    with open(cache_file, 'rb') as f:
        cache = pickle.load(f)
else:
    cache = {}

url = 'https://example.com/data'
if url in cache:
    print('\nDonnées depuis le cache')
    data = cache[url]
else:
    print('\nDonnées simulées et mise en cache')
    data = {'value': random.randint(0,100)}
    cache[url] = data
    with open(cache_file, 'wb') as f:
        pickle.dump(cache, f)

print('Données:', data)


# ---
# 6. Introduire un délai aléatoire
import time

delay = random.uniform(1, 3)
print(f'Pause aléatoire de {delay:.2f} secondes')
time.sleep(delay)


# ---
# 7. Vérifier le fichier robots.txt
import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
rp.set_url('https://jsonplaceholder.typicode.com/robots.txt')
rp.read()
can_fetch = rp.can_fetch('*', 'https://jsonplaceholder.typicode.com/posts')
print(f'Peut-on scraper la page? {can_fetch}')


# ---
# 8. Exercices
# 1. Modifier le cache pour utiliser Redis (requiert installation redis-py et serveur Redis)
# 2. Comparer performance entre threading, multiprocessing et asyncio
# 3. Implémenter un scraper respectueux qui lit robots.txt, utilise cache et délai aléatoire
