from rest_framework import serializers
from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields we want to show in th `API`
        fields = ("id","name","get_absolute_url","description","price","get_image","get_thumbnail")

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        # fields we want to show in th `API`
        fields = ("id","name","get_absolute_url","products")