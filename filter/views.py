from rest_framework import viewsets
from . import models
from . import serializers

class FilterViewSet(viewsets.ModelViewSet):
    queryset = models.Filter.objects.all()
    serializer_class = serializers.FilterSerializer
