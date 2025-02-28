from django.shortcuts import render
from rest_framework import generics
from .models import Expenses
from .serializers import ExpenseSerializer

# List and create expenses
class ExpenseListCreateView(generics.ListCreateAPIView):

    serializer_class = ExpenseSerializer

    def get_queryset(self):

        return Expenses.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):

        serializer.save(user=self.request.user)

# Retrieve, update, or delete a specific expense
class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ExpenseSerializer

    def get_queryset(self):

        return Expenses.objects.filter(user=self.request.user)

