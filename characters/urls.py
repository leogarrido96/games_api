from django.urls import path

from characters.views import CharacterListView, CharacterRetrieveUpdateDestroyView


urlpatterns = [
    path('characters/', CharacterListView.as_view(), name='character-create-list'),
    path('characters/<int:pk>/', CharacterRetrieveUpdateDestroyView.as_view(), name='character-detail'),
]
