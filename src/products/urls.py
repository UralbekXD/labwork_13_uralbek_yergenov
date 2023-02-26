from django.urls import path


urlpatterns = [
    path('', index, name='index'),
    path('products/', index, name='products'),
]
