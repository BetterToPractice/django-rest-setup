from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

# Admin Config
admin.site.site_header = "Project Admin"
admin.site.site_title = "Project Admin Dashboard"
admin.site.index_title = "Welcome to Project Admin Dashboard"

urlpatterns = [
    path("", include("apps.users.urls", namespace="users")),
    path("", include("apps.auths.urls", namespace="auths")),
    path("", include("apps.blog.urls", namespace="blog")),
    # --------------------------------------------------------------------------------------
    # -- Admin and Auth --
    # --------------------------------------------------------------------------------------
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    # --------------------------------------------------------------------------------------
    # -- Third Party --
    # --------------------------------------------------------------------------------------
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("silk/", include("silk.urls", namespace="silk")),
]
