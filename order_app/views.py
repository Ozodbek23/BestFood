from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from rest_framework.permissions import IsAuthenticated
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet

from food_app.models import Food
from order_app.forms import OrderForm, OrderFoodForm
from order_app.models import Order, OrderFood
from order_app.serializers import OrderSerializer, OrderFoodSerializer, OrderDetailSerializer
from users_app.models import TelegramUser


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return OrderSerializer
        elif self.action == 'retrieve':
            return OrderDetailSerializer
        return OrderSerializer


class OrderFoodViewSet(ModelViewSet):
    queryset = OrderFood.objects.all()
    serializer_class = OrderFoodSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return OrderFoodSerializer
        elif self.action == 'retrieve':
            return OrderDetailSerializer
        return OrderFoodSerializer


class OrderListView(ListView):
    model = Order
    template_name = 'order/list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search',)
        telegram_user = self.request.GET.get('telegram_user', '')

        if search:
            queryset = queryset.filter(
                Q(foods__conatins=search)
            )

        if telegram_user:
            queryset = queryset.filter(
                telegram_user=telegram_user
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['telegram_user'] = TelegramUser.objects.all()

        context['search'] = self.request.GET.get('search', '')
        context['telegram_user_id'] = self.request.GET.get('telegram_user_id', '')
        telegram_user_id = self.request.GET.get('telegram_user_id', '')

        if telegram_user_id:
            telegram_user_id = int(telegram_user_id)

        else:
            telegram_user_id = 0

        context['telegram_user_id'] = telegram_user_id
        return context


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = '/order/list/'
    template_name = 'order/form.html'


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    success_url = '/order/list/'
    template_name = 'order/form.html'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order/detail.html'
    context_object_name = 'order'


def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('order-list')


class OrderFoodListView(ListView):
    model = OrderFood
    template_name = 'order_food/list.html'
    context_object_name = 'order_foods'

    def get_queryset(self):
        queryset = super().get_queryset()
        food = self.request.GET.get('food', '')
        order = self.request.GET.get('order', '')

        if food:
            queryset = queryset.filer(
                food = food
            )

        if order:
            queryset = queryset.filer(
                order = order
            )


        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['order'] = Order.objects.all()
        context['food'] = Food.objects.all()

        context['order_id'] = self.request.GET.get('order_id', '')
        context['food_id'] = self.request.GET.get('food_id', '')
        order_id = self.request.GET.get('order_id','')
        food_id = self.request.GET.get('food_id','')

        if food_id:
            food_id = int(food_id)
        else:
            food_id = 0

        if order_id:
            order_id = int(order_id)
        else:
            order_id = 0

        context['order_id'] = order_id
        context['food_id'] = food_id

        return context


class OrderFoodCreateView(CreateView):
    model = OrderFood
    form_class = OrderFoodForm
    success_url = '/order_food/list/'
    template_name = 'order_food/form.html'


class OrderFoodUpdateView(UpdateView):
    model = OrderFood
    form_class = OrderFoodForm
    success_url = '/order_food/list/'
    template_name = 'order_food/form.html'


class OrderFoodDetailView(DetailView):
    model = OrderFood
    template_name = 'order_food/detail.html'
    context_object_name = 'order_food'


def order_food_delete(request, pk):
    order_food = get_object_or_404(OrderFood, pk=pk)
    order_food.delete()
    return redirect('order_food-list')


router = DefaultRouter()
router.register('order', OrderViewSet, basename='order')
router.register('order_food', OrderFoodViewSet, basename='order_food')
