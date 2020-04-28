from django.shortcuts import render
from products.models import Product, Product_types


def landing(request):
    """
    View to create the landing page and
    get the required information from other app
    """
    products = Product.objects.all().order_by('?')[:5]
    product_types = Product_types.objects.all()
    return render(
        request, "landing.html", {
            'products': products,
            'product_types': product_types
            }
        )
