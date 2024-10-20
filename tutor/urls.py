from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register('list', views.TutorViewset)
urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.UserRegistrationApiView.as_view(), name='register'),
    path('login/', views.UserLoginApiView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('activate/<uid64>/<token>/', views.activate, name = 'activate'),
    path('user-tutor-profile/', views.UserTutorProfileApiView.as_view(), name='user-tutor-profile'),
     path('user-tutor-profile/<int:id>/', views.UserTutorProfileApiView.as_view(), name='delete-tutor-profile'),  # New path for deleting by ID
]