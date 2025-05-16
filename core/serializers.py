from rest_framework import serializers
from .models import Wallet, Transaction
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class WalletSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Wallet.
    Serializa todos os campos da carteira digital.
    """
    class Meta:
        model = Wallet
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Transaction.
    Serializa todos os campos da transação financeira.
    """
    class Meta:
        model = Transaction
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo User.
    Expõe apenas os campos públicos básicos do usuário.
    """
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Serializer customizado para obtenção de tokens JWT usando email e senha.
    Sobrescreve o campo username para usar email como identificador.
    Adiciona o email no payload do token.
    """
    username_field = 'email'  # Define o campo para login por email

    @classmethod
    def get_token(cls, user):
        """
        Inclui o email do usuário no payload do token JWT.
        """
        token = super().get_token(user)
        token['email'] = user.email
        return token

    def validate(self, attrs):
        """
        Valida o email e senha enviados.
        Autentica o usuário e retorna os tokens.
        """
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            if not user:
                raise serializers.ValidationError(_('Usuário ou senha inválidos'), code='authorization')
        else:
            raise serializers.ValidationError(_('Preencha email e senha'), code='authorization')

        data = super().validate({
            self.username_field: email,
            'password': password
        })

        return data
