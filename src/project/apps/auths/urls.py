from django.urls import path

from .views import LoginAPIView, RefreshTokenAPIView, RegisterAPIView

app_name = "auths"

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
    path("refresh-token/", RefreshTokenAPIView.as_view(), name="refresh-token"),
    path("register/", RegisterAPIView.as_view(), name="register"),
]
