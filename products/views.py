from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Product, Product_types


def all_products(request):
    """
    Create view to get all products and render the proucts page
    """
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
    """
    Create view to get a product by id and display just that one
    """
    product = Product.objects.get(id=id)
    return render(request, 'product.html', {"product": product})


def product_types(request):
    """
    Create view to get a product types
    """
    product_types = Product_types.object.all()
    return {'product_types': product_types}


def product_stock_count(request):
    """
    Create a view to get product stock levels
    """
    products = Product.objects.all()
    for product in products:
        product_stock = product.stock_count
    return {"product_stock": product_stock}


def rings(request):
    """
    Create view to get a product by type of ring
    """
    products = Product.objects.filter(product_type__name__iexact="ring")
    return render(request, "products.html", {"products": products})


def necklaces(request):
    """
    Create view to get a product by type of necklace
    """
    products = Product.objects.filter(product_type__name__iexact="necklace")
    return render(request, "products.html", {"products": products})


def bracelets(request):
    """
    Create view to get a product by type of bracelet
    """
    products = Product.objects.filter(product_type__name__iexact="bracelet")
    return render(request, "products.html", {"products": products})


def earrings(request):
    """
    Create view to get a product by type of earring
    """
    products = Product.objects.filter(product_type__name__iexact="earring")
    return render(request, "products.html", {"products": products})
