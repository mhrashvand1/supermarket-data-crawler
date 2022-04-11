from rest_framework import viewsets
from supermarket_api.permissions import IsSuperuserOrStaffOrReadOnly
from supermarket_api.models import (
    Product, Category, Brand, MainImage, OtherImages, Vendor
)
from supermarket_api.serializers import (
    ProductDetailSerializer, ProductListSerializer,
    ProductCreateUpdateSerializer, CategorySerializer,BrandSerializer,
    MainImageSerializer, MainImageCreateUpdateSerializer,
    OtherImagesSerializer, OtherImagesCreateUpdateSerializer,
    VendorSerializer
)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    lookup_field = 'product_id'
    #permission_classes = [IsSuperuserOrStaffOrReadOnly,]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        if self.action in ['create', 'update', 'partial_updates']:
            return ProductCreateUpdateSerializer
        return ProductDetailSerializer
  
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    lookup_field = 'cat_id'
    #permission_classes = [IsSuperuserOrStaffOrReadOnly,]
    serializer_class = CategorySerializer
    
    
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    #permission_classes = [IsSuperuserOrStaffOrReadOnly,]
    serializer_class = BrandSerializer
    
    
class MainImageViewSet(viewsets.ModelViewSet):
    queryset = MainImage.objects.all()
    #permission_classes = [IsSuperuserOrStaffOrReadOnly,]
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_updates']:
            return MainImageCreateUpdateSerializer
        return MainImageSerializer
  
    
class OtherImagesViewSet(viewsets.ModelViewSet):
    queryset = OtherImages.objects.all()
    #permission_classes = [IsSuperuserOrStaffOrReadOnly,]    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_updates']:
            return OtherImagesCreateUpdateSerializer
        return OtherImagesSerializer
  
    
class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    lookup_field = 'name'
    #permission_classes = [IsSuperuserOrStaffOrReadOnly,]
    serializer_class = VendorSerializer