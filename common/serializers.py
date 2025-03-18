from rest_framework import serializers
from .models import Currencies, UserCurrencies, Pitches, Categories

class CurrenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currencies
        fields = '__all__'

class UserCurrenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCurrencies
        fields = '__all__'

class PitchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pitches
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'