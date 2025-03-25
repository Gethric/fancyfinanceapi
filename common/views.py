from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Currency, UserCurrency, Pitch, Category
from .serializers import CurrencySerializer, UserCurrencySerializer, PitchSerializer, CategorySerializer

class CurrenciesListView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer  # No authentication required

class UserCurrenciesListView(generics.ListAPIView):
    serializer_class = UserCurrencySerializer
    permission_classes = [IsAuthenticated]  # Only logged-in users can access

    def get_queryset(self):
        return UserCurrency.objects.filter(user=self.request.user)

class PitchesListView(generics.ListAPIView):
    queryset = Pitch.objects.all()
    serializer_class = PitchSerializer  # No authentication required

class CategoriesListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer  # No authentication required
