from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.routers import DefaultRouter

from rest_framework.viewsets import ModelViewSet

from food_app.forms import CategoryForm, FoodForm
from food_app.models import Category, Food
from food_app.serializer import CategorySerializer, FoodSerializer, CategoryDetailSerializer, FoodDetailSerializer



class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        elif self.action == 'retrieve':
            return CategoryDetailSerializer
        return CategorySerializer

    # def get_queryset(self):
    #     queryset = self.queryset
    #     queryset = queryset.filter(is_active=True)
    #     return queryset


class FoodViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return FoodDetailSerializer
        elif self.action == 'list':
            return FoodSerializer
        return FoodSerializer


def index(request):
    return render(request, 'index.html')




class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search','')
        if search:
            queryset = queryset.filter(
                Q(name__contains=search)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.request.GET.get('category', '')

        return context



class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = '/category/list/'
    template_name = 'category/form.html'


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = '/category/list/'
    template_name = 'category/form.html'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/detail.html'
    context_object_name = 'category'


def category_delete(request , pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('category-list')





class FoodListView(ListView):
    model = Food
    template_name = 'food/list.html'
    context_object_name = 'foods'


    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        category = self.request.GET.get('category', '')
        if search:
            queryset = queryset.filter(
                Q(name__contains=search)
            )

        if category:
            queryset = queryset.filter(
                category=category
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()

        context['search'] = self.request.GET.get('search', '')
        context['category_id'] = self.request.GET.get('category_id', '')
        category_id = self.request.GET.get('category_id', '')
        if category_id:
            category_id = int(category_id)
        else:
            category_id = 0

        context['category_id'] = category_id

        return context


class FoodCreateView(CreateView):
    model = Food
    form_class = FoodForm
    success_url = '/food/list/'
    template_name = 'food/form.html'



class FoodUpdateView(UpdateView):
    model = Food
    form_class = FoodForm
    success_url = '/food/list/'
    template_name = 'food/form.html'


class FoodDetailView(DetailView):
    model = Food
    template_name = 'food/detail.html'
    context_object_name = 'food'


def food_delete(request , pk):
    food = get_object_or_404(Food, pk=pk)
    food.delete()
    return redirect('food-list')





router = DefaultRouter()
router.register('category', CategoryViewSet, basename='categories')
router.register('food', FoodViewSet, basename='foods')