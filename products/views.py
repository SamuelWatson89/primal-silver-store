from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product


def all_products(request):
    product_list = Product.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(product_list, 10)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {'products': products})


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


def earrings(request):
    products = Product.objects.filter(product_type__name__iexact="earrings")
    return render(request, "products.html", {"products": products})
