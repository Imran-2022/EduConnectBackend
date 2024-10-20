from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from . import models
from . import serializers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

class TuitionViewSet(viewsets.ModelViewSet):
    queryset = models.TuitionPost.objects.all()
    serializer_class = serializers.TuitionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['class_of_student']
    permission_classes = [AllowAny]  # Allow access without authentication

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # print("print:",serializer)  
        if serializer.is_valid():
            serializer.save()  # Save the new TuitionPost
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Log the errors to understand what's going wrong
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)