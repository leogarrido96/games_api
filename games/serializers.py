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
