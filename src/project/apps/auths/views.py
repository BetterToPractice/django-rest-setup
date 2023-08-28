from apps.auths.serializers import RegisterSerializer
from rest_framework import generics, status
from rest_framework.response import Response


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        return Response(status=status.HTTP_201_CREATED)
