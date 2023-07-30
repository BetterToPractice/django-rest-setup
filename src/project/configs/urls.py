from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("", include("apps.users.urls", namespace="users")),
    path("", include("apps.auths.urls", namespace="auths")),
    # -- Admin and Auth --
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    # -- Third Party --
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
