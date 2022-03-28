from django.urls import path
from .views import (PostDetailView,
                    PostCreateView, PostUpdateView,
                    PostDeleteView, PostListView
                    )
from django.contrib.auth.decorators import login_required as l_req

urlpatterns = [
    path('', l_req(PostListView.as_view()), name='checks-home'),
    path('user/<str:username>', PostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
]
