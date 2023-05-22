from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from myapp.forms import LoginForm, EmployerSignUpForm, EmployeeSignUpForm
from django.contrib import messages

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
                return redirect('employer-home', pk=request.user)
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('employee-home', pk=request.user)
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'

    context = {'form': form, 'msg': msg}

    return render(request, "authenticate/login.html", context)


# Logout User
def logoutUser(request):
    logout(request)
    return redirect('login')


# Employee signup
def employeeSignupPage(request):
    msg = None
    if request.method == 'POST':
        form = EmployeeSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course created successfully.')
            return redirect('login')
        else:
            msg = 'form is not valid'
    else:
        form = EmployeeSignUpForm()

    context = {'form': form, 'msg': msg}

    return render(request, "authenticate/employee_signup.html", context)


# Employer Signup
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

    context = {'form': form, 'msg': msg}

    return render(request, "authenticate/employer_signup.html", context)