from django.shortcuts import render, redirect
from .forms import LoginForm, EmployerSignUpForm, EmployeeSignUpForm, CourseForm, AnnouncementForm, ResourceForm, RoomForm
from django.contrib.auth import authenticate, login
from .models import User, Course, Announcement, Resource, Room
from django.contrib import messages

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
                return redirect('employee-home')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'

    context = {'form': form, 'msg': msg}

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

    context = {'form': form, 'msg': msg}

    return render(request, "myapp/employee_signup.html", context)

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

    return render(request, "myapp/employer_signup.html", context)

# Employer home


def employerHome(request):
    user = request.user
    courses = Course.objects.filter(instructor=user)

    resources = Resource.objects.filter(course__in=courses)
    rooms = Room.objects.filter(course__in=courses)
    announcements = Announcement.objects.filter(course__in=courses)

    context = {
        'courses': courses,
        'resources': resources,
        'rooms': rooms,
        'announcements': announcements,
    }
    return render(request, "myapp/employer_home.html", context)

# Employee home


def employeeHome(request):
    return render(request, "myapp/employee_home.html")

# Course form


def createCourse(request):
    form = CourseForm()
    if request.method == 'POST':
        Course.objects.create(
            instructor=request.user,
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )
        messages.success(request, 'Course created successfully.')
        return redirect('create-course')

    context = {'form': form}

    return render(request, "myapp/course_form.html", context)


def createAnnoucement(request):
    form = AnnouncementForm()
    if request.method == 'POST':
        Announcement.objects.create(
            title=request.POST.get('title'),
            content=request.POST.get('content'),
            course=request.POST.get('course')
        )
        messages.success(request, 'Announcement created successfully.')
        return redirect('create-announcement')

    context = {'form': form}
    return render(request, "myapp/announcement_form.html", context)


def createResource(request):
    form = ResourceForm()

    if request.method == 'POST':
        Resource.objects.create(
            file=request.POST.get('file'),
            course=request.POST.get('course'),
            youtubeLink=request.POST.get('youtubeLink'),
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )
        messages.success(request, 'Resources created successfully.')
        return redirect('create-resource')

    context = {'form': form}
    return render(request, "myapp/resource_form.html", context)


def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        Room.objects.create(
            room_host=request.user,
            room_topic=request.POST.get('room_topic'),
            course=request.POST.get('course'),
            description=request.POST.get('description')
        )
        messages.success(request, 'Room created successfully.')
        return redirect('create-room')

    context = {'form': form}
    return render(request, "myapp/room_form.html", context)
