
Apercu

Ce depot contient des notebooks de formation (Python, web scraping, APIs, threading, Scrapy, Selenium) et des mini projets associes.

Notebooks disponibles

01_file_management.ipynb
- Gestion de fichiers, encodage, CSV, JSON, XML, generateurs.

02_web_scrapping_base.ipynb
- HTTP, requests, SQLAlchemy, BeautifulSoup.

03_threading.ipynb
- Threads, multiprocessing, asyncio, cache, bonnes pratiques reseau.

04_api.ipynb
- Auth, REST, retry, rate limiting, erreurs, logging, client API.

05_scrapy.ipynb
- Introduction Scrapy, spiders, pipelines, exports.

06_selenium.ipynb
- Selenium headless, usage manuel, integration Scrapy + Selenium.

wikipedia.ipynb
- Projet Wikipedia avec BeautifulSoup.

genius_music_scraping.ipynb
- Projet Genius (scraping de lyrics).

Exercices

Le dossier `Exercices` contient un set d exercices et un corrige par notebook et par projet.
Voir `Exercices/README.md` pour la liste complete.

Installation minimale

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Execution notebooks

Ouvrir et executer les notebooks dans Jupyter ou PyCharm.

Notes reseau

Certains notebooks et demos font des appels reseau (JSONPlaceholder, example.com, Wikipedia, Genius, quotes.toscrape).
Verifier les conditions d utilisation et respecter les delais.


04_api.ipynb

Notebook de formation sur les APIs : auth, REST, retry, rate limiting, erreurs, logging.

Installation minimale

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

Exécution

Ouvrir et exécuter le notebook `04_api.ipynb` dans Jupyter ou PyCharm.

Note

Le section "Exemple avec un vrai client HTTP" fait un appel réseau vers un service public de test (JSONPlaceholder).

05_scrapy.ipynb

Notebook de formation Scrapy : introduction, mécanismes de base, exercices.

Mini projet Scrapy (scrapy_demo)

But : demontrer un vrai projet Scrapy avec items, pipeline, settings et spider.

Execution

cd scrapy_demo
python run_spider.py

Resultat

Un fichier output.jsonl est cree avec les items extraits depuis https://example.com/.

Autres spiders

python run_spider.py jsonplaceholder
python run_spider.py quotes

CSV configurable

Par defaut, le CSV contient les colonnes url et title.
Vous pouvez changer l'ordre ou les colonnes avec CSV_EXPORT_COLUMNS dans scrapy_demo/settings.py.

Utilisation du projet Scrapy

Pre-requis

- Environnement virtuel active
- Dependencies installees via requirements.txt

Lancer un spider

```bash
cd /home/rmdir/PyCharmMiscProject/scrapy_demo
python run_spider.py
python run_spider.py jsonplaceholder
python run_spider.py quotes
```

Sorties generees

- output.jsonl : export JSON Lines
- output.csv : export CSV (colonnes configurables)

Configuration CSV

Dans scrapy_demo/settings.py :
- CSV_EXPORT_PATH : chemin du fichier CSV
- CSV_EXPORT_COLUMNS : ordre et liste des colonnes

Tests

Les tests valident les pipelines (nettoyage et export CSV).

```bash
cd /home/rmdir/PyCharmMiscProject
python -m unittest tests/test_pipelines.py
```

Conseil : si un import echoue, verifiez que le dossier scrapy_demo est present et que l'environnement est bien active.

06_selenium.ipynb

Notebook de formation Selenium : headless, usage manuel, integration Scrapy + Selenium.

Demo Selenium (selenium_demo)

Prerequis

- Un navigateur installe (Chrome ou Firefox)
- Environnement virtuel active
- Dependencies installees via requirements.txt

Execution

```bash
cd /home/rmdir/PyCharmMiscProject/selenium_demo
python run_headless.py
BROWSER=firefox python run_headless.py
```

Sorties

- example_headless.png

Tests Selenium (options only)

```bash
cd /home/rmdir/PyCharmMiscProject
python -m unittest tests/test_selenium_utils.py
```
