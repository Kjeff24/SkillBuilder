from django.shortcuts import render, redirect
from .forms import LoginForm, EmployerSignUpForm, EmployeeSignUpForm
from django.contrib.auth import authenticate, login
from .models import User

# Create your views here.
def home(request):



    return render(request, "myapp/home.html")

def loginPage(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_employer:
                login(request, user)
                return redirect('employer_home')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('employee_home')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'

    context = {'form': form, 'msg':msg}

    return render(request, "myapp/login.html", context)

# Employee signup
def employeeSignupPage(request):
    msg = None
    if request.method == 'POST':
        form = EmployeeSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'User created'
            return redirect('login')
        else:
            msg = 'form is not valid'
    else:
        form = EmployeeSignUpForm()

    context = {'form': form, 'msg':msg}

    return render(request, "myapp/employee_signup.html", context)


def employerSignupPage(request):
    msg = None
    if request.method == 'POST':
        form = EmployerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'User created'
            return redirect('login')
        else:
            msg = 'form is not valid'
    else:
        form = EmployerSignUpForm()

    context = {'form': form, 'msg':msg}

    return render(request, "myapp/employer_signup.html", context)


def employerHome(request):
    return render(request, "myapp/employer_home.html")

def employeeHome(request):
    return render(request, "myapp/employee_home.html")