from django.db import models
from django.contrib.auth.models import User
from common.models import Currency, Pitch, Category

class Expense(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.ForeignKey(Pitch, on_delete=models.PROTECT, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    date_created = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.description} ({self.amount})"