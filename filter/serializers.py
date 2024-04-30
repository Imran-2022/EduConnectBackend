from rest_framework import serializers
from . import models

class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Filter
        fields = '__all__'
