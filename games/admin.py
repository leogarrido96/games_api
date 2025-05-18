from django.contrib import admin

from games.models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    """
    Admin view from Game Model
    """
    list_display = ('id', 'title', 'description', 'release_year', 'genre', 'developer', 'character', 'platform', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'release_year')
    search_fields = ('title', 'release_year', 'genre__name', 'developer__name', 'platform__name')
    ordering = ('id', )
