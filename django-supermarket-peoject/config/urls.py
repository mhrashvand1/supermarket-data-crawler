from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from supermarket_api.routers import router as r1
from account_api.routers import router as r2

router = DefaultRouter()
router.registry.extend(r1.registry)
router.registry.extend(r2.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += router.urls
