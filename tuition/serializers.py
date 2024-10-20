from rest_framework import serializers
from . import models

class TuitionSerializer(serializers.ModelSerializer):
    class_of_student = serializers.PrimaryKeyRelatedField(queryset=models.Filter.objects.all())
    # class_of_student = serializers.StringRelatedField(many=False)

    class Meta:
        model = models.TuitionPost
        fields = '__all__'

    def create(self, validated_data):

        # Ensure that 'class_of_student' is already the correct instance
        validated_data['active'] = 'pending'  # Ensure this is set

        return super().create(validated_data)
