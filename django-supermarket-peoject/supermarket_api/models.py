from django.db import models


class Product(models.Model):  

    product_id = models.SlugField('product_id', unique=True) 
    category = models.ForeignKey(
        to='Category', to_field='cat_id',
        on_delete=models.SET_NULL, 
        related_name='products', null=True, blank=True
        )    
    brand = models.ForeignKey(
        to='Brand', to_field='brand_code', on_delete=models.SET_NULL,
        related_name='products', null=True, blank=True
    )
    #vendor: scrapted site. for example Digikala, snapmarket
    vendor = models.ForeignKey(
        to='Vendor', to_field='name', on_delete=models.CASCADE,
        related_name='products'
    )  
    
    title = models.TextField('title', max_length=500, null=True, blank=True)
    description = models.TextField('description', null=True, blank=True)
    #Average rating given by users
    rating_value = models.IntegerField('rate from 100', null=True, blank=True)
    price = models.BigIntegerField('price', null=True, blank=True)
    discounted_price = models.BigIntegerField('discounted price', null=True, blank=True)
    discount_percent = models.IntegerField('discount percent', null=True, blank=True)
    status = models.CharField('status', max_length=50, null=True, blank=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['product_id']),
        ]

    def discount_diffrence(self):
        #In some vondors there is not any selling info if status is not marketable
        if self.status == 'marketable':
            return self.price - self.discounted_price

    def __str__(self):
        return f'{self.product_id}/{self.title}'
    

    
class Category(models.Model):
    cat_id = models.SlugField("category ID", unique=True)   
    title = models.CharField('title', max_length=1000, unique=True)

    class Meta:
        indexes = [
            models.Index(fields=['cat_id']),
        ]

    def __str__(self):
        return f'{self.cat_id}'



class Brand(models.Model):
    brand_code = models.TextField('brand code', unique=True)
    brand_name = models.CharField('brand name', max_length=1000, unique=True)

    class Meta:
        indexes = [
            models.Index(fields=['brand_name']),
        ]

    def __str__(self):
        return f'{self.brand_name}'

class MainImage(models.Model):
    url = models.URLField('url')
    product = models.OneToOneField(
        to='Product', to_field='product_id', on_delete=models.CASCADE,
        related_name='main_image'
    )   
    def __str__(self):
        return f'{self.url}'
 
class OtherImages(models.Model):
    url = models.URLField('url')
    product = models.ForeignKey(
        to='Product', to_field='product_id', on_delete=models.CASCADE,
        related_name='other_images'
    )
    def __str__(self):
        return f'{self.url}'
    
class Vendor(models.Model):
    name = models.SlugField('vendor name', unique=True)
    url = models.URLField('vendor url')
    
    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return f'{self.url}' 