from .models import Product, Category, Brand
from rest_framework.serializers import ModelSerializer

class ProductSerializer(ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

    
class CategorySerializer(ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

    
class BrandSerializer(ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'

    