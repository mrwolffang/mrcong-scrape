# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ImagespiderPipeline(object):
    def process_item(self, item, spider):
        return item
        
        
# class ImagespiderPipeline(FilesPipeline):
    # def handle_redirect(self, file_url):
        # response = requests.head(file_url)
        # if response.status_code == 302:
            # file_url = response.headers["Location"]
        # return file_url

    # def get_media_requests(self, item, info):
        # redirect_url = self.handle_redirect(item["file_urls"][0])
        # yield scrapy.Request(redirect_url)

    # def item_completed(self, results, item, info):
        # file_paths = [x['path'] for ok, x in results if ok]
        # if not file_paths:
            # raise DropItem("Item contains no images")
        # item['file_urls'] = file_paths
        # return item
