from django.shortcuts import render

from ..models import Product
from ..forms import SearchForm

def index(request):
    form = SearchForm()
    products = Product.objects.filter(amount__gt=0).order_by('category', 'title')
    return render(request, 'products/index.html', context={
        'form': form,
        'products': products,
        'categories': Product.CategoryChoices.choices,
    })
