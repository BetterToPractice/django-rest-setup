from django.urls import path

from .views import (
    ActivateAccountAPIView,
    LoginAPIView,
    LoginSocialAPIView,
    RefreshTokenAPIView,
    RegisterAPIView,
)

app_name = "auths"

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
    path("login-social/<str:backend>/", LoginSocialAPIView.as_view(), name="login-social"),
    path("refresh-token/", RefreshTokenAPIView.as_view(), name="refresh-token"),
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("activate-account/", ActivateAccountAPIView.as_view(), name="activate-account"),
]
