from apps.auths.serializers import LoginSocialSerializer, RegisterSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from social_django.utils import load_backend, load_strategy


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        return Response(status=status.HTTP_201_CREATED)


class LoginAPIView(TokenObtainPairView):
    ...


class RefreshTokenAPIView(TokenRefreshView):
    ...


class LoginSocialAPIView(generics.CreateAPIView):
    serializer_class = LoginSocialSerializer

    def post(self, request, *args, **kwargs):
        backend = load_backend(
            load_strategy(self.request), self.kwargs["backend"], redirect_uri=None
        )
        serializer = self.get_serializer(data=request.data, backend=backend)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
