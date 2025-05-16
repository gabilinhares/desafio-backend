from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    # Não precisa sobrescrever username_field
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            if not user:
                raise serializers.ValidationError(_('Usuário ou senha inválidos'), code='authorization')
        else:
            raise serializers.ValidationError(_('Preencha email e senha'), code='authorization')

        # Agora chama o super passando username (que é user.username), porque SimpleJWT espera isso
        data = super().validate({
            'username': user.username,
            'password': password
        })

        return data
