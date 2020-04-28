from django.shortcuts import render
from products.models import Product


# Create your views here.
def do_search(request):
    """
    Function to search the database for the website
    searching for a product that contains the search query
    """
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})