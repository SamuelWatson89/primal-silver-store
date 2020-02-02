from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from products.models import Product
from .models import Wishlist


@login_required
def user_wishlist(request):
    """
    The users profile page
    """
    user = User.objects.get(email=request.user.email)
    wishlist = Wishlist.objects.filter(user_id=request.user.id)
    return render(request, 'wishlist.html', {"profile": user, "wishlist": wishlist})


@login_required
def add_to_wishlist(request, id):
    """
    Add the specified product to the user wishlist
    """
    item = get_object_or_404(Product, pk=id)

    product, date_added = Wishlist.objects.get_or_create(product=item,
                                                         user=request.user,
                                                         )

    messages.info(request, 'The item was added to your wishlist')
    return redirect(reverse('index'))


@login_required
def remove_from_wishlist(request, id):
    """
    Remove the specified item from the users wishlist
    """
    Wishlist.objects.filter(id=id).delete()
    return redirect(reverse('user_wishlist'))
