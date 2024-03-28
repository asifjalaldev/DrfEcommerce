from .models import Product, Category, Brand
from rest_framework.serializers import ModelSerializer

class ProductSerializer(ModelSerializer):
    model=Product
    fields='__all__'

    
class CategorySerializer(ModelSerializer):
    model=Category
    fields='__all__'

    
class BrandSerializer(ModelSerializer):
    model=Brand
    fields='__all__'

    