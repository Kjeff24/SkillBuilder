from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

# User models that includes employee and employers
class User(AbstractUser):
    is_employer = models.BooleanField("Is employer",default=False)
    is_employee = models.BooleanField("Is employee", default=False)
    my_employer = models.CharField(max_length=200, null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
