from django.contrib import admin
from supermarket_api.models import (
    Product, Category, Brand, MainImage, OtherImages, Vendor
)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'title', 'price', 'discounted_price', 'status', 'category') 
    list_filter = ('category', 'brand__brand_name', 'vendor') 
    search_fields = ('title', 'description', 'product_id')
admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_id', 'title')  
admin.site.register(Category, CategoryAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_code', 'brand_name') 
admin.site.register(Brand, BrandAdmin)


class MainImageAdmin(admin.ModelAdmin):
    list_display = ('url',)  
admin.site.register(MainImage, MainImageAdmin)


class OtherImagesAdmin(admin.ModelAdmin):
    list_display = ('url', 'product')  
admin.site.register(OtherImages, OtherImagesAdmin)


class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')  
admin.site.register(Vendor, VendorAdmin)