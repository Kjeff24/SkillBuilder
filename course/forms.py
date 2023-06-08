from .models import Course, Resource, Announcement, Room
from django.forms import ModelForm
from django import forms
from myapp.models import User

# Course form
class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        exclude = ['course_participants', 'instructor']


# Resource form
class ResourceForm(ModelForm):
    # Shows only courses, created by the employer
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # Retrieve the 'user' argument from kwargs
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.filter(instructor=user)

    class Meta:
        model = Resource
        fields = ['name', 'course', 'description', 'youtubeLink', 'file']


# Annoucement form class AnnouncementForm(forms.ModelForm):
class AnnouncementForm(ModelForm):
    # Shows only courses, created by the employer
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # Retrieve the 'user' argument from kwargs
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.filter(instructor=user)

    class Meta:
        model = Announcement
        fields = ['title', 'content', 'course']


# Room form
class RoomForm(ModelForm):
    # Shows only courses, created by the employer
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # Retrieve the 'user' argument from kwargs
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.filter(instructor=user)
        
    class Meta:
        model = Room
        fields = ['room_topic', 'course', 'room_description']
