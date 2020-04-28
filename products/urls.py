from django.urls import path
from .views import (
    all_products,
    a_product,
    rings,
    bracelets,
    necklaces,
    earrings
    )


urlpatterns = [
    path('all/', all_products, name='products'),
    path('<int:id>', a_product, name='product'),
    path('rings/', rings, name='ring'),
    path('necklaces/', necklaces, name='necklace'),
    path('bracelets/', bracelets, name='bracelet'),
    path('earrings/', earrings, name='earring'),
]
