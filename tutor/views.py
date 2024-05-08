from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here.

class TutorViewset(viewsets.ModelViewSet):
    queryset = models.Tutor.objects.all()
    serializer_class = serializers.TutorSerializer
