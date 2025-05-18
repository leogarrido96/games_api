from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.permissions import GlobalDefaultPermission
from games.models import Game
from games.serializers import GameSerializer


class GameListView(generics.ListCreateAPIView):
    """
    View to list and create games.
    """
    permission_classes = (GlobalDefaultPermission, IsAuthenticatedOrReadOnly)
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, and destroy a game.
    """
    permission_classes = (GlobalDefaultPermission, IsAuthenticatedOrReadOnly)
    queryset = Game.objects.all()
    serializer_class = GameSerializer
