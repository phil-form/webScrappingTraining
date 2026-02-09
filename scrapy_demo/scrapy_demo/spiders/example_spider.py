import scrapy
from scrapy_demo.items import ExampleItem


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['https://example.com/']

    def parse(self, response):
        # Extrait le titre de la page d'exemple.
        title = response.css('title::text').get()
        # Construit l'item en normalisant le titre.
        item = ExampleItem(url=response.url, title=(title or '').strip())
        yield item

