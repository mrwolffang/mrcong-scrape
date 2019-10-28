from imagespider.items import ImageItem
import scrapy
from imagespider.items import ImageItem

#original
# class ImageSpider(scrapy.Spider):
    # name = "imagespider"

    # start_urls = (
        # "https://mrcong.com/ugirls-u426-65-anh",
    # )

    # def parse(self, response):
        # for elem in response.xpath('//*[@id="fukie2"]/p/img'):
            # img_url = elem.xpath("@src").extract_first()
            # yield {'image_urls': [img_url]}

#1 link ---------------------------------------------------------------------            
# class ImageSpider(scrapy.Spider):
    # name = "imagespider"

    # # start_urls = (
        # # "https://mrcong.com/ugirls-u426-65-anh",
    # # )
    
    # def __init__(self, *args, **kwargs): 
      # super(ImageSpider, self).__init__(*args, **kwargs) 
      # self.start_urls = [kwargs.get('start_url')] 
    
    
    # def parse(self,response):
        ## crawl first page--------------
        # # sel = scrapy.Selector(response)
        # for elem in response.xpath('//*[@id="fukie2"]/p/img'):
            # img_url = elem.xpath("@src").extract_first()
            # yield {'image_urls': [img_url]}
        ##------------------    
        # links = response.xpath('//*[@id="fukie2"]/div[4]/a/@href').extract()
        # for link in links:
            # # item['link'] = link
            # link = ''.join(link)
            # new_request = scrapy.Request(link, callback=self.parse_img)
            # # new_request.meta['item'] = item
            # yield new_request

    # def parse_img(self, response):
        # for elem in response.xpath('//*[@id="fukie2"]/p/img'):
            # img_url = elem.xpath("@src").extract_first()
            # yield {'image_urls': [img_url]}
        # # next_page = response.css('#fukie2 > div:nth-child(6) > a[href]').get()
        # # item = ImageItem()
        
#1 catagory-------------------------------------------------------------------------
class ImageSpider(scrapy.Spider):
    name = "imagespider"

    # start_urls = (
        # "https://mrcong.com/ugirls-u426-65-anh",
    # )
    
    def __init__(self, *args, **kwargs): 
      super(ImageSpider, self).__init__(*args, **kwargs) 
      self.start_urls = [kwargs.get('start_url')] 
    
    def parse(self,response):
        links = response.xpath('//*[@id="main-content"]/div[1]/div[3]/article/h2/a/@href').extract()
        for link in links:
            # item['link'] = link
            link = ''.join(link)
            new_request = scrapy.Request(link, callback=self.parse_link)
            # new_request.meta['item'] = item
            yield new_request 
        # scrapy.Request(self, callback=self.parse_link)    
        sites = response.xpath('//*[@id="main-content"]/div/div/a/@href').extract()
        for site in sites:
            # item['link'] = link
            site = ''.join(site)
            new_request = scrapy.Request(site, callback=self.parse_page)
            # new_request.meta['item'] = item
            yield new_request
    
    def parse_page(self,response):
        links = response.xpath('//*[@id="main-content"]/div[1]/div[3]/article/h2/a/@href').extract()
        for link in links:
            # item['link'] = link
            link = ''.join(link)
            new_request = scrapy.Request(link, callback=self.parse_link)
            # new_request.meta['item'] = item
            yield new_request
        
    
    def parse_link(self,response):
        # sel = scrapy.Selector(response)
        for elem in response.xpath('//*[@id="fukie2"]/p/img'):
            img_url = elem.xpath("@src").extract_first()
            yield {'image_urls': [img_url]}
        links = response.xpath('//*[@id="fukie2"]/div[4]/a/@href').extract()
        for link in links:
            # item['link'] = link
            link = ''.join(link)
            new_request = scrapy.Request(link, callback=self.parse_img)
            # new_request.meta['item'] = item
            yield new_request

    def parse_img(self, response):
        for elem in response.xpath('//*[@id="fukie2"]/p/img'):
            img_url = elem.xpath("@src").extract_first()
            yield {'image_urls': [img_url]}
        # next_page = response.css('#fukie2 > div:nth-child(6) > a[href]').get()
        # item = ImageItem()     