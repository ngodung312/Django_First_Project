from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    group = models.CharField(max_length=256, blank=True)
    role = models.CharField(max_length=256, blank=True)

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    is_verified = models.BooleanField('verified', default=False) # Add the `is_verified` flag
    verification_uuid = models.UUIDField('Unique Verification UUID', default=uuid.uuid4)

    login_times = models.DecimalField(max_digits=10, decimal_places=0, blank=False, default=0, editable=False)