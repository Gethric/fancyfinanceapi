from django.db import models
from django.contrib.auth.models import User

class Currencies(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    iso_code = models.CharField(max_length=3, unique=True)
    symbol = models.CharField(max_length=10, blank=True, null=True)
    decimal_precision = models.SmallIntegerField()
    numeric_code = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "common_currencies"

    def __str__(self):
        return f"{self.name} ({self.iso_code})"

class UserCurrencies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currencies, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "currency")  # Prevents duplicate entries

    def __str__(self):
        return f"{self.user.username} - {self.currency.name}"
    
class Pitches(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "common_pitches"

    def __str__(self):
        return f"{self.name}"
    
class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "common_categories"

    def __str__(self):
        return f"{self.name}"