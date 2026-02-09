Corrige - 06_selenium

1) Headless
```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless=new')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1280,800')
```

2) Selenium a la main
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless=new')

driver = webdriver.Chrome(options=options)
try:
    driver.get('https://example.com/')
    print(driver.title)
    driver.save_screenshot('example.png')
finally:
    driver.quit()
```

3) WebDriverWait
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

wait = WebDriverWait(driver, 5)
h1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1')))
print(h1.text)
```

4) Extraction liste
```python
links = driver.find_elements(By.CSS_SELECTOR, 'a')
print([a.get_attribute('href') for a in links])
```

5) Scrapy + Selenium
```python
import scrapy
from scrapy.http import HtmlResponse

class SeleniumSpider(scrapy.Spider):
    name = 'selenium_spider'
    start_urls = ['https://example.com/']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = webdriver.Chrome(options=options)
    def closed(self, reason):
        self.driver.quit()
    def parse(self, response):
        self.driver.get(response.url)
        html = self.driver.page_source
        rendered = HtmlResponse(url=response.url, body=html, encoding='utf-8')
        title = rendered.css('title::text').get()
        yield {'url': response.url, 'title': (title or '').strip()}
```

