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


# User Form
class UserForm(ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input-text"
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input-text"
            }
        )
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input-text"
            }
        )
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "input-text"
            }
        )
    )

    bio = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "update-bio input-text",
                'rows': 2
            }
        )
    )

    avatar = forms.ImageField(widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'bio', 'avatar']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # Retrieve the 'user' argument from kwargs
        super().__init__(*args, **kwargs)