from django.db import models


class Product(models.Model):
    
    product_id = models.SlugField('product_id', unique=True) 
    #main category  
    category = models.ForeignKey(
        to='Category', to_field='cat_id',
        on_delete=models.SET_NULL, 
        related_name='products', null=True, blank=True
        )
    sub_category = models.ForeignKey(
        to='SubCategory', to_field='sub_cat_id',
        on_delete=models.SET_NULL, 
        related_name='products', null=True, blank=True
        )

    brand = models.ForeignKey(
        to='Brand', to_field='brand_id', on_delete=models.SET_NULL,
        related_name='products', null=True, blank=True
    )
    #vendor: scrapted site. for example Digikala, snapmarket
    vendor = models.ForeignKey(
        to='Vendor', to_field='name', on_delete=models.CASCADE,
        related_name='products'
    )
    seller = models.ManyToManyField(
        to='Seller', through='ProductPriceSeller',
        related_name='products', blank=True
        )
    
    title = models.CharField('title', max_length=500, null=True, blank=True)
    description = models.TextField('description', null=True, blank=True)
    #Average rating given by users 
    rating_value = models.IntegerField('rate from 100', null=True, blank=True)
    #status of product: merketable, out_of_stock, stop_production, ...
    status = models.CharField('status', max_length=30, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['product_id']),
            models.Index(fields=['category']),
        ]

    def __str__(self):
        return f'{self.product_id}/{self.title}/{self.selling_price}'
    
    
    
class Seller(models.Model):
    seller_id = models.SlugField('seller ID', unique=True)
    seller_code = models.CharField('seller code', max_length=15, null=True, blank=True)
    title = models.CharField('title', max_length=500, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['seller_id']),
        ]
     
    def __str__(self):
        return f'{self.seller_id}/{self.title}'   
    
# middle table for manytomany relation between product and seller
#with extra fields contained selling info: selling_price, discounted_price, discount_percent
class ProductPriceSeller(models.Model):
    product = models.ForeignKey(
        to='Product', to_field='product_id', related_name='selling_infos',
        on_delete=models.CASCADE      
    )
    seller = models.ForeignKey(
        to='Seller', to_field='seller_id', related_name='selling_infos',
        on_delete=models.CASCADE
    )
    selling_price = models.BigIntegerField('price', null=True, blank=True)
    discounted_price = models.BigIntegerField('discounted price', null=True, blank=True)
    discount_percent = models.IntegerField('discount percent', null=True, blank=True)   
    class Meta:
        indexes = [
            models.Index(fields=['product', 'seller']),
        ]

    def __str__(self):
        return f'{self.product}/{self.seller}/{self.selling_price}'
    
    
class Category(models.Model):
    cat_id = models.SlugField("category ID", unique=True)   
    cat_code = models.CharField('category code', max_length=70, null=True, blank=True)
    title = models.CharField('title', max_length=500, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['cat_id']),
        ]

    def __str__(self):
        return f'{self.cat_id}/{self.title}'

class SubCategory(models.Model):
    sub_cat_id = models.SlugField("subcategory ID", unique=True)   
    sub_cat_code = models.CharField('subcategory code',max_length=70 ,null=True, blank=True)
    title = models.CharField('title', max_length=500, null=True, blank=True)
    category = models.ForeignKey(
        to='Category', to_field='cat_id',
        on_delete=models.CASCADE, 
        related_name='subcategories', null=True
        )  
    
    class Meta:
        indexes = [
            models.Index(fields=['sub_cat_id']),
        ]
     
    def __str__(self):
        return f'{self.sub_cat_id}/{self.title}'


class Brand(models.Model):
    brand_id = models.SlugField('brand ID', unique=True)
    brand_code = models.CharField('brand code', max_length=15, blank=True, null=True)
    title = models.CharField('title', max_length=500, blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['brand_id']),
        ]

    def __str__(self):
        return f'{self.brand_id}/{self.title}'


# each product maybe has one or more images
class Images(models.Model):
    url = models.URLField('url', null=True, blank=True)
    product = models.ForeignKey(
        to='Product', to_field='product_id', on_delete=models.CASCADE,
        related_name='images', null=True)
   
    def __str__(self):
        return f'image:{self.product}'    
 
    

class Vendor(models.Model):
    name = models.SlugField('vendor name', unique=True)
    url = models.URLField('vendor url')

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return f'{self.name}'