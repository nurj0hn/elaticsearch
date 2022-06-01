from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .yasg import urlpatterns as swagger_urlpatterns
# from social_auth.views import FacebookLogin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('users.urls')),
    path('search/', include('search.urls')),
    # path('api/v1/users/', include('social_auth.urls')),
    # path('auth/', include('rest_framework_social_oauth2.urls')),
] + swagger_urlpatterns


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
