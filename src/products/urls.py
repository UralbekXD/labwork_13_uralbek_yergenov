from django.urls import path

from .views import index
from .views import product_detail, product_search, product_create, product_edit


urlpatterns = [
    path('', index, name='index'),
    path('products/', index, name='products'),
    path('products/product/search/', product_search, name='product_search'),
    path('products/product/<int:pk>', product_detail, name='product_detail'),
    path('products/product/add', product_create, name='product_create'),
    path('products/product/edit/<int:pk>', product_edit, name='product_edit')
]
