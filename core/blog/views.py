from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView,DetailView,RedirectView,FormView,CreateView,UpdateView
from .models import Post,Category
from django.shortcuts import get_list_or_404
from .forms import PostForm

class Index(TemplateView):
    
    """  Show a templates index """
    
    template_name = 'blog/index.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["name"] = "Morteza"
        context["post"] = Post.objects.all()
        return context
    
class RedirectMaktanKhoneh(RedirectView):
    
    """  Redirect To website  MaktanKhoneh """
    
    url = 'https://maktabkhooneh.org/'


class Posts(ListView):
    """
    To list the books on the main page based on their activeness
    
    """
    context_object_name = 'posts'
    paginate_by = 2
    ordering = ['created_date']
    
    def get_queryset(self):
        posts = Post.objects.filter(status=True).order_by('-created_date')
        return posts
 

class PostDetail(DetailView):
    """ Show details about each post """
    model = Post
    
    context_object_name = 'posts'
    
class PostForm(FormView):
    
    template_name ='blog/contact_us.html'
    form_class = PostForm
    success_url = '/posts/'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PostCreated(CreateView):
    
    model = Post
    fields = ['title','content','category','status','published_date']
    success_url = '/posts/'
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostEdit(UpdateView):
    
    model = Post
    form_class = PostForm
    success_url = '/posts/'
    template_name = 'blog/post_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)