from rest_framework import serializers
from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields we want to show in th `API`
        fields = ("id","name","get_absolute_url","description","price","get_image","get_thumbnail")

class CategorySerializer(serializers.ModelSerializer):
    # model = Product ee... `related_name='products'` liksi... eijonno amra 1 ta Category dhoira oi Category er Under ee shb Product niye ashte parbo
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        # fields we want to show in th `API`
        fields = ("id","name","get_absolute_url","products")

class AllCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields we want to show in th `API`
        fields = ("id","name","slug")