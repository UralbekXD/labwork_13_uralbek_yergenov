from django.urls import path

from .views import index
from .views import product_detail


urlpatterns = [
    path('', index, name='index'),
    path('products/', index, name='products'),
    path('product/<int:pk>', product_detail, name='product_detail'),
]
