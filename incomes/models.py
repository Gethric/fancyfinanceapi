from django.db import models
from django.contrib.auth.models import User
from common.models import Pitch, Currency

class Income(models.Model):
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.CharField(max_length=50) 
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.ForeignKey(Pitch, on_delete=models.PROTECT, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.source} ({self.amount:.2f})"
