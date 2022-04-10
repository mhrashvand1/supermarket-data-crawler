from rest_framework.routers import DefaultRouter
from supermarket_api.views import ProductViewSet

router = DefaultRouter()
router.register(r'supermarket/products', ProductViewSet, basename='products')


