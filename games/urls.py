from django.urls import path

from games.views import GameListView, GameRetrieveUpdateDestroyView


urlpatterns = [
    path('games/', GameListView.as_view(), name='game-create-list'),
    path('games/<int:pk>/', GameRetrieveUpdateDestroyView.as_view(), name='game-detail'),
]
