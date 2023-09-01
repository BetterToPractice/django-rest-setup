from rest_framework import generics

from .filters import PostFilter
from .models import Category, Post
from .permissions import PostPermission
from .serializers import CategorySerializer, PostSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "slug"


class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.select_related("user").prefetch_related("categories").all()
    serializer_class = PostSerializer
    permission_classes = [PostPermission]

    search_fields = ["title"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_class = PostFilter


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.select_related("user").prefetch_related("categories").all()
    serializer_class = PostSerializer
    lookup_field = "slug"
    permission_classes = [PostPermission]
