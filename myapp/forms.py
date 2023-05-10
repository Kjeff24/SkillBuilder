from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Course, Resource, Announcement, Room
from django.forms import ModelForm

# login form
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


# Employee signup
class EmployeeSignUpForm(UserCreationForm):
    employer_select = forms.ModelChoiceField(queryset=User.objects.filter(is_employer=True), widget=forms.TextInput(
            attrs={
                "class": "select-employer"
            }
        ))

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    is_employee = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',
                  'is_employee', 'employer_select')
    

    def save(self, commit=True):
        user = super().save(commit=False)
        user.my_employer = self.cleaned_data['employer_select']
        if commit:
            user.save()
        return user
        

    
# Employer Signup
class EmployerSignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    is_employer = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',
                  'password2', 'is_employer')

# Course form 
class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        exclude = ['course_participants', 'instructor']

# Resource form
class ResourceForm(ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'course', 'description', 'youtubeLink', 'file']

# Annoucement form class AnnouncementForm(forms.ModelForm):
class AnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content', 'course']

# Room form
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['room_host']