from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.permissions import GlobalDefaultPermission
from platforms.models import Platform
from platforms.serializers import PlatformSerializer


class PlatformListView(generics.ListCreateAPIView):
    """
    API view to retrieve and create platforms.
    """
    permission_classes = (GlobalDefaultPermission, IsAuthenticatedOrReadOnly)
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer


class PlatformRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete a platform.
    """
    permission_classes = (GlobalDefaultPermission, IsAuthenticatedOrReadOnly)
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
