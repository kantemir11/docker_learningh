from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects_info.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger-ui/', SpectacularSwaggerView.as_view(), name='swagger-ui'),
]

urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language= False)
]