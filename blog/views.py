from django.shortcuts import render

# Create your views here.
from django.contrib import messages 
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView,DetailView
from blog.models import BlogPost
from blog.forms import BlogCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin

class BlogDetailView(LoginRequiredMixin,DetailView):
    model = BlogPost
    template_name = "blog/detail.html"
    context_object_name = "blog"


class BlogListView(LoginRequiredMixin,ListView):
    model = BlogPost 
    template_name = "blog/list.html"
    context_object_name = "blogs"
    ordering = ["-id"]
    paginate_by = 6

class BlogCreateView(LoginRequiredMixin,CreateView):
    model = BlogPost
    form_class = BlogCreateForm

    template_name = 'blog/create.html'
    success_url = reverse_lazy('blog_list')


    def form_valid(self,form):
        form.instance.author = self.request.user
        messages.success(self.request,"Blog created successfully.")
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request,"Error creating blog post. Please correct the form.")
        return super().form_invalid(form)