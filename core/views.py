# core/views.py
from rest_framework import viewsets, permissions
from .models import Wallet, Transaction
from core.serializers import WalletSerializer, TransactionSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import EmailTokenObtainPairSerializer
from django.http import HttpResponse

def home(request):
    """
    Endpoint simples para a página inicial da API.
    Retorna uma mensagem HTML de boas-vindas.
    """
    return HttpResponse("<h1>Bem-vindo à API de Carteiras Digitais!</h1><p>Acesse /admin para gerenciar.</p>")

class EmailLoginView(TokenObtainPairView):
    """
    Endpoint para autenticação via email e senha.
    Retorna tokens JWT (access e refresh).
    """
    serializer_class = EmailTokenObtainPairSerializer

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite CRUD de usuários.
    Apenas usuários autenticados podem acessar.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class WalletViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gerenciamento de carteiras digitais.
    Permite criar, listar, atualizar e deletar carteiras.
    Acesso restrito a usuários autenticados.
    """
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [permissions.IsAuthenticated]

class TransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gerenciar transações financeiras entre carteiras.
    Permite criar, listar, atualizar e deletar transações.
    Acesso restrito a usuários autenticados.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
