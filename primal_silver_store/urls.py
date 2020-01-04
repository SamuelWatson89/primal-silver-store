from django.contrib import admin
from django.urls import path, include
from accounts.views import index
from accounts import urls as accounts_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('accounts/', include(accounts_urls))
]
