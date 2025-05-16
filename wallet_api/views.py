from django.http import HttpResponse
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Wallet, Transaction
from .serializers import WalletSerializer, TransactionSerializer, UserSerializer
from .serializers import EmailTokenObtainPairSerializer  # seu serializer custom

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciamento dos usuários.
    - Ação 'create' é aberta para registro.
    - Outras ações exigem autenticação.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':  # registro aberto
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

class WalletViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciamento das carteiras digitais.
    - Permite somente o acesso e manipulação das carteiras do usuário autenticado.
    """
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TransactionViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciamento das transações financeiras entre carteiras.
    - Permite apenas transações onde o usuário é remetente ou destinatário.
    - Valida saldo antes de executar a transação.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(
            sender_wallet__user=self.request.user
        ) | self.queryset.filter(
            receiver_wallet__user=self.request.user
        )

    def perform_create(self, serializer):
        sender_wallet = serializer.validated_data['sender_wallet']
        receiver_wallet = serializer.validated_data['receiver_wallet']
        amount = serializer.validated_data['amount']

        if sender_wallet.user != self.request.user:
            raise PermissionDenied("Você não pode enviar de uma carteira que não é sua.")

        if sender_wallet.balance < amount:
            raise ValidationError("Saldo insuficiente para realizar a transação.")

        sender_wallet.balance -= amount
        receiver_wallet.balance += amount

        sender_wallet.save()
        receiver_wallet.save()

        serializer.save()

def index(request):
    """
    Página inicial simples para validar que a API está rodando.
    """
    return HttpResponse("API de Carteira funcionando!")

class EmailTokenObtainPairView(TokenObtainPairView):
    """
    View para autenticação via JWT usando email e senha.
    """
    serializer_class = EmailTokenObtainPairSerializer

class EmailLoginView(TokenObtainPairView):
    """
    View alternativa para autenticação via JWT com email.
    """
    serializer_class = EmailTokenObtainPairSerializer
