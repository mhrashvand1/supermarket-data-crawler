from rest_framework import serializers
from supermarket_api.models import (
    Product, Category, Brand, MainImage, OtherImages, Vendor
)


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'product_id', 'category', 
            'brand', 'vendor', 'main_image',
            'title', 'rating_value', 'price',
            'discounted_price', 'discount_percent', 'status'
        ]


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'product_id', 'category', 
            'brand', 'vendor', 'main_image', 'other_images',
            'title', 'description', 'rating_value', 'price',
            'discounted_price', 'discount_percent', 
            'discount_diffrence', 'status'
        ]