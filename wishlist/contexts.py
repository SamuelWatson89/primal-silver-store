from wishlist.models import Wishlist


def wishlist_contents(request):
    """
    Ensure that the users wishlist contents are available on every page
    """
    if request.user.is_authenticated:
        wishlist = Wishlist.objects.filter(user_id=request.user.id)
        wishlist_count = wishlist.count()
        return {"wishlist_count": wishlist_count}
    else:
        return {}
