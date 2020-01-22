from django.urls import path
from .views import user_wishlist, add_to_wishlist

urlpatterns = [
    path('', user_wishlist, name="user_wishlist"),
    path('add/(?<id>\d+)', add_to_wishlist, name='add_to_wishlist'),
]