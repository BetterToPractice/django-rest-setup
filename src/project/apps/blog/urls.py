from django.urls import path

from .views import (
    CategoryDetailAPIView,
    CategoryListAPIView,
    PostDetailAPIView,
    PostListAPIView,
)

app_name = "blog"

urlpatterns = [
    path("categories/", CategoryListAPIView.as_view(), name="category-list"),
    path("categories/<slug:slug>/", CategoryDetailAPIView.as_view(), name="category-detail"),
    path("posts/", PostListAPIView.as_view(), name="post-list"),
    path("posts/<slug:slug>/", PostDetailAPIView.as_view(), name="post-detail"),
]
