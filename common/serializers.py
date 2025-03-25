from rest_framework import serializers
from .models import Currency, UserCurrency, Pitch, Category

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'

class UserCurrencySerializer(serializers.ModelSerializer):
    currency = CurrencySerializer(read_only=True)

    class Meta:
        model = UserCurrency
        fields = ['id', 'user', 'currency']

class PitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pitch
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'