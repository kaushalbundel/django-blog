#!/usr/bin/env python3
from django.urls import path
from .views import (
    BlogDeleteView,
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
)

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("detail/<int:pk>/", BlogDetailView.as_view(), name="detail"),
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    path("detail/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
]
