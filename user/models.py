from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from poll.models import RestaurantList, Menu


class Profile(models.Model):
    menu = models.ForeignKey(Menu, null=True, on_delete=models.SET_NULL)
    res = models.ForeignKey(RestaurantList, max_length=30, null=True, blank=True, on_delete=models.SET_NULL)
    on_site = models.BooleanField(default=False)
    who_orders = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_pic.png',
                              upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
