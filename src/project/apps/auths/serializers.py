from apps.users.models import User
from django.db import transaction
from rest_framework import serializers


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
        return user
