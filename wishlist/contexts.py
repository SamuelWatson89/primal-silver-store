from django.shortcuts import get_object_or_404
from wishlist.models import Wishlist
from django.contrib.auth.models import User
from django.template import Context


def wishlist_contents(request):
    """
    Ensure that the users wishlist contents are available on every page
    """

    user = User.objects.get(email=request.user.email)
    wishlist = Wishlist.objects.filter(user_id=request.user.id)
    wishlist_count = wishlist.count()
    return {"profile": user, "wishlist": wishlist, "wishlist_count": wishlist_count}
