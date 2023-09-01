from apps.blog.models import Post
from django_filters import rest_framework as filters


class PostFilter(filters.FilterSet):
    class Meta:
        model = Post
        fields = ("user__email",)
