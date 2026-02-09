Corrige - scrapy_demo

1) Nouveau spider
```python
class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/']
    def parse(self, response):
        for q in response.css('div.quote'):
            text = q.css('span.text::text').get()
            author = q.css('small.author::text').get()
            yield {'title': (text or '').strip(), 'author': (author or '').strip(), 'url': response.url}
```

2) Export CSV
```python
# settings.py
CSV_EXPORT_COLUMNS = ['url', 'title', 'author']
```

3) Pipeline
```python
class CleanTitlePipeline:
    def process_item(self, item, spider):
        title = (item.get('title') or '').strip()
        if not title:
            raise ValueError('Titre vide')
        item['title'] = title
        return item
```

4) Settings
```python
ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 1.0
```

5) Tests
```python
from scrapy_demo.pipelines import CleanTitlePipeline

def test_clean():
    p = CleanTitlePipeline()
    assert p.process_item({'title': '  A  '}, None)['title'] == 'A'
```

