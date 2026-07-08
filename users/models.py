from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class AuthCode(models.Model):
    code = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.code)
