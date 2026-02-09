import scrapy
from scrapy_demo.items import ExampleItem


class JsonPlaceholderSpider(scrapy.Spider):
    name = 'jsonplaceholder'
    allowed_domains = ['jsonplaceholder.typicode.com']
    start_urls = ['https://jsonplaceholder.typicode.com/posts']

    def parse(self, response):
        # Parse the JSON array of posts.
        data = response.json()
        # Yield a limited subset for demo purposes.
        for post in data[:5]:
            item = ExampleItem(
                url=f"https://jsonplaceholder.typicode.com/posts/{post.get('id')}",
                title=(post.get('title') or '').strip(),
            )
            yield item

