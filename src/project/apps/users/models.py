from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group as DjangoGroup
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    avatar = models.ImageField(_("avatar"), null=True, blank=True, upload_to="users/users")

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


class Profile(models.Model):
    MALE, FEMALE = "male", "female"
    GENDER_CHOICES = (
        (MALE, _("Male")),
        (FEMALE, _("Female")),
    )

    phone_number = PhoneNumberField(blank=True)
    gender = models.CharField(
        _("gender"),
        choices=GENDER_CHOICES,
        null=True,
        blank=True,
    )

    user = models.OneToOneField("users.User", related_name="profile", on_delete=models.CASCADE)

    class Meta:
        db_table = "users_profiles"
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")
