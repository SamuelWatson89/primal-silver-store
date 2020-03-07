from django.shortcuts import render
from .models import Product


def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def a_product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product.html', {"product": product})


def rings(request):
    products = Product.objects.filter(product_type__name__iexact="ring")
    return render(request, "products.html", {"products": products})


def necklaces(request):
    products = Product.objects.filter(product_type__name__iexact="necklace")
    return render(request, "products.html", {"products": products})


def bracelets(request):
    products = Product.objects.filter(product_type__name__iexact="bracelet")
    return render(request, "products.html", {"products": products})
