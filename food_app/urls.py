from django.urls import path, include
from rest_framework.routers import DefaultRouter

from food_app import views
from food_app.views import CategoryViewSet, FoodViewSet, index
from register_login.views import login_required


urlpatterns = [
    path('category/list/', views.CategoryListView.as_view(), name='category-list'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('category/<int:pk>/update', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category/<int:pk>/detail', views.CategoryDetailView.as_view(), name='category-detail'),
    path('category/<int:pk>/delete', views.category_delete , name='category-delete'),
    path('food/list/', views.FoodListView.as_view(), name='food-list'),
    path('food/create/', views.FoodCreateView.as_view(), name='food-create'),
    path('food/<int:pk>/update', views.FoodUpdateView.as_view(), name='food-update'),
    path('food/<int:pk>/detail', views.FoodDetailView.as_view(), name='food-detail'),
    path('food/<int:pk>/delete', views.food_delete , name='food-delete'),
    path('api/', include(views.router.urls))
]


