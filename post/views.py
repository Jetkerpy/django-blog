
from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
)

from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Post, Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

class CreateCommentView(CreateView):
    model = Comment
    fields = ["post","comment"]
    template_name = 'create_comment.html'

    def form_valid(self, form, *args, **kwargs):
        # post = get_object_or_404(Post, pk = self.kwargs['pk'])
        form.instance.author = self.request.user
        
        return super().form_valid(form)



class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'detail.html'



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "summary", "body", "photo"]
    template_name = 'create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = "__all__"
    template_name = 'update_post.html'


    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('postlar')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
