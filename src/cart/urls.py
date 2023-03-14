from django.urls import path

from .views import *

urlpatterns = [
    path('', CartList.as_view(), name='cart'),
]