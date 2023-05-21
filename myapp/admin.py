from django.contrib import admin
from .models import User, Course, Resource, Announcement, Message, Room, Participants, Enrollment

# Register your models here.
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Resource)
admin.site.register(Announcement)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Participants)
admin.site.register(Enrollment)