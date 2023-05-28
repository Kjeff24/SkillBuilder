from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

# login form
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "login-input",
                "id":"username",
                "autocomplete":"username",
                "placeholder": "Enter your username",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "login-input",
                "id":"passwordField",
                "autocomplete":"password",
                "placeholder": "Enter your password",
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
                "class": "input-text",
                "autocomplete":"first_name",
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input-text",
                "autocomplete":"last_name",
            }
        )
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input-text",
                "autocomplete":"username",
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
                "class": "input-text",
                "autocomplete":"email",
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
                "class": "input-text",
                "autocomplete":"first_name",
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input-text",
                "autocomplete":"last_name",
            }
        )
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input-text",
                "autocomplete":"username",
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
                "class": "input-text",
                "autocomplete":"email",
            }
        )
    )
    is_employer = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',
                  'password2', 'is_employer')
        