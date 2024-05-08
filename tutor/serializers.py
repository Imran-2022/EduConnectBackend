from rest_framework import serializers
from . import models

class TutorSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(many=False)
    
    class Meta:
        model = models.Tutor
        fields='__all__'