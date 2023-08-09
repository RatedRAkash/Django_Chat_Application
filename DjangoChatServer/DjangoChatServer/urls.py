"""
URL configuration for DjangoChatServer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registerApp.urls')),
    path('rooms/', include('chatApp.urls')),

    # API Path of chatApp
    path('api/', include('chatApp.api_urls')),

    # API Path of Authentication
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('productApp.api_urls')),

    # Registration Through API
    path('api/', include('registerApp.api_urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
