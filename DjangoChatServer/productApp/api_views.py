from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from django.db.models import Q

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer, AllCategorySerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:6]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class SingleProductDetail(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class SingleCategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class AllCategories(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = AllCategorySerializer(categories, many=True)
        return Response(serializer.data)


class SearchProductsView(APIView):
    def post(self, request):
        query = request.data.get('query','')
        if query:
            products = Product.objects.filter(Q(name__icontains=query) | Q(slug__icontains=query))
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        else:
            return Response({"products":[]})