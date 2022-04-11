from itemadapter import ItemAdapter
import requests



class CrawlerPipeline:   
    
      
    def process_item(self, item, spider):
        #item = ItemAdapter(item).asdict()
        #create brand
        requests.post(
            url='http://127.0.0.1:8000/supermarket/brands/',
            data= item.get('brand')
        )
        #create category
        requests.post(
            url='http://127.0.0.1:8000/supermarket/categories/',
            data=item.get('category')
        )
        #create vendor
        requests.post(
            url='http://127.0.0.1:8000/supermarket/vendors/',
            data=item.get('vendor')
        )
        #create product
        requests.post(
            url='http://127.0.0.1:8000/supermarket/products/',
            data={
                "product_id":item.get('product_id'),
                "title":item.get('title'),
                "description":item.get('description'),
                "status":item.get('status'),
                "price":item.get("selling_info").get('price'),
                "discounted_price":item.get("selling_info").get('discounted_price'),
                "discount_percent":item.get("selling_info").get('discount_percent'),
                "rating_value":item.get("rating_value"),
                "brand":item.get("brand").get("brand_code"),
                "category":item.get("category").get("cat_id"),
                "vendor":item.get("vendor").get("name")        
            }
        )
        #create main image
        requests.post(
            url="http://127.0.0.1:8000/supermarket/mainimages/",
            data={
                "url":item.get("images").get("main_image"),
                "product":item.get("product_id")
            }
        )
        #create other images
        for img_url in item.get("images").get("other_images"):
            requests.post(
                url="http://127.0.0.1:8000/supermarket/otherimages/",
                data={
                    "url":img_url,
                    "product":item.get("product_id")
                }
            )         
               
        return item

