from django.urls import path
from .views import user_wishlist

urlpatterns = [
    path('', user_wishlist, name="user_wishlist"),
]