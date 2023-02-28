from django.shortcuts import render

from ..models import Product
from ..forms import SearchForm


def show_category(request):
    category = request.GET.get('category')
    form = SearchForm()
    result = Product.objects.filter(category__iexact=category)

    return render(request, 'products/search.html', context={
        'form': form,
        'categories': Product.CategoryChoices.choices,
        'products': result,
    })
