from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserSerializer
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterUserView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        try:
            validate_password(request.data['password'])
            user = User.objects.create_user(
                username=request.data['username'],
                email=request.data.get('email'),
                password=request.data['password']
            )
            return Response({'message': 'User registered'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]