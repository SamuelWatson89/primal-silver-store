from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Product, Product_types


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


def product_types(request):
    product_types = Product_types.object.all()
    return {'product_types': product_types}


def product_stock_count(request):
    """
    Global access to the product stock counts
    """

    products = Product.objects.all()
    for product in products:
        product_stock = product.stock_count
    return {"product_stock": product_stock}


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
