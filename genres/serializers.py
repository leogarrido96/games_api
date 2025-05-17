from rest_framework import serializers

from .models import Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
        extra_kwargs = {
            'name': {'required': True},
            'description': {'required': True},
            'slug': {'required': True},
        }
