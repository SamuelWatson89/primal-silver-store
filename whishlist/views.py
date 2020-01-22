from django.shortcuts import render, redirect, reverse


def view_wishlist(request):
    """
    View that renders the wishlist contents
    """
    return render(request, 'whishlist.html')


def add_to_wishlist(request, id):
    """
    Add a quantity of the specified product to the users wishlist
    """


def remove_from_whishlist(request, id):
    """
    Remove an item from the whishlist
    """
