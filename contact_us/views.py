from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class ContactusViewset(viewsets.ModelViewSet):
    queryset = models.ContactUs.objects.all()
    serializer_class = serializers.ContactUsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # print("print:",serializer)  
        if serializer.is_valid():
            serializer.save()  # Save the new TuitionPost
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Log the errors to understand what's going wrong
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)