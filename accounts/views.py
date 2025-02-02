from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib import messages
from django.urls import reverse_lazy

class UserLoginView(LoginView):
    template_name = "accounts/login.html"

    def get_success_url(self):
        return reverse_lazy("blog_list")


class UserLogoutView(LogoutView):

    template_name = "accounts/logout.html"

    next_page = reverse_lazy("login")

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have successfully logged out.")
        return super().dispatch(request, *args, **kwargs)