# core/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, WalletViewSet, TransactionViewSet, home

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from rest_framework import routers
from .views import home, WalletViewSet, TransactionViewSet, UserViewSet

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
]


