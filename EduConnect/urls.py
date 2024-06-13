from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from . views import UserViewSet
router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('contact_us/',include('contact_us.urls')),
    path('filter/',include('filter.urls')),
    path('tuition_post/',include('tuition.urls')),
    path('tutor/',include('tutor.urls')),
    path('application/', include('application.urls')),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)