from django.contrib import admin

from genres.models import Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """
    Admin view for the Genre model.
    """
    list_display = ('id', 'name', 'description', 'slug', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'slug')
