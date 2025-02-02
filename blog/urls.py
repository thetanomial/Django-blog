from django.urls import path
from blog.views import BlogCreateView, BlogListView, BlogDetailView

urlpatterns = [
    path("create/", BlogCreateView.as_view(), name="blog_create"),
    path("list/", BlogListView.as_view(), name="blog_list"),
    path('<int:pk>/',BlogDetailView.as_view(), name="blog_detail")

]
