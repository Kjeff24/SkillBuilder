from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Course, Resource, Announcement, Room
from django.forms import ModelForm

# login form
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "login-input"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "login-input",
                "id":"passwordField"
            }
        )
    )


# Employee signup
class EmployeeSignUpForm(UserCreationForm):
    # Create a modelchoicefield to display only employers
    employer_select = forms.ModelChoiceField(
        queryset=User.objects.filter(is_employer=True), widget=forms.Select(attrs={'class': 'input-text'}))

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
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input-text",
                "id":"passwordField1"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input-text",
                "id":"passwordField2"
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
    is_employee = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',
                  'is_employee', 'employer_select')

    # Based on the employer the user select, it it assigned to my_employer field in User model
    def save(self, commit=True):
        user = super().save(commit=False)
        user.my_employer = self.cleaned_data['employer_select']
        if commit:
            user.save()
        return user


# Employer Signup
class EmployerSignUpForm(UserCreationForm):
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
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input-text",
                "id":"passwordField1"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input-text",
                "id":"passwordField2"
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
                "class": "update-bio",
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
    
    # Based on the employer the user select, it it assigned to my_employer field in User model
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.my_employer = self.cleaned_data['my_employer']
    #     if commit:
    #         user.save()
    #     return user