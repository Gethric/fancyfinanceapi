from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("api/auth/", include("users.urls")),
    path('admin/', admin.site.urls),
    path('api/', include('expenses.urls')),
    path('api/', include('incomes.urls')),
]
