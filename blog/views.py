from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    DetailView,
    UpdateView,
)
from .models import Post
from django.urls import reverse, reverse_lazy

# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "blog_list_view"


class BlogDetailView(DetailView):
    model = Post
    template_name = "detail.html"
    context_object_name = "detail_list_view"


class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    context_object_name = "post_new"
    fields = ["title", "author", "body", "created_date"]


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    context_object_name = "post_edit"
    fields = ["title", "body"]


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    context_object_name = "post_delete"
    success_url = reverse_lazy("home")
