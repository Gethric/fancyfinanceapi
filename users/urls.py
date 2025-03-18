from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginView, ValidateTokenView, UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename="user")

urlpatterns = [
    path('', include(router.urls)),
    path("login/", LoginView.as_view(), name="login"),
    path("validate/", ValidateTokenView.as_view(), name='validate_token'),
]
