from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('', PasswordResetView, name='password_reset'),
    path('done/', PasswordResetDoneView, name='PasswordResetDoneView'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('complete', PasswordResetCompleteView,
         name='PasswordResetCompleteView')
]
