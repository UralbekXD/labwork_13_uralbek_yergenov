from django import forms


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
