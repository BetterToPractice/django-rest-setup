from apps.users.models import User
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers


class MeSerializer(serializers.ModelSerializer):
    avatar = Base64ImageField(required=False)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "avatar",
        )


class MePasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(required=True, style={"input_type": "password"})
    confirm_password = serializers.CharField(required=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = (
            "new_password",
            "confirm_password",
        )

    @classmethod
    def validation_password(cls, data):
        if data["new_password"] != data["confirm_password"]:
            raise serializers.ValidationError({"new_password": "invalid unmatched password"})

    def validate(self, attrs):
        data = super().validate(attrs)
        self.validation_password(data)
        return data

    def save(self, **kwargs):
        user = self.context["request"].user
        user.set_password(self.validated_data["new_password"])
        user.save()
        return user
