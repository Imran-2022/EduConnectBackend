from rest_framework import serializers
from . import models

class TuitionSerializer(serializers.ModelSerializer):
    class_of_student=serializers.StringRelatedField(many=False)
    class Meta:
        model = models.TuitionPost
        fields = '__all__'
