

from rest_framework.routers import DefaultRouter
from .views import ProductViewSets, CategoryViewSets, BrandViewSets
from django.urls import path, include

router=DefaultRouter()
router.register('product/', ProductViewSets, basename='product'),
router.register('category/', CategoryViewSets, basename='category'),
router.register('brand/', BrandViewSets, basename='brand'),

urlpatterns = [
path('', include(router.urls)),
]