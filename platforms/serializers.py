from rest_framework import serializers

from .models import Platform


class PlatformSerializer(serializers.ModelSerializer):
    """
    Serializer for the Platform model.
    """
    class Meta:
        model = Platform
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
        extra_kwargs = {
            'name': {'required': True},
            'manufacturer': {'required': False},
            'release_year': {'required': False},
            'description': {'required': False},

        }
