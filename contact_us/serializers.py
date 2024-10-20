from rest_framework import serializers
from . import models
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUs
        fields='__all__'
        
        
    def create(self, validated_data):
        return super().create(validated_data)
