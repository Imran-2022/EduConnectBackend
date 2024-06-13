from django.urls import path
from .views import ApplicationCreateApiView

urlpatterns = [
    path('apply/', ApplicationCreateApiView.as_view(), name='application-create'),
]
