from rest_framework import serializers
from .models import Expense
from common.models import Pitch, Category, Currency
from common.serializers import CurrencySerializer, PitchSerializer, CategorySerializer

class ExpenseSerializer(serializers.ModelSerializer):
    frequency_detail = PitchSerializer(source='frequency', read_only=True)
    category_detail = CategorySerializer(source='category', read_only=True)
    currency_detail = CurrencySerializer(source='currency', read_only=True)

    frequency = serializers.PrimaryKeyRelatedField(
        queryset=Pitch.objects.all(), write_only=True)
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True)
    currency = serializers.PrimaryKeyRelatedField(
        queryset=Currency.objects.all(), write_only=True)

    class Meta:
        model = Expense
        fields = ['id', 'user', 'description', 'amount', 'date_created', 'notes', 'frequency', 'category', 'currency', 'frequency_detail', 'category_detail', 'currency_detail']
        read_only_fields = ['id', 'user', 'date_created']

    