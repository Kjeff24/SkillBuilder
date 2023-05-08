from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login

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
                return redirect('home')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('home')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'

    context = {'form': form, 'msg':msg}

    return render(request, "myapp/login.html", context)

def signupPage(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'User created'
            return redirect('login.html')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()

    context = {'form': form, 'msg':msg}

    return render(request, "myapp/signup.html", context)