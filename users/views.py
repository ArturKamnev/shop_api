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
from rest_framework.views import APIView
# Create your views here.

class RegistrationApiView(APIView):
    def post(self, request):
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

class ConfirmApiView(APIView):
    def post(self, request):
        serializer = AuthCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        auth_code = serializer.validated_data.get('auth_code') # type: ignore
        user = auth_code.user # type: ignore

        user.is_active = True
        user.save(update_fields=['is_active'])

        auth_code.delete() # type: ignore

        return Response(
            {"message": "Аккаунт успешно подтвержден"},
            status=status.HTTP_200_OK
        )

class AuthenticationApiView(APIView):
    def post(self, request):
        serializer = UserAuthentificateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                try:
                    token = Token.objects.get(user=user)
                except:
                    token = Token.objects.create(user=user)
                return Response(status=status.HTTP_202_ACCEPTED, data={"message": "Добро пожаловать", "token": token.key})
            else:
                return Response(status=status.HTTP_403_FORBIDDEN, data={"message": "Аккаунт не подтвержден"})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': "Неверный логин или пароль"})
