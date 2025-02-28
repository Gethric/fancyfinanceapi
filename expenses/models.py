from django.db import models
from django.contrib.auth.models import User

class Expenses(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('bi-weekly', 'Bi-weekly'),
        ('monthly', 'Monthly'),
        ('annual', 'Annual'),
    ]

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
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES, default='monthly')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='household')
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.description} ({self.amount})"