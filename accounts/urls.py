from django.urls import path, include
from accounts.views import index, logout, login, registration, user_profile, update_profile
from accounts import url_reset

urlpatterns = [
    path('logout/', logout, name="logout"),
    path('login/', login, name="login"),
    path('register/', registration, name="register"),
    path('profile/', user_profile, name="profile"),
    path('password-reset/', include(url_reset)),
    path('profile/update', update_profile, name="update_profile"),
]
