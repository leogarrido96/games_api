from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.permissions import GlobalDefaultPermission
from characters.models import Character
from characters.serializers import CharacterSerializer


class CharacterListView(generics.ListCreateAPIView):
    """
    API view to create and retrieve from characters
    """

    permission_classes = (GlobalDefaultPermission, IsAuthenticatedOrReadOnly)
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class CharacterRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete a character.
    """

    permission_classes = (GlobalDefaultPermission, IsAuthenticatedOrReadOnly)
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
