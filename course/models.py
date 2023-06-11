from django.db import models
from myapp.models import User

# Create your models here.
# Course model allows employers to create course
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


# Resources model allows employers to add resources based on course
class Resource(models.Model):
    FILE_TYPES = (
        ('pdf', 'PDF'),
        ('image', 'Image'),
        ('audio', 'Audio'),
        ('video', 'Video'),
    )
    
    name = models.CharField(max_length=30)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField(max_length=50, blank=True)
    file_type = models.CharField(max_length=10, choices=FILE_TYPES, default="null")
    youtubeLink = models.TextField(blank=True)
    file = models.FileField(upload_to='resources/', blank=True)
    created  = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_download_count = models.PositiveIntegerField(default=0)
    user_email_sent = models.PositiveIntegerField(default=0)

    def download_count(self):
        self.user_download_count += 1
        self.save()

    def email_count(self):
        self.user_email_sent += 1
        self.save()

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
    
    
# Course Participants
class Participants(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE) 
    room =  models.ForeignKey(Room, on_delete=models.SET_NULL, null=True) 
    user_download_count = models.PositiveIntegerField(default=0)
    user_email_sent = models.PositiveIntegerField(default=0)

    def download_count(self):
        self.user_download_count += 1
        self.save()

    def email_count(self):
        self.user_email_sent += 1
        self.save()
        
    def has_course(self):
        return self.course is not None
        
    def __str__(self):
        return str(self.user)