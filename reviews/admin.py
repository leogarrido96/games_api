from django.contrib import admin

from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'game', 'user', 'rating', 'review_text', 'created_at', 'updated_at')
    list_filter = ('game', 'user', 'rating', 'created_at', 'updated_at')
    search_fields = ('game__title', 'user__username')
    ordering = ('id',)
