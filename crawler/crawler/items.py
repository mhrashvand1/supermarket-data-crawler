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
    #marketable, unmarketable
    status = scrapy.Field()
    #selling_info
    #fields: price, discounted_price, discount_percent    
    selling_info = scrapy.Field() 
    # category
    #fields: cat_id, title  
    category = scrapy.Field()
    #brand
    #fields: brand_id, brand_name
    brand = scrapy.Field()
    #vendor
    #fields: name, url
    vendor = scrapy.Field()
    #list of product images
    #fields: main_image, other_images
    images = scrapy.Field()
    
  