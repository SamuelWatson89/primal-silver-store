from django.shortcuts import render
from .models import Product


def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def a_product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product.html', {"product": product})