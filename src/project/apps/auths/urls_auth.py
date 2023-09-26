from django.conf import settings
from django.http import JsonResponse
from django.urls import path
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from social_django import views
from social_django.urls import extra
from social_django.utils import psa
from social_django.views import NAMESPACE

app_name = "social"


# Views
@never_cache
@csrf_exempt
@psa(f"{NAMESPACE}:complete")
def complete(request, backend, *args, **kwargs):
    """default social will redirect to profile page, but we only want access_token for logged_in"""
    response = request.backend.request_access_token(
        request.backend.ACCESS_TOKEN_URL,
        data=request.backend.auth_complete_params(),
        headers=request.backend.auth_headers(),
        method=request.backend.ACCESS_TOKEN_METHOD,
    )
    return JsonResponse(response)


# URL
urlpatterns = []

if settings.DEBUG:
    urlpatterns = [
        path(f"login/<str:backend>{extra}", views.auth, name="begin"),
        path(f"complete/<str:backend>{extra}", complete, name="complete"),
        # disconnection
        path(f"disconnect/<str:backend>{extra}", views.disconnect, name="disconnect"),
        path(
            f"disconnect/<str:backend>/<int:association_id>{extra}",
            views.disconnect,
            name="disconnect_individual",
        ),
    ]
