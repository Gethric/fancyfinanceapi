from rest_framework import generics, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from .serializers import UserSerializer, LoginSerializer


User = get_user_model()

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [IsAuthenticated()]

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    

class ValidateTokenView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]  # requires a valid JWT

    def post(self, request):
        # If we got here, the JWT is valid and the user is authenticated.
        return Response({"detail": "Token is valid"}, status=200)
