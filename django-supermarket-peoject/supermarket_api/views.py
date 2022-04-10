from rest_framework import viewsets
from supermarket_api.models import (
    Product, Category, Brand, MainImage, OtherImages, Vendor
)
from supermarket_api.serializers import ProductDetailSerializer, ProductListSerializer

class ProductViewSet(viewsets.ModelViewSet):
 
    queryset = Product.objects.all()
    lookup_field = 'product_id'
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return ProductDetailSerializer
    
