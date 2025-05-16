# core/views.py
from rest_framework import viewsets, permissions
from .models import Wallet, Transaction
from core.serializers import WalletSerializer, TransactionSerializer
from django.contrib.auth import get_user_model
from core.serializers import WalletSerializer, TransactionSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import EmailTokenObtainPairSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bem-vindo à API de Carteiras Digitais!</h1><p>Acesse /admin para gerenciar.</p>")


class EmailLoginView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer


User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [permissions.IsAuthenticated]

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    # core/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bem-vindo à API de Carteiras Digitais!</h1><p>Acesse /admin para gerenciar.</p>")

