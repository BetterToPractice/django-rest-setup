from django.contrib.auth import get_user_model
from django.test import TestCase


class UserModelTest(TestCase):
    def test_success_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="test@example.com", password="p@ssw0rd11")

        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_success_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(email="test@example.com", password="p@ssw0rd11")

        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
