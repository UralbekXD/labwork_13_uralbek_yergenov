from django.shortcuts import render, get_object_or_404

from ..models import Product
from ..forms import SearchForm


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', context={
        'product': product,
    })


def product_search(request):
    form = SearchForm()
    query = request.GET.get('title')
    result = Product.objects.filter(title__icontains=query)

    return render(request, 'products/search.html', context={
        'form': form,
        'categories': Product.CategoryChoices.choices,
        'products': result,
    })

