from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Wishlist(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user',
        on_delete=models.CASCADE, null=True
        )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
