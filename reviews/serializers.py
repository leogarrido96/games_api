from rest_framework import serializers

from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'game': {'required': True},
            'user': {'required': True},
            'rating': {'required': True},
            'review_text': {'required': False},
        }
