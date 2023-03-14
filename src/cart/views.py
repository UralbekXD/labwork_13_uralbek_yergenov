from django.shortcuts import render
from django.views.generic import ListView

from .models import ProductInCart


# Create your views here.
class CartList(ListView):
    model = ProductInCart
    template_name = 'cart/index.html'
    context_object_name = 'cart'



