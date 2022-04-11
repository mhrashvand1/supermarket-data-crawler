from rest_framework import serializers
from supermarket_api.models import (
    Product, Category, Brand, MainImage, OtherImages, Vendor
)


class CategorySerializer(serializers.ModelSerializer):    
    class Meta:
        model = Category
        fields = ['cat_id', 'title']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'brand_code', 'brand_name']


class VendorSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Vendor
        fields = ['name', 'url']
        
        

class MainImageSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.HyperlinkedIdentityField(
        view_name='products-detail',
        lookup_field='product_id',
        read_only = True
        )
    class Meta:
        model = MainImage
        fields = ['id', 'url', 'product']

class MainImageCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainImage
        fields = ['url', 'product']



class OtherImagesSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.HyperlinkedIdentityField(
        view_name='products-detail',
        lookup_field='product_id',
        read_only=True
        )
    class Meta:
        model = OtherImages
        fields = ['id', 'url', 'product']

class OtherImagesCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherImages
        fields = ['url', 'product']




class ProductListSerializer(serializers.ModelSerializer):
    
    main_image = serializers.StringRelatedField() 
    brand = BrandSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    vendor = VendorSerializer(read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'product_id', 'category', 
            'brand', 'vendor', 'main_image',
            'title', 'rating_value', 'price',
            'discounted_price', 'discount_percent', 'status'
        ]

class ProductDetailSerializer(serializers.ModelSerializer):
     
    main_image = serializers.StringRelatedField()
    other_images = serializers.StringRelatedField(many=True)
    brand = BrandSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    vendor = VendorSerializer(read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'product_id', 'category', 
            'brand', 'vendor', 'main_image', 'other_images',
            'title', 'description', 'rating_value', 'price',
            'discounted_price', 'discount_percent', 
            'discount_diffrence', 'status'
        ]
        
class ProductCreateUpdateSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Product
        fields = [
            'product_id', 'category',
            'brand', 'vendor',
            'title', 'description', 'rating_value', 'price',
            'discounted_price', 'discount_percent', 'status'
        ]
        

