from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404


class BlogListView(ListView):
    model = Post
    template_name = 'blogging/list_class_based.html'
    queryset = Post.objects.exclude(published_date__exact=None).order_by('-published_date')


class BlogDetailView(DetailView):
    model = Post
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = 'blogging/detail_class_based.html'
   