from django.urls import path

from .views import *

urlpatterns = [
    path('', CartItemList.as_view(), name='cart'),
    path('add/<int:pk>', CartItemAdd.as_view(), name='cart_add'),
    path('delete/<int:pk>', CartItemRemove.as_view(), name='cart_remove'),
]
