import scrapy
from scrapy_demo.items import ExampleItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        # Extract each quote block.
        for quote in response.css('div.quote'):
            text = quote.css('span.text::text').get()
            item = ExampleItem(
                url=response.url,
                title=(text or '').strip(),
            )
            yield item

        # Follow pagination if a next page exists.
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

