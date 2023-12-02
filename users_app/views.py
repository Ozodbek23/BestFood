from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from rest_framework.permissions import IsAuthenticated
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet

from users_app.forms import TelegramUserForm, UserForm
from users_app.models import User, TelegramUser
from users_app.serializers import UserSerialzier, UserDetailSerializer, TelegramUserSerializer, \
    TelegramUserDetailSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialzier
    permission_classes = [IsAuthenticated]


    def get_serializer_class(self):
        if self.action == 'list':
            return UserSerialzier
        elif self.action == 'retrieve':
            return UserDetailSerializer
        return UserSerialzier


class TelegramUserViewSet(ModelViewSet):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUser
    permission_classes = [IsAuthenticated]


    def get_serializer_class(self):
        if self.action == 'list':
            return TelegramUserSerializer
        elif self.action == 'retrieve':
            return TelegramUserDetailSerializer
        return TelegramUserSerializer



class TelegramUserListView(ListView):
    model = TelegramUser
    template_name = 'telegram_user/list.html'
    context_object_name = 'telegram_user'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')

        if search:
            queryset = queryset.filter(
                Q(full_name__contains = search)
            )
        return queryset




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TelegramUserCreateView(CreateView):
    model = TelegramUser
    form_class = TelegramUserForm
    success_url = '/telegram_user/list/'
    template_name = 'telegram_user/form.html'


class TelegramUserUpdateView(UpdateView):
    model = TelegramUser
    form_class = TelegramUserForm
    success_url = '/telegram_user/'
    template_name = 'telegram_user/update.html'


class TelegramUserDetailView(DetailView):
    model = TelegramUser
    template_name = 'telegram_user/detail.html'
    context_object_name = 'telegram_user'


def telegram_user_delete(request, pk):
    telegram_user = get_object_or_404(TelegramUser, pk=pk)
    telegram_user.delete()
    return redirect('telegram_user-list')



class UserListView(ListView):
    model = User
    template_name = 'user/list.html'
    context_object_name = 'user'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')

        if search:
            queryset = queryset.filter(
                Q(first_name__contains=search) | Q(last_name__contains=search)
            )
        return queryset




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    success_url = '/user/list/'
    template_name = 'user/form.html'


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    success_url = '/user/'
    template_name = 'user/update.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'user/detail.html'
    context_object_name = 'user'


def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('user-list')




router = DefaultRouter()
router.register('user', UserViewSet, basename='user')
router.register('telegram_user', TelegramUserViewSet, basename='telegramuser')

