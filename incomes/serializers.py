from rest_framework import serializers
from common.models import Pitch, Currency
from common.serializers import CurrencySerializer, PitchSerializer
from .models import Income

class IncomeSerializer(serializers.ModelSerializer):
    frequency_detail = PitchSerializer(source='frequency', read_only=True)
    currency_detail = CurrencySerializer(source='currency', read_only=True)

    frequency = serializers.PrimaryKeyRelatedField(
        queryset=Pitch.objects.all(), write_only=True)
    currency = serializers.PrimaryKeyRelatedField(
        queryset=Currency.objects.all(), write_only=True)


    class Meta:
        model = Income
        fields = ['id', 'user', 'source', 'amount', 'frequency', 'description', 'date_created', 'notes', 'currency', 'frequency_detail', 'currency_detail']
        read_only_fields = ['id', 'user', 'date_created']
        