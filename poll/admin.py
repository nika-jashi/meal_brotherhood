from django.contrib import admin

from poll.models import Menu, RestaurantList, Decision

admin.site.register(Menu)
admin.site.register(RestaurantList)
admin.site.register(Decision)
