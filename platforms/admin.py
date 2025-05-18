from django.contrib import admin

from platforms.models import Platform


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    """
    Admin view for the Platform model.
    """
    list_display = ('id', 'name', 'manufacturer', 'release_year', 'description', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'manufacturer', 'release_year')
    ordering = ('id',)
