from django.urls import path, include
from .views import all_products, a_product


urlpatterns = [
    path('', all_products, name='products'),
    path('product/?P<id>', a_product, name='product'),
]
