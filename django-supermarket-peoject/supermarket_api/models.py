from django.db import models


class Product(models.Model):
    product_id = models.SlugField('product_id', unique=True)   
    category = models.ForeignKey(
        to='Category', 
        on_delete=models.SET_NULL, 
        related_name='products', null=True, blank=True
        )
    sub_category = models.ForeignKey(
        to='SubCategory', 
        on_delete=models.SET_NULL, 
        related_name='products', null=True, blank=True
        )
    seller = models.ForeignKey(
        to='Seller', on_delete=models.CASCADE,
        related_name='products'
    )
    brand = models.ForeignKey(
        to='Brand', on_delete=models.SET_NULL,
        related_name='products', null=True, blank=True
    )
    vendor = models.ForeignKey(
        to='Vendor', on_delete=models.CASCADE,
        related_name='products'
    )
    title = models.CharField('title', max_length=500, null=True, blank=True)
    description = models.TextField('description', null=True, blank=True)
    selling_price = models.BigIntegerField('price', null=True, blank=True)
    discounted_price = models.BigIntegerField('discounted price', null=True, blank=True)
    discount_percent = models.IntegerField('discount percent', null=True, blank=True)
    rating_value = models.IntegerField('rate from 100', null=True, blank=True)
    status = models.CharField('status', max_length=30, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['product_id']),
            models.Index(fields=['category']),
        ]

    def __str__(self):
        return f'{self.product_id}/{self.title}/{self.selling_price}'
    
class Category(models.Model):
    cat_id = models.SlugField("category ID", unique=True)   
    code = models.CharField('category code', max_length=70, null=True, blank=True)
    title = models.CharField('title', max_length=500, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['cat_id']),
        ]

    def __str__(self):
        return f'{self.cat_id}/{self.title}'

class SubCategory(models.Model):
    sub_cat_id = models.SlugField("subcategory ID", unique=True)   
    code = models.CharField('subcategory code',max_length=70 ,null=True, blank=True)
    title = models.CharField('title', max_length=500, null=True, blank=True)
    category = models.ForeignKey(
        to='Category', 
        on_delete=models.CASCADE, 
        related_name='subcategories', null=True
        )  
    
    class Meta:
        indexes = [
            models.Index(fields=['sub_cat_id']),
        ]
     
    def __str__(self):
        return f'{self.sub_cat_id}/{self.title}'


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



class Images(models.Model):
    url = models.URLField('url', null=True, blank=True)
    product = models.ForeignKey(
        to='Product', on_delete=models.CASCADE,
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