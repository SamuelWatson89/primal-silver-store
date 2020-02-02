from django.urls import path
from .views import user_wishlist, add_to_wishlist, remove_from_wishlist

urlpatterns = [
    path('', user_wishlist, name="user_wishlist"),
    path('add/(?<id>\d+)', add_to_wishlist, name='add_to_wishlist'),
    path('remove/(?<id>\d+)', remove_from_wishlist, name='remove_from_wishlist'),
]
