from rest_framework import generics
from .models import Currencies, UserCurrencies, Pitches, Categories
from .serializers import CurrenciesSerializer, UserCurrenciesSerializer, PitchesSerializer, CategoriesSerializer

class CurrenciesListView(generics.ListAPIView):
    queryset = Currencies.objects.all()
    serializer_class = CurrenciesSerializer

class UserCurrenciesListView(generics.ListAPIView):
    serializer_class = UserCurrenciesSerializer
    def get_queryset(self):
        return UserCurrencies.objects.filter(user=self.request.user)

class PitchesListView(generics.ListAPIView):
    queryset = Pitches.objects.all()
    serializer_class = PitchesSerializer

class CategoriesListView(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer