from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category, Product, Brand
from .serializers import CategorySerializer, ProductSerializer, BrandSerializer
from rest_framework.response import Response
# Create your views here.

class CategoryViewSets(ModelViewSet):

    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    def list(self, request, *args, **kwargs):
        queryset=Category.objects.all()
        serialized=CategorySerializer(queryset, many=True)
        return Response(serialized.data)
    

class ProductViewSets(ModelViewSet):

    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    def list(self, request, *args, **kwargs):
        queryset=Product.objects.all()
        serialized=ProductSerializer(queryset, many=True)
        return Response(serialized.data)
    

class BrandViewSets(ModelViewSet):

    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    def list(self, request, *args, **kwargs):
        queryset=Brand.objects.all()
        serialized=BrandSerializer(queryset, many=True)
        return Response(serialized.data)
