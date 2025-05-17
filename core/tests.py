from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from core.models import Wallet, Transaction

User = get_user_model()

class UserTests(APITestCase):
    def test_user_registration(self):
        url = reverse('user-list')  # Assumindo rota do ViewSet UserViewSet
        data = {
            'email': 'testuser@example.com',
            'password': 'strongpassword123',
            'first_name': 'Test',
            'last_name': 'User'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email='testuser@example.com').exists())

    def test_token_obtain(self):
        user = User.objects.create_user(email='tokenuser@example.com', password='pass12345')
        url = reverse('token_obtain_pair')
        response = self.client.post(url, {'email': user.email, 'password': 'pass12345'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

class WalletTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='walletuser@example.com', password='walletpass')
        self.client.force_authenticate(user=self.user)

    def test_create_wallet(self):
        url = reverse('wallet-list')
        data = {
            'name': 'Minha Carteira',
            'balance': 1000
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user'], self.user.id)
        self.assertEqual(response.data['balance'], 1000)

    def test_list_wallets(self):
        Wallet.objects.create(user=self.user, name='Carteira 1', balance=500)
        Wallet.objects.create(user=self.user, name='Carteira 2', balance=200)
        url = reverse('wallet-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

class TransactionTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='usuario1',
            email='usuario@example.com',
            password='senha123'
        )
        self.other_user = User.objects.create_user(email='other@example.com', password='otherpass')
        self.wallet_sender = Wallet.objects.create(user=self.user, name='Carteira Sender', balance=1000)
        self.wallet_receiver = Wallet.objects.create(user=self.other_user, name='Carteira Receiver', balance=100)

        self.client.force_authenticate(user=self.user)

    def test_create_transaction_success(self):
        url = reverse('transaction-list')
        data = {
            'sender_wallet': self.wallet_sender.id,
            'receiver_wallet': self.wallet_receiver.id,
            'amount': 200
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.wallet_sender.refresh_from_db()
        self.wallet_receiver.refresh_from_db()
        self.assertEqual(self.wallet_sender.balance, 800)
        self.assertEqual(self.wallet_receiver.balance, 300)

    def test_create_transaction_insufficient_balance(self):
        url = reverse('transaction-list')
        data = {
            'sender_wallet': self.wallet_sender.id,
            'receiver_wallet': self.wallet_receiver.id,
            'amount': 2000  # maior que saldo
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_transaction_not_owner(self):
        self.client.force_authenticate(user=self.other_user)
        url = reverse('transaction-list')
        data = {
            'sender_wallet': self.wallet_sender.id,
            'receiver_wallet': self.wallet_receiver.id,
            'amount': 100
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
       

