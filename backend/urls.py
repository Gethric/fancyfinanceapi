from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/auth/", include("users.urls")),
    path('api/common/', include('common.urls')),
    path('api/', include('expenses.urls')),
    path('api/', include('incomes.urls')),
]
