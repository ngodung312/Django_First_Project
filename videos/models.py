from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=256)
    length = models.PositiveIntegerField()
    release_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Customer(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone = models.PositiveIntegerField()

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    

