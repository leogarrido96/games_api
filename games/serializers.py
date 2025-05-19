from django.db.models import Avg
from rest_framework import serializers

from games.models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
        extra_kwargs = {
            'title': {'required': True},
            'description': {'required': False},
            'release_year': {'required': False},
            'genre': {'required': True},
            'developer': {'required': False},
            'character': {'required': False},
            'platform': {'required': True}
        }

        def get_rate_review(self, obj):
            """
            Get the average rating of the game.
            """
            rate = obj.reviews.aggregate(Avg('rating'))['rating__avg']

            if rate:
                return round(rate, 2)
            return None

        def validate_title(self, value):
            """
            Validate the title of the game.
            """
            if not value:
                raise serializers.ValidationError("Title is required.")
            return value

        def get_count_reviews(self, obj):
            """
            Get the count of reviews for the game.
            """
            count = obj.reviews.count()
            if count:
                return count
            return 0
