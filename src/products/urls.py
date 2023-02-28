from django.urls import path

from .views import index
from .views import product_detail, product_search


urlpatterns = [
    path('', index, name='index'),
    path('products/', index, name='products'),
    path('products/product/search/', product_search, name='product_search'),
    path('product/product/<int:pk>', product_detail, name='product_detail'),
]
