from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


class User(AbstractUser):
    USER_TYPES = (
        ("Admin", "Admin"),
        ("MyUser", "MyUser")
    )

    number = models.CharField(max_length=20, unique=True)
    user_type = models.CharField(choices=USER_TYPES, max_length=50, editable=False, default='MyUser')


class Sensor(models.Model):
    type = models.CharField(max_length=255)
    status = models.CharField(max_length=50)



class Territory(models.Model):
    square = models.IntegerField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE)
