from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import TuitionPost, Application
from .serializers import ApplicationSerializer

class ApplicationCreateApiView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ApplicationSerializer

    def post(self, request):
        try:
            user = request.user
            tuition_post_id = request.data.get('tuition_post')

            # Check if the user has already applied to this tuition post
            existing_application = Application.objects.filter(user=user, tuition_post_id=tuition_post_id).exists()
            if existing_application:
                return Response({'error': 'You have already applied to this tuition post'}, status=status.HTTP_400_BAD_REQUEST)

            tuition_post = get_object_or_404(TuitionPost, id=tuition_post_id)

            data = {
                'user': user.id,
                'tuition_post': tuition_post.id,
            }

            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserApplicationsApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        applications = Application.objects.filter(user=user)
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    