from rest_framework import viewsets
from supermarket_api.permissions import IsSuperuserOrStaffOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from supermarket_api.filters import ProductFilter
from supermarket_api.pagination import StandardPagination
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
    pagination_class = StandardPagination
   
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'description', 'product_id',]
    ordering_fields = [
        '-rating_value', '-discount_percent',
        'price', 'discounted_price', 'status'
        ]

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
    pagination_class = StandardPagination
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter,]
    search_fields = ['cat_id', 'title']

    
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    #permission_classes = [IsSuperuserOrStaffOrReadOnly,]
    pagination_class = StandardPagination
    serializer_class = BrandSerializer
    filter_backends = [SearchFilter,]
    search_fields = ['brand_name',]

    
    
class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    lookup_field = 'name'
    #permission_classes = [IsSuperuserOrStaffOrReadOnly,]
    pagination_class = StandardPagination
    serializer_class = VendorSerializer
    filter_backends = [SearchFilter,]
    search_fields = ['name',]

    
    
class MainImageViewSet(viewsets.ModelViewSet):
    queryset = MainImage.objects.all()
    #permission_classes = [IsSuperuserOrStaffOrReadOnly,]
    pagination_class = StandardPagination
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_updates']:
            return MainImageCreateUpdateSerializer
        return MainImageSerializer

    
class OtherImagesViewSet(viewsets.ModelViewSet):
    queryset = OtherImages.objects.all()
    #permission_classes = [IsSuperuserOrStaffOrReadOnly,]  
    pagination_class = StandardPagination  
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_updates']:
            return OtherImagesCreateUpdateSerializer
        return OtherImagesSerializer
  
    
