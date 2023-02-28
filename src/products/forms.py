from django import forms

from .models import Product


class SearchForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'search',
            'placeholder': 'Search',
            'id': 'title',
        })
    )


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'category', 'image', 'price', 'amount', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control mb-3'
            }),
            'category': forms.Select(
                choices=Product.CategoryChoices.choices,
                attrs={
                    'class': 'form-select mb-3'
                }
            ),
            'image': forms.TextInput(attrs={
                'class': 'form-control mb-3'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control mb-3'
            }),
            'amount': forms.NumberInput(attrs={
                'min': 0,
                'class': 'form-control mb-3'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control mb-3'
            })
        }
