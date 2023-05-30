from django.contrib import admin
from .models import Course, Resource, Announcement, Message, Room, Enrollment, Participants

# Register your models here.
admin.site.register(Course)
admin.site.register(Resource)
admin.site.register(Announcement)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Participants)
admin.site.register(Enrollment)
