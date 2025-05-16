# Transaction # transactions/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.TransactionListCreateView.as_view(), name='transaction-list-create'),
]
