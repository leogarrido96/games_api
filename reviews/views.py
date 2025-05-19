from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.permissions import GlobalDefaultPermission
from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ReviewListCreateView(generics.ListCreateAPIView):
    permission_classes = (GlobalDefaultPermission, IsAuthenticatedOrReadOnly)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filterset_fields = ['game', 'user']
    search_fields = ['game__title', 'user__username']


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (GlobalDefaultPermission, IsAuthenticatedOrReadOnly)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
