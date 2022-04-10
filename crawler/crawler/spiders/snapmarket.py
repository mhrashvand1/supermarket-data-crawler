import scrapy
from crawler.items import CrawlerItem
from urllib.parse import quote
from crawler.spiders.utils import SNAPMARKET_CATEGORY_ADAPTER


class SnapMarketSpider(scrapy.Spider):
    name = "snapmarket"
    
    # urls of categories
    start_urls = [
        f'https://core.snapp.market/api/v1/vendors/0r5ryz/categories/2783{i}' for i in range(43, 57)
        ]
    start_urls += [
        'https://core.snapp.market/api/v1/vendors/0r5ryz/categories/278858'
        ]

    def parse(self, response):
        #get items inside each cagetory and request to their urls
        response = response.json()
        for item in response['items']:
            item_id = item.get('id')
            yield scrapy.Request(
                f'https://core.snapp.market/api/v2/vendors/0r5ryz/products?limit=24&offset=0&categories[]={item_id}',
                callback=self.page_parse,
                meta = {"item_id":item_id}     
            )
            
    def page_parse(self, response):
        # request to all pages
        item_id = response.meta["item_id"]
        response = response.json()
        total_products = response['metadata']['pagination']['total']
        limit = response['metadata']['pagination']['limit']
        page_numbers = total_products//limit+1
        offset = 0
        for _ in range(1, page_numbers+1):
            yield scrapy.Request(
                f'https://core.snapp.market/api/v2/vendors/0r5ryz/products?limit=24&offset={offset}&categories[]={item_id}',
                callback=self.product_url_parse    
            )
            offset += 24
            
    def product_url_parse(self, response):
        #get and request to products url
        response = response.json()
        for product in response['results']:
            product_id = product.get('id')
            yield scrapy.Request(
                f'https://core.snapp.market/api/v1/vendors/0r5ryz/products/{product_id}?platform=WEB',
                callback=self.product_parse
            )
            
    def product_parse(self, response):
        #parse and return product info
        item = CrawlerItem()
        response = response.json()
        cat_id = self.get_category_id(response)
        
        item['product_id'] = self.get_product_id(response)
        item['title'] = self.get_title(response)
        item['description'] = self.get_description(response)
        item['status'] = self.get_status(response)
        item['selling_info'] = self.get_selling_info(response)
        item['images'] = self.get_images(response)
        item['rating_value'] = self.get_rating_value(response)
        item['category'] = SNAPMARKET_CATEGORY_ADAPTER.get(cat_id)  
        item['brand'] = self.get_brand(response)       
        item['vendor'] = {"name":"snappmarket", "url":"https://snapp.market/"}
        
        yield item
     
     
    @staticmethod    
    def get_category_id(res):
        breadcrumb = res.get('breadcrumb')
        if breadcrumb and isinstance(breadcrumb, list):
            return breadcrumb[0].get('id')
    
        
    @staticmethod     
    def get_selling_info(res):
        result = dict()
        product = res['product'] 
        result['price'] = product.get('price')
        result['discounted_price'] = product.get('discounted_price')
        result['discount_percent'] = product.get('discount_percent')
        return result
    

    @staticmethod        
    def get_product_id(res):
        id = res['product'].get("id")
        if id:
            return str(id)+"-S"
    
    @staticmethod
    def get_title(res):
        return  res['product'].get("title")
     
    @staticmethod                     
    def get_description(res):
        return res['product'].get('description')
   
    @staticmethod    
    def get_rating_value(res):
        return res['product'].get('rating_value')*20
       
     
    @staticmethod
    def get_brand(res):
        brand = res['product'].get('brand')
        if brand and isinstance(brand, dict):
            if brand.get('slug') == 'no-branded':
                return {'brand_name':'متفرقه', 'brand_id':quote('متفرقه')}
            return {
                "brand_name":brand.get("title"),
                "brand_id":quote(brand.get("title")),
            }
    
    @staticmethod        
    def get_images(res):
        result = dict()
        images = res['product'].get('images')   
        if images:    
            result['main_image'] = images[0].get('image')
            result['other_images'] = [img.get('image') for img in images[1:]]  
        return result
    
    @staticmethod
    def get_status(res):
        max_order_cap = res['product'].get('max_order_cap')
        if max_order_cap == 0:
            return 'unmarketable'
        return 'marketable'