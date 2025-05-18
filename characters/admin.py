from django.contrib import admin

from characters.models import Character


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    """
    Admin view for the Character model.
    """
    list_display = ('id', 'name', 'game', 'role', 'is_playable', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'game__title', 'role', 'is_playable')
    search_fields = ('name', 'game__title')
    ordering = ('id',)
