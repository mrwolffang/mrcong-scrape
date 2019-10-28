BOT_NAME = 'imagespider'
SPIDER_MODULES = ['imagespider.spiders']
NEWSPIDER_MODULE = 'imagespider.spiders'
ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline': 1,
}
IMAGES_STORE = "D:\\abc\\mrcong"
MEDIA_ALLOW_REDIRECTS = True