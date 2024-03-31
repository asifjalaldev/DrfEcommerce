from .models import Product, Category, Brand, ProductLine
from rest_framework.serializers import ModelSerializer

class ProductSerializer(ModelSerializer):
    model = Product
    fields = '__all__'


class ProductLineSerializer(ModelSerializer):
    model = ProductLine
    fields = '__all__'



class CategorySerializer(ModelSerializer):
    model = Category
    fields = '__all__'

    
class BrandSerializer(ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'
    model = Brand
    fields = '__all__'


    