from django.shortcuts import render, get_object_or_404, redirect

from ..models import Product
from ..forms import SearchForm, ProductForm


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
            form = ProductForm()
            return render(request, 'products/create.html', context={
                'form': form,
            })

        case 'POST':
            form = ProductForm(request.POST)
            if not form.is_valid():
                return render(request, 'products/create.html', context={
                    'form': form,
                })

            Product.objects.create(**form.cleaned_data)
            return redirect('index')


def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    match request.method:
        case 'GET':
            form = ProductForm(instance=product)
            return render(request, 'products/update.html', context={
                'pk': product.pk,
                'form': form,
            })

        case 'POST':
            form = ProductForm(request.POST)
            if not form.is_valid():
                return render(request, 'products/update.html', context={
                    'form': form,
                })

            # SUCCESS
            product.author = form.cleaned_data.get('author')
            product.email = form.cleaned_data.get('email')
            product.description = form.cleaned_data.get('description')
            product.save()

            return redirect('home')