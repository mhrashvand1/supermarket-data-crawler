from rest_framework.routers import DefaultRouter
from supermarket_api.views import (
    ProductViewSet, CategoryViewSet, BrandViewSet,
    MainImageViewSet, OtherImagesViewSet, VendorViewSet
)


router = DefaultRouter()
router.register(r'supermarket/products', ProductViewSet, basename='products')
router.register(r'supermarket/categories', CategoryViewSet, basename='categories')
router.register(r'supermarket/brands', BrandViewSet, basename='brands')
router.register(r'supermarket/mainimages', MainImageViewSet, basename='mainimages')
router.register(r'supermarket/otherimages', OtherImagesViewSet, basename='otherimages')
router.register(r'supermarket/vendors', VendorViewSet, basename='vendors')


