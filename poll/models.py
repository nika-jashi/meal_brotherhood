from django.contrib.auth.models import User
from django.db import models


class RestaurantsList(models.Model):
    restaurant_name = models.CharField(max_length=30)

    def __str__(self):
        return self.restaurant_name


class Questionary(models.Model):
    menu = models.TextField(max_length=256, null=True, blank=True)
    going_out = models.BooleanField(default=0)
