from rest_framework import serializers

from characters.models import Character


class CharacterSerializer(serializers.ModelSerializer):
    """
    Serializer for the Character model.
    """
    class Meta:
        model = Character
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
        extra_kwargs = {
            'name': {'required': True},
            'description': {'required': False},
            'game': {'required': True},
            'role': {'required': True},
            'is_playable': {'required': False},
            'image_url': {'required': False},
        }
