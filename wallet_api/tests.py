from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTests(APITestCase):

    def test_create_user(self):
        url = reverse('user-list')  # rota para criar usuário via ViewSet
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpass123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email='testuser@example.com').exists())

    def test_login_with_jwt(self):
        # Criar usuário antes do login
        #User.objects.create_user(
        #    username='testuser',
        #    email='testuser@example.com',
        #    password='testpass123'
        #)
        self.user = User.objects.create_user(
            username='usuario1',
            email='usuario@example.com',
            password='senha123'
        )

        url = reverse('token_obtain_pair')  # esta é a url que aponta para EmailTokenObtainPairView
        data = {
            'email': 'testuser@example.com',
            'password': 'testpass123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        
        

