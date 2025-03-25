from rest_framework import viewsets
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.permissions import IsAuthenticated

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user).order_by('-date')
