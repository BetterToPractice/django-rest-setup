from apps.users.models import User
from django.db import transaction
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
    user = UserSerializer(read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    category_slugs = serializers.SlugRelatedField(
        write_only=True,
        queryset=Category.objects.all(),
        slug_field="slug",
        many=True,
    )

    class Meta:
        model = Post
        fields = (
            "title",
            "slug",
            "body",
            "categories",
            "category_slugs",
            "user",
        )

    @transaction.atomic
    def save(self, **kwargs):
        categories = self.validated_data.pop("category_slugs", None)
        post = super().save(user=self.context["request"].user, **kwargs)

        self.save_categories(post, categories)

        return post

    @classmethod
    def save_categories(cls, post, categories):
        if categories is None:
            return

        category_ids = [category.id for category in categories]
        if len(category_ids) == 0:
            post.categories.clear()
            return

        deleted_category_ids = post.categories.exclude(id__in=category_ids).values_list(
            "id", flat=True
        )

        post.categories.filter(id__in=deleted_category_ids).delete()
        post.categories.add(*category_ids)
