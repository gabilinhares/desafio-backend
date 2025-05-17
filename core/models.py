#core/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Wallet(models.Model):
    owner = models.ForeignKey(User, related_name='wallets', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.owner.email}) - Saldo: {self.balance}'

class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, related_name='transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    CREDIT = 'CR'
    DEBIT = 'DB'
    TRANSACTION_TYPE_CHOICES = [
        (CREDIT, 'Crédito'),
        (DEBIT, 'Débito'),
    ]
    transaction_type = models.CharField(max_length=2, choices=TRANSACTION_TYPE_CHOICES)

    def __str__(self):
        return f'{self.get_transaction_type_display()} {self.amount} em {self.created_at.strftime("%Y-%m-%d %H:%M:%S")}'
