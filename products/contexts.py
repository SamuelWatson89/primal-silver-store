from .models import Product
from django.template import Context


def product_stock_count(request):
    """
    Global access to the product stock counts
    """

    products = Product.objects.all()
    for product in products:
        product_stock = product.stock_count
    return {"product_stock": product_stock}
