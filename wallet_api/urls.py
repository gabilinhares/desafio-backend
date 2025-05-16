from django.contrib import admin
from django.urls import path, include
from core.views import EmailLoginView
from rest_framework_simplejwt.views import TokenRefreshView

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),  # Inclui todas as rotas de API, JWT e home
    path('', include('core.urls')),  # inclui core.urls com home e API
    path('api/token/', EmailLoginView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
