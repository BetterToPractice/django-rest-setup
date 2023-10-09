from apps.users.models import User
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.exceptions import ValidationError
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return f"{user.pk}{timestamp}{user.is_email_confirmed}"

    @classmethod
    def generate_user_uid(cls, user):
        return urlsafe_base64_encode(force_bytes(user.pk))

    @classmethod
    def get_user_by_uid(cls, uid):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            user_id = urlsafe_base64_decode(uid).decode()
            user = User.objects.get(pk=user_id)
        except (
            TypeError,
            ValueError,
            OverflowError,
            User.DoesNotExist,
            ValidationError,
        ):
            user = None
        return user

    def generate(self, user):
        return self.make_token(user), self.generate_user_uid(user)

    def generate_url(self, user):
        token, uid = self.generate(user)
        return settings.FRONTEND_ACTIVATE_URL.format(uid=uid, token=token)

    def validate(self, uid, token):
        user = self.get_user_by_uid(uid)
        if user is None or not self.check_token(user, token):
            return None, False
        return user, True


account_activation_token = AccountActivationTokenGenerator()
