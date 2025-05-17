from django.contrib import admin

from developers.models import Developer


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    """
    Admin view for the Developer model.
    """
    list_display = ('id', 'name', 'founded_year', 'country', 'website', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'founded_year', 'country')
    search_fields = ('name', 'founded_year', 'country')
    ordering = ('id',)
