from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.permissions import AllowAny


class FilterViewSet(viewsets.ModelViewSet):
    queryset = models.Filter.objects.all()
    serializer_class = serializers.FilterSerializer
    permission_classes = [AllowAny]  # Allow access without authentication

