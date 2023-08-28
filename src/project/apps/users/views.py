from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .serializers import MePasswordSerializer, MeSerializer


class MeAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = MeSerializer

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return Response(status=status.HTTP_202_ACCEPTED)


class MePasswordAPIView(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = MePasswordSerializer

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        return Response(status=status.HTTP_202_ACCEPTED)
