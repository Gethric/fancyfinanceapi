from django.db import models
from django.contrib.auth.models import User

class Currency(models.Model):
    name = models.CharField(max_length=50, unique=True)
    iso_code = models.CharField(max_length=3, unique=True)
    symbol = models.CharField(max_length=5, blank=True, null=True)
    decimal_precision = models.SmallIntegerField(default=2)
    numeric_code = models.SmallIntegerField(blank=True, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "common_currencies"

    def __str__(self):
        return f"{self.name} ({self.iso_code})"

class UserCurrency(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'currency'], name='unique_user_currency')
        ]

    def __str__(self):
        return f"{self.user.username} - {self.currency.name}"
    
class Pitch(models.Model):
    name = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "common_pitches"

    def __str__(self):
        return f"{self.name}"
    

class TransactionType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "common_categories"

    def __str__(self):
        return f"{self.name}"