from django.db import models
from django.contrib.auth.models import User

class Incomes(models.Model):

    FREQUENCY_CHOICES = [
    ('weekly', 'Weekly'),
    ('bi-weekly', 'Bi-weekly'),
    ('monthly', 'Monthly'),
    ]
        
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="incomes")
    source = models.CharField(max_length=50) 
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES, default='monthly')
    description = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    currency = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.source} ({self.amount:.2f})"
