from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    # Charge les settings du projet Scrapy.
    settings = get_project_settings()

    # Cree le process et lance le spider.
    process = CrawlerProcess(settings=settings)
    # Utilise un nom de spider via argument, sinon default.
    import sys
    spider_name = sys.argv[1] if len(sys.argv) > 1 else 'example'
    process.crawl(spider_name)
    process.start()


if __name__ == '__main__':
    main()
