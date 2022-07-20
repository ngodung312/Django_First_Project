from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    group = models.CharField(max_length=256)
    role = models.CharField(max_length=256)
