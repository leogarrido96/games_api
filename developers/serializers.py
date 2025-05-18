from rest_framework import serializers

from developers.models import Developer


class DeveloperSerializer(serializers.ModelSerializer):
    """
    Serializer for the Developer model.
    """
    class Meta:
        model = Developer
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
        extra_kwargs = {
            'name': {'required': True},
            'description': {'required': False},
            'website': {'required': False},
            'founded_year': {'required': False},
        }
