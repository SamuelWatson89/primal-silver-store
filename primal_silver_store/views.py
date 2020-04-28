from django.shortcuts import render
from products.models import Product, Product_types


def landing(request):
    products = Product.objects.all().order_by('?')[:5]
    product_types = Product_types.objects.all()
    return render(
        request, "landing.html", {
            'products': products,
            'product_types': product_types
            }
        )
