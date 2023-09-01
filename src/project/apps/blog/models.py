from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(_("name"), db_index=True, max_length=200)
    slug = AutoSlugField(populate_from="name")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "blog_categories"
        ordering = ("name",)
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(_("title"), max_length=200)
    slug = AutoSlugField(populate_from="title")
    body = RichTextField(null=True)

    categories = models.ManyToManyField(
        "blog.Category",
        through="PostCategory",
        verbose_name=_("categories"),
    )
    user = models.ForeignKey(
        "users.User",
        related_name="blog_posts",
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "blog_posts"
        ordering = ("-created_at",)
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title


class PostCategory(models.Model):
    post = models.ForeignKey("blog.Post", on_delete=models.CASCADE, verbose_name=_("Product"))
    category = models.ForeignKey("blog.Category", on_delete=models.CASCADE, verbose_name=_("Category"))

    class Meta:
        db_table = "blog_post_categories"
        verbose_name = _("Post category")
        verbose_name_plural = _("Post categories")

    def __str__(self):
        return self.post.title
