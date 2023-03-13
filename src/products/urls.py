from django.urls import path

from .views import *


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('products/', Index.as_view(), name='products'),
    path('products/categories/', CategoryList.as_view(), name='category'),
    path('products/product/search/', ProductSearch.as_view(), name='product_search'),
    path('products/product/<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('products/product/add', ProductCreate.as_view(), name='product_create'),
    path('products/product/edit/<int:pk>', ProductEdit.as_view(), name='product_edit'),
    path('products/product/delete/<int:pk>', ProductDelete.as_view(), name='product_delete'),
]
