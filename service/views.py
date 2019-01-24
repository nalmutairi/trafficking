from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView , RetrieveAPIView, ListAPIView
from .serializers import UserCreateSerializer, UserLoginSerializer, UserDataSerializer, UserListSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        my_data = request.data
        serializer = UserLoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)


class UsersListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAdminUser]

class UserDetailsAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDataSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'user_id'
    permission_classes = [IsAuthenticated ,IsAdminUser]