import os
import sys
import tempfile
import unittest
from pathlib import Path

from scrapy.settings import Settings

# Add scrapy_demo/ to sys.path so scrapy_demo package can be imported.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRAPY_DEMO_ROOT = PROJECT_ROOT / 'scrapy_demo'
sys.path.insert(0, str(SCRAPY_DEMO_ROOT))

from scrapy_demo.pipelines import CleanTitlePipeline, CsvExportPipeline


class DummySpider:
    def __init__(self, settings):
        self.settings = settings


class PipelineTests(unittest.TestCase):
    def test_clean_title_pipeline_trims(self):
        pipeline = CleanTitlePipeline()
        item = {'title': '  Hello  '}
        result = pipeline.process_item(item, spider=None)
        self.assertEqual(result['title'], 'Hello')

    def test_clean_title_pipeline_rejects_empty(self):
        pipeline = CleanTitlePipeline()
        with self.assertRaises(ValueError):
            pipeline.process_item({'title': '   '}, spider=None)

    def test_csv_export_pipeline_writes(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, 'out.csv')
            settings = Settings({
                'CSV_EXPORT_PATH': path,
                'CSV_EXPORT_COLUMNS': ['title', 'url'],
            })
            spider = DummySpider(settings=settings)
            pipeline = CsvExportPipeline()
            pipeline.open_spider(spider)
            pipeline.process_item({'url': 'u1', 'title': 't1'}, spider)
            pipeline.close_spider(spider)

            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            self.assertIn('title,url', content)
            self.assertIn('t1,u1', content)


if __name__ == '__main__':
    unittest.main()
