from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from ..models import Product
from ..forms import SearchForm, ProductForm


class ProductSearch(ListView):
    model = Product
    template_name = 'products/search.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm()
        context['categories'] = Product.CategoryChoices.choices
        return context

    def get_queryset(self):
        query = self.request.GET.get('title')
        return Product.objects.filter(title__icontains=query)


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'


class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('index')


class ProductEdit(UpdateView):
    model = Product
    template_name = 'products/update.html'
    form_class = ProductForm
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('index')
