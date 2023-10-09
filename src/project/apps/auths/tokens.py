from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return f"{user.pk}{timestamp}{user.is_email_confirmed}"

    @classmethod
    def generate_user_uid(cls, user):
        return urlsafe_base64_encode(force_bytes(user.pk))

    def generate(self, user):
        return self.make_token(user), self.generate_user_uid(user)

    def generate_url(self, user):
        token, uid = self.generate(user)
        return settings.FRONTEND_ACTIVATE_URL.format(uid=uid, token=token)


account_activation_token = AccountActivationTokenGenerator()
