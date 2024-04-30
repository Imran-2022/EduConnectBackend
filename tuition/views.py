from rest_framework import viewsets
from . import models
from . import serializers

class TuitionViewSet(viewsets.ModelViewSet):
    queryset = models.TuitionPost.objects.all()
    serializer_class = serializers.TuitionSerializer
