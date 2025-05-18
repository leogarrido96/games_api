from django.db import models


from genres.models import Genre
from characters.models import Character
from developers.models import Developer
from platforms.models import Platform


class Game(models.Model):
    """
    Model representing a game.
    """
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    release_year = models.IntegerField(null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='games')
    developer = models.ForeignKey(Developer, on_delete=models.SET_NULL, related_name='games', null=True, blank=True)
    character = models.ForeignKey(Character, on_delete=models.SET_NULL, related_name='games', null=True, blank=True)
    platform = models.ForeignKey(Platform, on_delete=models.PROTECT, related_name='games')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
