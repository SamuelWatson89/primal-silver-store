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
    path('rings/', rings, name='rings'),
    path('necklaces/', necklaces, name='necklaces'),
    path('bracelets/', bracelets, name='bracelets'),
    path('earrings/', earrings, name='earrings'),
]
