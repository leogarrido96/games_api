from django.db.models import Avg
from rest_framework import generics, response, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.permissions import GlobalDefaultPermission
from games.models import Game
from games.serializers import GameSerializer
from reviews.models import Review


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


class GameStatsViews(generics.ListAPIView):
    """
    View to get game statistics.
    """
    permission_classes = (GlobalDefaultPermission, IsAuthenticatedOrReadOnly)
    queryset = Game.objects.all()

    def get(self, request):
        total_games = self.queryset.count()
        total_reviews = Review.objects.count()
        total_users = Review.objects.values('user').distinct().count()
        total_reviews_per_game = Review.objects.values('game').distinct().count()
        average_rating = Review.objects.aggregate(Avg('rating'))['rating__avg']

        return response.Response(
            data={
                'total_games': total_games,
                'total_reviews': total_reviews,
                'total_users': total_users,
                'total_reviews_per_game': total_reviews_per_game,
                'average_rating': round(average_rating, 2) if average_rating else None,
            },
            status=status.HTTP_200_OK)
