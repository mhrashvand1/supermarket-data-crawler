import scrapy
from crawler.items import CrawlerItem
from urllib.parse import quote
from crawler.spiders.utils import DIGIKALA_CATEGORY_ADAPTER


class DigikalaSpider(scrapy.Spider):
    name = "digikala"
    
    start_urls = [
        'https://api.digikala.com/v1/categories/food-beverage/',
    ]

    def parse(self, response):
        #get categories inside supermarket and request to their urls
        response = response.json()
        for category in response['data']['sub_categories']:
            code = category['code']
            yield scrapy.Request(
                url=f"https://api.digikala.com/v1/categories/{code}/search/",
                callback=self.page_parse
            )
        
            
    def page_parse(self, response):
        #get pagination info and request to each page
        url = response.url
        response = response.json()
        total_pages = response['data']['pager']['total_pages']
        for page_num in range(1, total_pages):
            yield scrapy.Request(
                url= url + f'?page={page_num}',
                callback=self.product_url_parse
            )
           
    def product_url_parse(self, response):
        #get product_ids and request products url and send category info from meta
        response = response.json()
        for product in response['data']['products']:
            yield scrapy.Request(
                f'https://api.digikala.com/v1/product/{product["id"]}/',
                callback=self.product_parse,
                meta = {
                    "category_id":response['data']['category']['id']                 
                }         
            )
            
    def product_parse(self, response):
        #parse and return product info
        item = CrawlerItem()
        cat_id = response.meta['category_id']     
        response = response.json()
        
        item['product_id'] = self.get_product_id(response)
        item['title'] = self.get_title(response)
        item['description'] = self.get_description(response)
        item['status'] = self.get_status(response)
        item['selling_info'] = self.get_selling_info(response)
        item['images'] = self.get_images(response)  
        item['rating_value'] = self.get_rating_value(response)      
        item['category'] = DIGIKALA_CATEGORY_ADAPTER.get(cat_id)    
        item['brand'] = self.get_brand(response)      
        item['vendor'] = {"name":"digikala", "url":"https://www.digikala.com/"}
        
        yield item
      
        
    @staticmethod     
    def get_selling_info(res):
        result = dict()
        variant = res['data']['product'].get('default_variant')
        if variant and isinstance(variant, dict):
            result["price"] = variant["price"].get("rrp_price")/10,
            result["discounted_price"] = variant["price"].get("selling_price")/10
            result["discount_percent"] = variant["price"].get("discount_percent")         
        return result
    

    @staticmethod        
    def get_product_id(res):
        id = res['data']['product'].get("id")
        if id:
            return str(id)+"-D"
    
    @staticmethod
    def get_title(res):
        return  res['data']['product'].get("title_fa")
     
    @staticmethod                     
    def get_description(res):
        review = res['data']['product'].get('review')
        if review and isinstance(review, dict):
            return review.get('description')
    
    @staticmethod    
    def get_rating_value(res):
        rating = res['data']['product'].get('rating')
        if rating and isinstance(rating, dict):
            return rating.get("rate")
     
    @staticmethod
    def get_brand(res):
        brand = res['data']['product'].get('brand')
        if brand and isinstance(brand, dict):
            return {
                "brand_code":quote(brand.get("title_fa")),
                "brand_name":brand.get("title_fa"),
            }
    
    @staticmethod        
    def get_images(res):
        result = dict()
        images = res['data']['product'].get('images')       
        main_img = images.get('main')
        list_img = images.get('list')
        
        result['main_image'] = main_img.get('url')[0]
        result['other_images'] = [img.get('url')[0] for img in list_img]
        return result
    
    @staticmethod
    def get_status(res):
        status = res['data']['product'].get('status')
        if status == 'marketable':
            return status
        return 'unmarketable'