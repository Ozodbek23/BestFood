from django.urls import path, include

from post_app import views


urlpatterns = [
    path('post/list/', views.PostListView.as_view(), name='post-list'),
    path('post/create/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/detail', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/delete', views.post_delete , name='post-delete'),
    path('', include(views.router.urls))
]



class PostListView(ListView):
    model = Post
    template_name = 'post/list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        # search = self.request.GET.get('search',)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.request.GET.get('post', '')

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

