from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.db.models import Sum
from functools import reduce

from .models import ProductInCart
from products.models import Product


class CartItemList(ListView):
    model = ProductInCart
    template_name = 'cart/index.html'
    context_object_name = 'cart'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        cart_sum = 0
        for item in context['cart']:
            cart_sum += item.product.price * item.quantity
        context['sum'] = cart_sum

        return context


class CartItemAdd(View):
    def post(self, request, *args, **kwargs):
        product_pk = kwargs.get('pk')
        product = Product.objects.get(pk=product_pk)
        if product.amount > 0:
            product_cart = ProductInCart.objects.filter(product__pk=product_pk)
            if product_cart.exists():
                item = product_cart.first()
                if item.quantity < product.amount:
                    item.quantity += 1

                item.save()
            else:
                ProductInCart.objects.create(
                    product=product,
                    quantity=1,
                )

        return redirect('index')


class CartItemRemove(DeleteView):
    model = ProductInCart
    success_url = reverse_lazy('cart')
