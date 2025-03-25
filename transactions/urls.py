from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet

router = DefaultRouter()
router.register(r'', TransactionViewSet, basename='transaction')  # Registers transactions API

urlpatterns = [
    path('', include(router.urls)),  # Includes all CRUD operations for transactions
]
