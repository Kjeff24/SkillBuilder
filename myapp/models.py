from django.db import models
from django.contrib.auth.models import AbstractUser

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


# Course model allows employers to create course
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    course_participants = models.ManyToManyField(User, related_name='course_participants', blank=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()

    def __str__(self):
        return self.name
    
# Resources model allows employers to add resources based on course
class Resource(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    youtubeLink = models.TextField(blank=True)
    file = models.FileField(upload_to='resources/')

    def __str__(self):
        return self.name

# Announcement model allows employers to add announcements based on course
class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
# Room allows employees to chat
class Room(models.Model):
    room_host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    room_topic = models.CharField(max_length=200, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    room_description = models.TextField(null=True, blank=True)
    created  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
    
# Message allows host and participants to converse
class Message(models.Model):
    message_host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]