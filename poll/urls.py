from django.urls import path
from poll import views
from django.contrib.auth.decorators import login_required as l_req

app_name = 'poll'
urlpatterns = [
   # path('1/', l_req(views.InOrOut.as_view()), name='want_to_eat'),
   # path('2/', l_req(views.ChooseRestaurant.as_view()), name='location'),
   # path('3/', l_req(views.fill_form), name='restaurant_menu'),
   path('4/', l_req(views.Result.as_view()), name='result'),
   # path('5/', l_req(views.orderer), name='ordering'),
   path('ordering/', l_req(views.Main.as_view()), name='ordering'),

]

