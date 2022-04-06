import scrapy


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
        category = response.meta['category']
        response = response.json()
        yield {
            "implemented":False
        }  