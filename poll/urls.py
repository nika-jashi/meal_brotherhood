from django.urls import path
import poll
from poll import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('1/', views.in_or_out, name='poll1'),
   path('2/', views.choose_restaurant, name='poll2'),
   path('3/', views.fill_form, name='poll3'),
]
