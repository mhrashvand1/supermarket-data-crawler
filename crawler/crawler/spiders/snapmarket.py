# all product in snapmarket is marketable

import scrapy
from crawler.items import CrawlerItem

class SnapMarketSpider(scrapy.Spider):
    name = "snapmaeket"
    
    start_urls = [
        'https://core.snapp.market/api/v1/vendors/0r5ryz/categories/278344?limit=12&offset=0'
    ]

    def parse(self, response):
        response = response.json()
        yield {
            "status": response['breadcrumb']
        }
 