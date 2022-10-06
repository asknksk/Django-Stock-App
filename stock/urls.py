from django.urls import path
from .views import(
    BrandView,
    CategoryView,
    FirmView,
    ProductView
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('category', CategoryView)
router.register('brand', BrandView)
router.register('product', ProductView)
router.register('firm', FirmView)

urlpatterns = [
] + router.urls
