from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Wishlist(models.Model):
    user = models.ForeignKey(User, related_name='wishlist', on_delete=models.CASCADE)
    list_name = models.CharField(max_length=20)
    items = models.ManyToManyField(Product)

    def __str__(self):
        return self.name