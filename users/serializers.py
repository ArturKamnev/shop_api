from rest_framework import serializers
from .models import AuthCode
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

class AuthCodeSerializer(serializers.Serializer):
    auth_code = serializers.IntegerField()

    def validate_auth_code(self, auth_code):
        try:
            code = AuthCode.objects.get(code=auth_code)
        except AuthCode.DoesNotExist:
            raise ValidationError('Invalid code')
        return code.user

class UserAuthentificateSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=150)
    password = serializers.CharField(required=True)

class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=150)
    password = serializers.CharField(required=True)

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('user already exists')
        