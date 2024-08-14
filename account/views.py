from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from .backend import EmailOrUsernameBackend as Backend
from .models import User
from .serializers import UserSerializer


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = Backend.authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            user_data = UserSerializer(user).data

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user_data
            })
        else:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserUpdateView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)


class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)
        except TokenError:
            return Response({'detail': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
