from django.urls import path
from .views import ApplicationCreateApiView,UserApplicationsApiView

urlpatterns = [
    path('apply/', ApplicationCreateApiView.as_view(), name='application-create'),
    path('user-applications/', UserApplicationsApiView.as_view(), name='user-applications'),
]
