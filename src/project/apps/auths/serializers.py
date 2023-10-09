from apps.auths.mails import register_mail
from apps.auths.tokens import account_activation_token
from apps.users.models import User
from django.contrib.auth.models import update_last_login
from django.db import transaction
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from social_core.exceptions import AuthForbidden


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password",
            "avatar",
        )

    @transaction.atomic
    def save(self, **kwargs):
        user = super().save(**kwargs)
        user.set_password(self.validated_data["password"])
        user.save()

        self.send_email(user)

        return user

    @classmethod
    def send_email(cls, user):
        register_mail.send(
            receiver=user.email,
            context={"name": user.email, "url": cls.generate_activate_url(user)},
        )

    @classmethod
    def generate_activate_url(cls, user):
        return account_activation_token.generate_url(user)


class LoginSocialSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)

    def __init__(self, *args, **kwargs):
        self.backend = kwargs.pop("backend", None)
        super().__init__(*args, **kwargs)

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.get_user_by_token(data)
        token = self.get_token(user)

        self.send_email(user)
        update_last_login(None, user)

        return token

    def get_user_by_token(self, data):
        try:
            user = self.backend.do_auth(data["token"])
        except AuthForbidden as e:
            raise serializers.ValidationError({"token": str(e)})

        if not user:
            raise serializers.ValidationError({"token": "Invalid Token"})
        return user

    @classmethod
    def get_token(cls, user):
        token = RefreshToken.for_user(user)
        return {"refresh": str(token), "access": str(token.access_token)}

    @classmethod
    def send_email(cls, user):
        if user.last_login is None:
            register_mail.send(
                receiver=user.email,
                context={
                    "username": user.username,
                },
            )
