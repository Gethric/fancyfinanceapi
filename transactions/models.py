from django.db import models
from django.contrib.auth.models import User
from common.models import Category, TransactionType
    
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.PROTECT)  # Income/Expense
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)  # Sub-category
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} on {self.date}"