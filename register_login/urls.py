from django.urls import path
from rest_framework import authentication

from register_login import views

urlpatterns = [
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
]
