from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address_line1 = models.CharField(max_length=84, blank=True, null=True)
    address_line2 = models.CharField(max_length=84, blank=True, null=True)
    town_city = models.CharField(max_length=84, blank=True, null=True)
    county = models.CharField(max_length=84, blank=True, null=True)
    postcode = models.CharField(max_length=8, blank=True, null=True)
    country = models.CharField(max_length=84, blank=True, null=True)

    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
