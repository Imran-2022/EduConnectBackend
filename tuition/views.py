from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from . import models
from . import serializers
from rest_framework.permissions import AllowAny

class TuitionViewSet(viewsets.ModelViewSet):
    queryset = models.TuitionPost.objects.all()
    serializer_class = serializers.TuitionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['class_of_student']
    permission_classes = [AllowAny]  # Allow access without authentication
