from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str 
from django.conf import settings
from myapp.tokens import account_activation_token
from myapp.forms import LoginForm, EmployerSignUpForm, EmployeeSignUpForm
from django.contrib import messages
from django.core.mail import EmailMessage
from myapp.models import User


def loginPage(request):
    form = LoginForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                if user.is_employer and user.is_email_verified:
                    login(request, user)
                    return redirect('employer-home', pk=request.user)
                elif user.is_employee and user.is_email_verified:
                    login(request, user)
                    return redirect('employee-home', pk=request.user)
                else:
                    messages.add_message(request, messages.ERROR,
                                         'Your email is not verified.')
            else:
                messages.add_message(request, messages.ERROR,
                                     'Invalid credentials, try again')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error validating, try again')

    context = {'form': form}

    return render(request, "authenticate/login.html", context)


# Logout User
def logoutUser(request):
    logout(request)
    return redirect('login')


# Employee signup
def employeeSignupPage(request):
    if request.method == 'POST':
        form = EmployeeSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_activation_email(user, request)
            messages.add_message(request, messages.SUCCESS,
                                         'We sent you an email to verify your account')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
    else:
        form = EmployeeSignUpForm()

    context = {'form': form}

    return render(request, "authenticate/employee_signup.html", context)


# Employer Signup
def employerSignupPage(request):
    if request.method == 'POST':
        form = EmployerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_activation_email(user, request)
            messages.add_message(request, messages.SUCCESS,
                                         'We sent you an email to verify your account')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
    else:
        form = EmployerSignUpForm()

    context = {'form': form}

    return render(request, "authenticate/employer_signup.html", context)

# sends activation code to the email
def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Activate your account'
    
    # render a template file and pass in context
    email_body = render_to_string('authenticate/activate.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user)
    })

    # create an email from using EmailMessage()
    email = EmailMessage(subject=email_subject, body=email_body,
                         from_email=settings.EMAIL_FROM_USER,
                         to=[user.email]
                         )

    # send email
    email.send()


# activate user
def activate_user(request, uidb64, token):

    # decode uid64 back to the user id, and get the user
    try:
        uid = force_str (urlsafe_base64_decode(uidb64))

        user = User.objects.get(pk=uid)

    except Exception as e:
        user = None

    # checks the user and token with the token generated from token.py   
    if user and account_activation_token.check_token(user, token):
        user.is_email_verified = True
        user.save()

        messages.add_message(request, messages.SUCCESS,
                             'Email verified, you can now login')
        return redirect(reverse('login'))

    return render(request, 'authenticate/activate-failed.html', {"user": user})
