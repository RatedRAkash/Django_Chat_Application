from django.contrib.auth import views as auth_views
from django.urls import path

from productApp.api_views import *

urlpatterns = [
    path('latest-products', LatestProductsList.as_view(), name='latest-products'),
    path('products/search', SearchProductsView.as_view(), name='search-products'),
    path('products/<slug:category_slug>/<slug:product_slug>', SingleProductDetail.as_view(), name='single-product-detail'),
    path('products/<slug:category_slug>', SingleCategoryDetail.as_view(), name='single-category-detail'),
]