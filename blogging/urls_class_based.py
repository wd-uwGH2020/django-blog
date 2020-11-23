# polling/urls.py

from django.urls import path
from blogging.views_class_based import BlogListView, BlogDetailView

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
]
