from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_employer = models.BooleanField("Is employer", default=True)
    is_employee = models.BooleanField("Is employee", default=True)
    my_employer = models.CharField(max_length=200, null=True, blank=True)