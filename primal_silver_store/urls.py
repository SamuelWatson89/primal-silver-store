from django.contrib import admin
from django.urls import path, include
from accounts.views import index
from accounts import urls as accounts_urls
from products import urls as products_urls
from cart import urls as cart_urls
from products.views import all_products
from django.views import static
from .settings import MEDIA_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', all_products, name="index"),
    path('accounts/', include(accounts_urls)),
    path('products/', include(products_urls)),
    path('cart/', include(cart_urls)),
    path('media/(<path>.*)/', static.serve, {'document_root": MEDIA_ROOT'})
]
