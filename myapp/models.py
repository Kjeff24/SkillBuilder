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


# Course model allows employers to create course
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


# Course Participants
class Participants(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return str(self.user)



# Enrollment into a course
class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)
    participants = models.ManyToManyField(Participants, related_name='participants', blank=True)
    
    def __str__(self):
        return str(self.course)


# Resources model allows employers to add resources based on course
class Resource(models.Model):
    name = models.CharField(max_length=30)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField(max_length=50, blank=True)
    youtubeLink = models.TextField(blank=True)
    file = models.FileField(upload_to='resources/', blank=True)
    created  = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Announcement model allows employers to add announcements based on course
class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    created  = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
# Room allows employees to chat
class Room(models.Model):
    room_topic = models.CharField(max_length=200, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    room_description = models.TextField(null=True, blank=True)
    created  = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.room_topic
    
# Message allows host and participants to converse
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]
