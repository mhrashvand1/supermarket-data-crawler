from django_filters import rest_framework as filters
from supermarket_api.models import Product



class ProductFilter(filters.FilterSet):
    #string fields
    title = filters.Filter(field_name="title", lookup_expr='icontains')
    description = filters.Filter(field_name="description", lookup_expr='icontains')
    #numeric fields
    rating_value__lt = filters.NumberFilter(field_name="rating_value", lookup_expr='lt')
    rating_value__gt = filters.NumberFilter(field_name="rating_value", lookup_expr='gt')
    price__lt = filters.NumberFilter(field_name="price", lookup_expr='lt')
    price__gt = filters.NumberFilter(field_name="price", lookup_expr='gt')
    discounted_price__lt = filters.NumberFilter(field_name="discounted_price", lookup_expr='lt')
    discounted_price__gt = filters.NumberFilter(field_name="discounted_price", lookup_expr='gt')
    discount_percent__lt = filters.NumberFilter(field_name="discount_percent", lookup_expr='lt')
    discount_percent__gt = filters.NumberFilter(field_name="discount_percent", lookup_expr='gt')  
    rating_value__lt = filters.NumberFilter(field_name="rating_value", lookup_expr='lt')
    rating_value__gt = filters.NumberFilter(field_name="rating_value", lookup_expr='gt')
    #relation fields
    category_id = filters.Filter(field_name="category", lookup_expr='cat_id__icontains')
    category_title = filters.Filter(field_name="category", lookup_expr='title__icontains')
    brand_name = filters.Filter(field_name="brand", lookup_expr='brand_name__icontains')
    vendor_name = filters.Filter(field_name="vendor", lookup_expr='name__icontains')
    
    class Meta:
        model = Product
        fields = [
            'product_id',       
            'rating_value',
            'price',
            'discounted_price', 
            'discount_percent',
            'status', 
            ]