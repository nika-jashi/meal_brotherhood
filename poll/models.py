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
