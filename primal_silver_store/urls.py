from django.contrib import admin
from django.urls import path, include
from accounts.views import index
from accounts import urls as accounts_urls
from products import urls as products_urls
from cart import urls as cart_urls
from search import urls as search_urls
from checkout import urls as checkout_urls
from wishlist import urls as wishlist_urls
from products.views import all_products
from django.views import static
from .settings import MEDIA_ROOT
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', TemplateView.as_view(
        template_name='../templates/about.html'), name='about'),
    path('contact', TemplateView.as_view(
        template_name='../templates/contact.html'), name='contact'),
    path('location', TemplateView.as_view(
        template_name='../templates/location.html'), name='location'),
    path('', all_products, name="index"),
    path('accounts/', include(accounts_urls)),
    path('products/', include(products_urls)),
    path('cart/', include(cart_urls)),
    path('search/', include(search_urls)),
    path('checkout/', include(checkout_urls)),
    path('wishlist/', include(wishlist_urls)),
    # path('media/<path>.', static.serve, {'document_root": MEDIA_ROOT'}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
