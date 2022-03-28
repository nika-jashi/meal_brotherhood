from django.urls import path
from poll import views
from django.contrib.auth.decorators import login_required as l_req

app_name = 'poll'
urlpatterns = [
   path('results/', l_req(views.Result.as_view()), name='result'),
   path('ordering/', l_req(views.Main.as_view()), name='ordering'),

]

