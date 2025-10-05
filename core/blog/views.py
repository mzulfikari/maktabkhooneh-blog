from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import (
    ListView,
    DetailView,
    RedirectView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, Category
from django.shortcuts import get_list_or_404
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse


class Index(TemplateView):
    """Show a templates index"""

    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Morteza"
        context["post"] = Post.objects.all()
        return context


class RedirectMaktanKhoneh(RedirectView):
    """Redirect To website  MaktanKhoneh"""

    url = "https://maktabkhooneh.org/"


class Posts(LoginRequiredMixin, ListView):
    """
    To list the books on the main page based on their activeness

    """

    context_object_name = "posts"
    paginate_by = 2
    ordering = ["created_date"]

    def get_queryset(self):
        posts = Post.objects.filter(status=True).order_by("-created_date")
        return posts


class PostDetail(LoginRequiredMixin, DetailView):
    """Show details about each post"""

    model = Post

    context_object_name = "posts"


# class PostForm(FormView):

#     template_name ='blog/contact_us.html'
#     form_class = PostForm
#     success_url = '/posts/'

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class PostCreated(LoginRequiredMixin, CreateView):

    model = Post
    fields = ["title", "content", "category", "status", "published_date"]
    success_url = "/posts/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEdit(LoginRequiredMixin, UpdateView):

    model = Post
    form_class = PostForm
    success_url = "/posts/"
    template_name = "blog/post_form.html"


class PostDelete(LoginRequiredMixin, DeleteView):

    model = Post
    success_url = "/posts/"
