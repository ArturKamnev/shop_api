from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import AuthCode
from .serializers import UserRegistrationSerializer, UserAuthentificateSerializer, AuthCodeSerializer
from django.contrib.auth import authenticate
import random
# Create your views here.

@api_view(http_method_names=['POST'])
def authorization_api_view(request):
    serializer = AuthCodeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = request.data.get('user')
    user.is_active = True
    return Response(status=status.HTTP_200_OK, data={"message": "Доброе пожаловать"})

@api_view(http_method_names=['POST'])
def authentication_api_view(request):
    serializer = UserAuthentificateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            return Response(status=status.HTTP_202_ACCEPTED, data={"message": "Добро пожаловать"})
        else:
            return Response(status=status.HTTP_200_OK, data={"message": "Добро пожаловать, но чтобы активировать аккаунт пожалуйста активируйте ваш код"})

@api_view(http_method_names=['POST'])
def registration_api_view(request):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = request.data.get('username')
    password = request.data.get('password')
    user = User.objects.create_user(
        username=username,
        password=password,
        is_active=False
    )
    auth_code = AuthCode.objects.create(
        code=random.randint(100000, 999999),
        user=user
    )
    return Response(status=status.HTTP_201_CREATED, data={"your_auth_code": auth_code.code})