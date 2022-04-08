import scrapy
from crawler.items import CrawlerItem
from urllib.parse import quote
from crawler.spiders.utils import digikala_category_adapter


class DigikalaSpider(scrapy.Spider):
    name = "digikala"
    
    start_urls = [
        #all category inside supermarket exclude natural-flower
        'https://api.digikala.com/v1/categories/beverages/search/',
        'https://api.digikala.com/v1/categories/breakfast/search/',
        'https://api.digikala.com/v1/categories/protein-foods/search/',
        'https://api.digikala.com/v1/categories/dairy/search/',
        'https://api.digikala.com/v1/categories/groceries/search/',
        'https://api.digikala.com/v1/categories/fruits-and-vegetables/search/',
        'https://api.digikala.com/v1/categories/snacks/search/',
        'https://api.digikala.com/v1/categories/dried-fruit-nuts/search/',
        'https://api.digikala.com/v1/categories/ready-made-canned-food/search/',
        'https://api.digikala.com/v1/categories/frozen-food/search/',
        'https://api.digikala.com/v1/categories/home-hygiene/search/'
        'https://api.digikala.com/v1/categories/personal-hygiene/search/',
        'https://api.digikala.com/v1/categories/condiments/search/',
        'https://api.digikala.com/v1/categories/baby-and-mother/search/',
        'https://api.digikala.com/v1/categories/fresh-pastry/search/',
        'https://api.digikala.com/v1/categories/finger_food/search/',
        'https://api.digikala.com/v1/categories/dietary_and_medicinal_supplements/search/'
        ]

    def parse(self, response):
        #request to each page of categories
        url = response.url
        response = response.json()
        #total_pages = response['data']['pager']['total_pages']
        for page_num in range(1, 21):
            yield scrapy.Request(
                url= url + f'?page={page_num}',
                callback=self.product_url_parse
            )
            
    def product_url_parse(self, response):
        #request to products url and send category info from mata
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
        
        item['category'] = digikala_category_adapter(cat_id)
        item['selling_info'] = self.get_selling_info(response)
        item['product_id'] = self.get_product_id(response)
        item['title'] = self.get_title(response)
        item['description'] = self.get_description(response)
        item['status'] = self.get_status(response)
        item['rating_value'] = self.get_rating_value(response)
        item['brand'] = self.get_brand(response)
        item['images'] = self.get_images(response)
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
                "brand_name":brand.get("title_fa"),
                "brand_id":quote(brand.get("title_fa")),
            }
    
    @staticmethod        
    def get_images(res):
        result = list()
        images = res['data']['product'].get('images')       
        main_img = images.get('main')
        result.append(main_img.get('url')[0])
        
        list_img = images.get('list')
        for img in list_img:
            result.append(img.get('url')[0])
        return result
    
    @staticmethod
    def get_status(res):
        status = res['data']['product'].get('status')
        if status == 'marketable':
            return status
        return 'unmarketable'