from rest_framework import serializers
from . import models

class TuitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TuitionPost
        fields = '__all__'
