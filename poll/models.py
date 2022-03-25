from django.contrib.auth.models import User
from django.db import models


class RestaurantList(models.Model):
    restaurant_name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.restaurant_name


class Menu(models.Model):
    menu = models.TextField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.menu


class Decision(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    res = models.ForeignKey(RestaurantList, null=True, blank=True, on_delete=models.DO_NOTHING)
    menu = models.ForeignKey(Menu, null=True, blank=True, on_delete=models.DO_NOTHING)
    on_site = models.BooleanField(default=0)
    orderer = models.BooleanField(default=0)
