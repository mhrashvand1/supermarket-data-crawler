import scrapy
from crawler.items import CrawlerItem

class DigikalaSpider(scrapy.Spider):
    name = "digikala"
    
    start_urls = [
        #url of supermarket products
        'https://api.digikala.com/v1/categories/food-beverage/'
    ]

    def parse(self, response):
        # request to each category inside supermarket
        response = response.json()
        for category in response['data']['sub_categories']:
            yield scrapy.Request(
                f'https://api.digikala.com/v1/categories/{category["code"]}/search/',
                callback=self.page_parse
                )
            
    def page_parse(self, response):
        #request to each page of categories
        url = response.url
        response = response.json()
        total_pages = response['data']['pager']['total_pages']
        for page_num in range(1, total_pages+1):
            yield scrapy.Request(
                url= url + f'?page={page_num}',
                callback=self.product_url_parse
            )

    def product_url_parse(self, response):
        #request to products url and send category info from mata
        response = response.json()
        for product in response['data']['products']:
            product_id = product['id']
            yield scrapy.Request(
                f'https://api.digikala.com/v1/product/{product_id}/',
                callback=self.product_parse,
                meta = {
                    "category":{
                        "cat_id":str(response['data']['category']['id'])+'-D',
                        "cat_code":str(response['data']['category']['code'])+'-D',
                        'title':response['data']['category']['title_fa']
                    }
                }         
            )
            
    def product_parse(self, response):
        #parse and return product info
        item = CrawlerItem()
        category = response.meta['category']        
        response = response.json()
        
        item['category'] = category
        item['sub_category'] = self.get_sub_category(response)
        item['selling_info'] = self.get_selling_info(response)
        item['product_id'] = self.get_product_id(response)
        item['title'] = self.get_title(response)
        item['description'] = self.get_description(response)
        item['status'] = response['data']['product'].get('status')
        item['rating_value'] = self.get_rating_value(response)
        item['brand'] = self.get_brand(response)
        item['images'] = self.get_images(response)
        item['vendor'] = {"name":"digikala", "url":"https://www.digikala.com/"}
        
        yield item
        
    @staticmethod     
    def get_selling_info(res):
        #if product is marketable: return list of sellers with their price
        #else: return empty list
        result=list()
        #variants is list of sellers and their price
        variants = res['data']['product'].get('variants')
        if variants and isinstance(variants, list):
            for v in variants:
                result.append(
                    {
                        "seller_id":str(v["seller"]["id"])+"-D",
                        "seller_code":str(v["seller"]["code"])+"-D",
                        "title":v["seller"]["title"],
                        "price":v["price"]["rrp_price"]/10,
                        "discounted_price":v["price"]["selling_price"]/10,
                        "discount_percent":v["price"]["discount_percent"],
                    }
                )
        return result
    
    @staticmethod
    def get_sub_category(res):
        sub_category = res['data']['product'].get('category')
        if sub_category and isinstance(sub_category, dict):
            return {
                "sub_cat_id":str(sub_category.get("id"))+"-D",
                "sub_cat_code":str(sub_category.get("code"))+"-D",
                "title":sub_category.get("title_fa")
            }
     
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
        if rating:
            return rating.get("rate")
     
    @staticmethod
    def get_brand(res):
        brand = res['data']['product'].get('brand')
        if brand and isinstance(brand, dict):
            return {
                "brand_id":str(brand.get("id")) + "-D",
                "brand_code":str(brand.get("code")) + "-D",
                "title":brand.get("title_fa")
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