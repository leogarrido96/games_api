from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.permissions import GlobalDefaultPermission
from developers.models import Developer
from developers.serializers import DeveloperSerializer


class DeveloperListView(generics.ListCreateAPIView):
    """
    API view to retrieve and create developers.
    """
    permission_classes = (GlobalDefaultPermission, IsAuthenticatedOrReadOnly)
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer


class DeveloperRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete a developer.
    """
    permission_classes = (GlobalDefaultPermission, IsAuthenticatedOrReadOnly)
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
