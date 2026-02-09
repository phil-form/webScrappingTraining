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
