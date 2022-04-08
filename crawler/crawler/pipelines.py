from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class CrawlerPipeline:   
      
    def process_item(self, item, spider):
        if item['status'] == 'unmarketable':
            raise DropItem("fuckkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")

        return item

