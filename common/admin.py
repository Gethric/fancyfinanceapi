from django.contrib import admin
from .models import Currency, UserCurrency, Pitch, Category, TransactionType

admin.site.register(Currency)
admin.site.register(UserCurrency)
admin.site.register(Pitch)
admin.site.register(Category)
admin.site.register(TransactionType)
