# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):

    product_id = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    rating_value = scrapy.Field()
    status = scrapy.Field() 
    #selling_info:
    #list of sellers with fields below:
    #seller_id, seller_code, title, selling_price, discounted_price, discount_percent    
    selling_info = scrapy.Field() 
    # main category
    #fields: cat_id, cat_code, title  
    category = scrapy.Field()
    #subcategory
    #fields: sub_cat_id, sub_cat_code, title
    sub_category = scrapy.Field()
    #brand
    #fields: brand_id, brand_code, title
    brand = scrapy.Field()
    #vendor
    #fields: name, url
    vendor = scrapy.Field()
    #list of product images
    images = scrapy.Field()
    
  