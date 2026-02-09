BOT_NAME = 'scrapy_demo'

SPIDER_MODULES = ['scrapy_demo.spiders']
NEWSPIDER_MODULE = 'scrapy_demo.spiders'

# Comportement respectueux.
ROBOTSTXT_OBEY = True

# Limite douce pour ne pas surcharger un site.
DOWNLOAD_DELAY = 0.5

# Active le pipeline de nettoyage.
ITEM_PIPELINES = {
    'scrapy_demo.pipelines.CleanTitlePipeline': 300,
    'scrapy_demo.pipelines.CsvExportPipeline': 400,
}

# Exporte les items dans un fichier JSONL.
FEEDS = {
    'output.jsonl': {
        'format': 'jsonlines',
        'encoding': 'utf8',
        'indent': 2,
    }
}

# Chemin du fichier CSV exporte par le pipeline.
CSV_EXPORT_PATH = 'output.csv'

# Colonnes exportees dans le CSV.
CSV_EXPORT_COLUMNS = ['url', 'title']
