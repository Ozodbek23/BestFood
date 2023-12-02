from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from post_app.forms import PostForm
from post_app.models import Post, PostImage
from post_app.serializers import PostListSerializer, PostImageSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]


    def get_serializer_class(self):
        return PostListSerializer

class PostImageViewSet(ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer
    permission_classes = [IsAuthenticated]


    def get_serializer_class(self):
        return PostImageSerializer


class PostListView(ListView):
    model = Post
    template_name = 'post/list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search','')

        if search:
            queryset = queryset.filter(
                Q(title__contains=search)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = '/post/list/'
    template_name = 'post/form.html'


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/post/list/'
    template_name = 'post/form.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'
    context_object_name = 'post'


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post-list')


router = DefaultRouter()
router.register('post', PostViewSet , basename='post')
router.register('post_image', PostImageViewSet , basename='post-image')
urlpatterns = router.urls