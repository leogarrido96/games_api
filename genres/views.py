from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.permissions import GlobalDefaultPermission
from genres.models import Genre
from genres.serializers import GenreSerializer


class GenreListView(generics.ListCreateAPIView):
    """
    API view to retrieve and create genres.
    """
    permission_classes = (GlobalDefaultPermission, IsAuthenticatedOrReadOnly)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete a genre.
    """
    permission_classes = (GlobalDefaultPermission, IsAuthenticatedOrReadOnly)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
