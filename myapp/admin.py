from django.contrib import admin
from .models import User, Course, Resource, Announcement, Message, Room

# Register your models here.
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Resource)
admin.site.register(Announcement)
admin.site.register(Room)