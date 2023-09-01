from django.urls import path

from .views import PostDetailAPIView, PostListAPIView

app_name = "blog"

urlpatterns = [
    path("posts/", PostListAPIView.as_view(), name="post-list"),
    path("posts/<slug:slug>/", PostDetailAPIView.as_view(), name="post-detail"),
]
