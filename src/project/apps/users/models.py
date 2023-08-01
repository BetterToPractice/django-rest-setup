from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group as DjangoGroup
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = "users_users"

    def __str__(self):
        return self.email


class Group(DjangoGroup):
    class Meta:
        proxy = True
        verbose_name = _("group")
        verbose_name_plural = _("groups")

    def __str__(self):
        return self.name
