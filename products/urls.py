from django.urls import path, include
from .views import all_products, a_product, rings, bracelets, necklaces


urlpatterns = [
    path('', all_products, name='products'),
    path('?P<id>', a_product, name='product'),
    path('rings/', rings, name='rings'),
    path('necklaces/', necklaces, name='necklaces'),
    path('bracelets/', bracelets, name='bracelets'),
]
