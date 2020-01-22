from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def user_wishlist(request):
    """
    The users profile page
    """
    user = User.objects.get(email=request.user.email)
    return render(request, 'wishlist.html', {"profile": user})


def add_to_wishlist(request, id):
    """
    Add the specified product to the user wishlist
    """

    return redirect(reverse('index'))