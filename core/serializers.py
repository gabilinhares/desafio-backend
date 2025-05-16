# core/serializers.py
from rest_framework import serializers
from .models import Wallet, Transaction
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'  # Define o campo para login por email

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token

    def validate(self, attrs):
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
