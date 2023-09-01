from apps.users.models import User
from rest_framework import serializers

from .models import Category, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "name",
            "slug",
        )


class PostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = Post
        fields = (
            "title",
            "slug",
            "body",
            "categories",
            "user",
        )
