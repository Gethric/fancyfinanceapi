from rest_framework import serializers
from .models import Transaction, TransactionType
from common.models import Category

class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionType
        fields = ['id', 'name']  # Only include essential fields

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class TransactionSerializer(serializers.ModelSerializer):
    transaction_type = TransactionTypeSerializer(read_only=True)  # Nest transaction type
    category = CategorySerializer(read_only=True)  # Nest category
    user = serializers.PrimaryKeyRelatedField(read_only=True)  # Auto-assign user

    class Meta:
        model = Transaction
        fields = ['id', 'user', 'transaction_type', 'category', 'amount', 'date', 'description']
        read_only_fields = ['id', 'user']
