from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("apps.users.urls", namespace="users")),
    path("", include("apps.auths.urls", namespace="auths")),
    # --
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
]
