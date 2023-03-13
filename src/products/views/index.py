from django.shortcuts import render
from django.views.generic import ListView

from ..models import Product
from ..forms import SearchForm


class Index(ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm()
        context['categories'] = Product.CategoryChoices.choices
        return context

    def get_queryset(self):
        return Product.objects.filter(amount__gt=0).order_by('category', 'title')

