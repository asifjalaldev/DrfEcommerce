from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from .models import Category, Product, Brand
from .serializers import CategorySerializer, ProductSerializer, BrandSerializer
from rest_framework.response import Response
# Create your views here.

class CategoryViewSets(ViewSet):

    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """


    def list(self, request):
        queryset=Category.objects.all()
        serializer=CategorySerializer(queryset, many=True)
        return Response(serializer.data)
    

class ProductViewSets(ViewSet):

    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    def list(self, request, *args, **kwargs):
        queryset=Product.objects.all()
        serialized=ProductSerializer(queryset, many=True)
        return Response(serialized.data)
    

class BrandViewSets(ViewSet):

    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    def list(self, request, *args, **kwargs):
        queryset=Brand.objects.all()
        serialized=BrandSerializer(queryset, many=True)
        return Response(serialized.data)
