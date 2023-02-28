from django.shortcuts import render

from ..models import Product


def index(request):
    products = Product.objects.filter(amount__gt=0).order_by('category', 'title')
    print(Product.CategoryChoices.choices)
    return render(request, 'products/index.html', context={
        'products': products,
        'categories': Product.CategoryChoices.choices,
    })
