from django.urls import path
from .views import(
    BrandView,
    CategoryView
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('category', CategoryView)
router.register('brand', BrandView)

urlpatterns = [
] + router.urls
