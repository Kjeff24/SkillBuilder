from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

MY_CHOICES = [
    ('A', 'Option A'),
    ('B', 'Option B'),
    ('C', 'Option C'),
]

class User(AbstractUser):
    username = models.CharField(
        max_length=50, null=True, blank=False, unique=True)
    is_employer = models.BooleanField("Is employer", default=True)
    is_employee = models.BooleanField("Is employee", default=True)
    first_name = models.CharField(max_length=50, null=True, blank=False)
    last_name = models.CharField(max_length=50, null=True, blank=False)
    email = models.EmailField(max_length=80, null=True,
                              unique=True, blank=False)
    avatar = models.ImageField(null=True, blank=True)
    bio = models.TextField(null=True)
    # employer = models.CharField(max_length=50, choices=MY_CHOICES)

    def get_employers(self):
        return User.objects.filter(is_employer=True)

    def get_employees(self):
        return User.objects.filter(is_employee=True)


class Employee(models.Model):
    pass


class Employer(models.Model):
    pass

