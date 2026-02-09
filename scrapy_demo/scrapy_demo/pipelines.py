class CleanTitlePipeline:
    def process_item(self, item, spider):
        # Nettoie le titre et filtre les vides.
        title = (item.get('title') or '').strip()
        if not title:
            raise ValueError('Titre vide')
        item['title'] = title
        return item


class CsvExportPipeline:
    def __init__(self, file_path=None, columns=None):
        # Allow injection for tests; otherwise use settings.
        self.file_path = file_path
        self.columns = columns
        self._file = None
        self._writer = None

    def open_spider(self, spider):
        # Resolve output path from settings if not provided.
        if not self.file_path:
            self.file_path = spider.settings.get('CSV_EXPORT_PATH', 'output.csv')
        # Resolve column list from settings if not provided.
        if not self.columns:
            self.columns = spider.settings.getlist('CSV_EXPORT_COLUMNS', ['url', 'title'])
        # Open the CSV file once per crawl.
        self._file = open(self.file_path, 'w', encoding='utf-8', newline='')
        # Initialize writer with consistent columns.
        import csv
        self._writer = csv.DictWriter(self._file, fieldnames=self.columns)
        self._writer.writeheader()

    def close_spider(self, spider):
        # Close file handle if it was opened.
        if self._file:
            self._file.close()

    def process_item(self, item, spider):
        # Write the item to the CSV file with configured columns.
        if self._writer:
            row = {key: item.get(key, '') for key in self.columns}
            self._writer.writerow(row)
        return item
