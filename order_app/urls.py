from django.urls import path, include

from order_app import views


urlpatterns = [
    path('order/list/', views.OrderListView.as_view(), name='order-list'),
    path('order/create/', views.OrderCreateView.as_view(), name='order-create'),
    path('order/<int:pk>/update', views.OrderUpdateView.as_view(), name='order-update'),
    path('order/<int:pk>/detail', views.OrderDetailView.as_view(), name='order-detail'),
    path('order/<int:pk>/delete', views.order_delete , name='order-delete'),
    path('order_food/list/', views.OrderFoodListView.as_view(), name='order_food-list'),
    path('order_food/create/', views.OrderFoodCreateView.as_view(), name='order_food-create'),
    path('order_food/<int:pk>/update', views.OrderFoodUpdateView.as_view(), name='order_food-update'),
    path('order_food/<int:pk>/detail', views.OrderFoodDetailView.as_view(), name='order_food-detail'),
    path('order_food/<int:pk>/delete', views.order_food_delete , name='order_food-delete'),
    path('api/', include(views.router.urls))
]


