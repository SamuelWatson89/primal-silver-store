from django.core.paginator import Paginator
from django.shortcuts import render
from products.models import Product


def landing(request):
    products = Product.objects.all().order_by('?')[:5]
    return render(request, "landing.html", {'products': products})