from django.contrib import admin
from .models import *

class ParticipantsInline(admin.TabularInline):
    model = Participants

class CourseAdmin(admin.ModelAdmin):
    inlines = [ParticipantsInline]

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Resource)
admin.site.register(Announcement)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Participants)