# core/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import home, WalletViewSet, TransactionViewSet, UserViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import permissions
from rest_framework.response import Response
from django.urls import path, include, re_path


schema_view = get_schema_view(
   openapi.Info(
      title="API Carteiras Digitais",
      default_version='v1',
      description="Documentação da API para gerenciamento de carteiras digitais",
      contact=openapi.Contact(email="seu-email@exemplo.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'wallets', WalletViewSet)
router.register(r'transactions', TransactionViewSet)

@api_view(['GET'])
@permission_classes([AllowAny])
def home(request):
    return Response({"message": "Bem-vindo à API Wallet!"})

urlpatterns = [
    path('', home, name='home'),
    path('', include(router.urls)),  # Removido o "api/" daqui

    # JWT Token direto
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


