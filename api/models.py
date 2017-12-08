from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):
    number = models.CharField(max_length=20)


class Sensor(models.Model):
    type = models.CharField(max_length=255)
    status = models.CharField(max_length=50)


class Territory(models.Model):
    square = models.IntegerField()
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE)
