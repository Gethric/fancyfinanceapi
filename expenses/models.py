from django.db import models
from django.contrib.auth.models import User
from common.models import Currencies, Pitches

class Expenses(models.Model):

    CATEGORY_CHOICES = [
        ('household', 'Household'),
        ('personal', 'Personal'),
        ('savings', 'Savings'),
        ('streaming', 'Streaming'),
        ('misc', 'Misc'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expenses")
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.ForeignKey(Pitches, on_delete=models.SET_NULL, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='household')
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    currency = models.ForeignKey(Currencies, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.description} ({self.amount})"