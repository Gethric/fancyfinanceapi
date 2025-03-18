from django.shortcuts import render
from rest_framework import generics
from .models import Incomes
from .serializers import IncomeSerializer

class IncomeListCreateView(generics.ListCreateAPIView):
    
    serializer_class = IncomeSerializer

    def get_queryset(self):

        return Incomes.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):

        serializer.save(user=self.request.user)

class IncomeDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = IncomeSerializer

    def get_queryset(self):

        return Incomes.objects.filter(user=self.request.user)
