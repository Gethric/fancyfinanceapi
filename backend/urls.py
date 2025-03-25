from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/auth/", include("users.urls")),
    path('api/common/', include('common.urls')),
    path('api/expenses/', include('expenses.urls')),
    path('api/incomes/', include('incomes.urls')),
    path('api/transactions/', include('transactions.urls')),
]
