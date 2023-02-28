from django.shortcuts import render, get_object_or_404, redirect

from ..models import Product
from ..forms import SearchForm, ProductCreateForm


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/detail.html', context={
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


def product_create(request):
    match request.method:
        case 'GET':
            form = ProductCreateForm()
            return render(request, 'products/create.html', context={
                'form': form,
            })

        case 'POST':
            form = ProductCreateForm(request.POST)
            if not form.is_valid():
                return render(request, 'products/create.html', context={
                    'form': form,
                })

            Product.objects.create(**form.cleaned_data)
            return redirect('index')
