from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from app import views
from intranet_visian import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/authenticate', obtain_auth_token),
    path('api/persons', views.persons),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
