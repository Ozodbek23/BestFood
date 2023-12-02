from django.urls import path, include
from rest_framework.routers import DefaultRouter

from post_app import views
from post_app.views import PostViewSet

urlpatterns = [
    path('post/list/', views.PostListView.as_view(), name='post-list'),
    path('post/create/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/detail', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/delete', views.post_delete , name='post-delete'),
    path('api/', include(views.router.urls))
]