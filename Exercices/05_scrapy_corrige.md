Corrige - 05_scrapy

1) Spider local
```python
class ArticleItem(dict):
    pass

class DemoSpider(Spider):
    name = 'demo'
    def parse(self, response):
        for title in response.css('h2.article-title::text').getall():
            item = ArticleItem(
                title=title.strip(),
                url=response.url,
                resume=(response.css('p::text').get() or '').strip(),
            )
            yield item
```

2) Request/Response
```python
from scrapy.http import TextResponse
html = '<a href="/a1">A1</a><a href="/a2">A2</a>'
resp = TextResponse(url='https://example.local', body=html, encoding='utf-8')
print(resp.css('a::attr(href)').getall())
```

3) Pipeline
```python
class CleanTitlePipeline:
    def process_item(self, item, spider):
        title = (item.get('title') or '').strip().lower()
        if len(title) < 3:
            raise ValueError('titre court')
        item['title'] = title
        return item
```

4) CrawlerProcess
```python
from scrapy.crawler import CrawlerProcess

class ExampleComSpider(Spider):
    name = 'example_com'
    start_urls = ['https://example.com/']
    def parse(self, response):
        title = response.css('title::text').get()
        yield {'title': (title or '').strip(), 'url': response.url}

process = CrawlerProcess({'LOG_LEVEL': 'ERROR'})
process.crawl(ExampleComSpider)
process.start()
```

5) ItemLoader
```python
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose

class LinkItem(scrapy.Item):
    url = scrapy.Field()
    label = scrapy.Field()

class LinkItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    label_in = MapCompose(str.strip)
```

6) Export JSON
```python
import json
items = [{'title': 'A'}, {'title': 'B'}]
with open('items.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)
```

