import scrapy

class ImageItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()