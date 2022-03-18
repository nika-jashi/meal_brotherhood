from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
import user
from user.views import dashboard
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logged_out.html'), name='logout'),
    path('register/', user.views.register, name='register'),
    path('', dashboard, name="dashboard"),
    path('profile/', user.views.profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
