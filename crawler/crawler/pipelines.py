from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class CrawlerPipeline:   
      
    def process_item(self, item, spider):
        return item

