from django.urls import path

from .views import MeAPIView, MePasswordAPIView

app_name = "users"

urlpatterns = [
    path("me/", MeAPIView.as_view(), name="me"),
    path("me/password/", MePasswordAPIView.as_view(), name="me-password"),
]
