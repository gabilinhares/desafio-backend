from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, WalletViewSet, TransactionViewSet, home
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'wallets', WalletViewSet)
router.register(r'transactions', TransactionViewSet)

@api_view(['GET'])
@permission_classes([AllowAny])
def home(request):
    return Response({"message": "Bem-vindo à API Wallet!"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # rotas automáticas: /api/users, /api/wallets, /api/transactions
    path('', home, name='home'),  # rota raiz da aplicação, fora do /api para evitar conflito
]
