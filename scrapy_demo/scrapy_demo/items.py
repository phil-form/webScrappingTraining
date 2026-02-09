import scrapy


class ExampleItem(scrapy.Item):
    # URL de la page scrapée.
    url = scrapy.Field()
    # Titre ou texte extrait.
    title = scrapy.Field()

