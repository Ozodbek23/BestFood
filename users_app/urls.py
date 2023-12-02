
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users_app import views
from register_login.views import login_required


urlpatterns = [
    path('telegram_user/list/', views.TelegramUserListView.as_view(), name='telegram_user-list'),
    path('telegram_user/create/', views.TelegramUserCreateView.as_view(), name='telegram_user-create'),
    path('telegram_user/<int:pk>/update', views.TelegramUserUpdateView.as_view(), name='telegram_user-update'),
    path('telegram_user/<int:pk>/detail', views.TelegramUserDetailView.as_view(), name='telegram_user-detail'),
    path('telegram_user/<int:pk>/delete', views.telegram_user_delete, name='telegram_user-delete'),
    path('user/list/', views.UserListView.as_view(), name='user-list'),
    path('user/create/', views.UserCreateView.as_view(), name='user-create'),
    path('user/<int:pk>/update', views.UserUpdateView.as_view(), name='user-update'),
    path('user/<int:pk>/detail', views.UserDetailView.as_view(), name='user-detail'),
    path('user/<int:pk>/delete', views.user_delete , name='user-delete'),
    path('api/', include(views.router.urls))
]


