from django.shortcuts import render, redirect
from .forms import LoginForm, EmployerSignUpForm, EmployeeSignUpForm, CourseForm, AnnouncementForm, ResourceForm, RoomForm, UserForm
from django.contrib.auth import authenticate, login, logout
from .models import User, Course, Announcement, Resource, Room, Message, Participants, Enrollment
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "myapp/home.html")

def about(request):
    return render(request, "myapp/about.html")

def contact(request):
    return render(request, "myapp/contact.html")


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

    return render(request, "myapp/login.html", context)


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
def employerHome(request, pk):
    user = request.user
    courses = Course.objects.filter(instructor=user)
    resources = Resource.objects.filter(course__in=courses)
    rooms = Room.objects.filter(course__in=courses)
    announcements = Announcement.objects.filter(course__in=courses)

    participants = Participants.objects.filter(course__in=courses)

    context = {
        'courses': courses,
        'resources': resources,
        'rooms': rooms,
        'announcements': announcements,
        'participants': participants
    }
    return render(request, "myapp/employer_home.html", context)


# Employee home
def employeeHome(request, pk):
    # Render the enrollment form with a list of available courses
    employee = request.user
    employer = User.objects.get(username=employee.my_employer)
    courses = Course.objects.filter(instructor__username=employer).distinct()
    enrollments = Enrollment.objects.filter(participants__user=employee)

    context = {'courses': courses, 'enrollments':enrollments}


    if request.method == 'POST':
        course_selected = request.POST.get('course')

        course = Course.objects.get(name=course_selected)
        user = User.objects.get(username=request.user.username)

        # Check if the course exists in the enrollment
        enrollment = Enrollment.objects.filter(course=course).first()

        if enrollment:
            # Check if the user exists in the participants
            participant = Participants.objects.filter(user=user).first()

            if participant:
                messages.success(request, 'You have already enrolled.')
                return render(request, "myapp/employee_home.html", context)
            else:
                # Create a new participant
                participant = Participants.objects.create(user=user, course=course)
                enrollment.participants.add(participant)
                messages.success(request, 'Enrollment successfully.')
                return render(request, "myapp/employee_home.html", context)
        else:
            # Create a new enrollment and participant
            enrollment = Enrollment.objects.create(course=course)
            participant = Participants.objects.create(user=user, course=course)
            enrollment.participants.add(participant)

            messages.success(request, 'Enrollment successfully.')
            return render(request, "myapp/employee_home.html", context)
    
    return render(request, "myapp/employee_home.html", context)


# Course form
def createCourse(request, pk):
    form = CourseForm()
    if request.method == 'POST':
        Course.objects.create(
            instructor=request.user,
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )
        messages.success(request, 'Course created successfully.')
        return redirect('create-course', pk=request.user)

    context = {'form': form}

    return render(request, "myapp/course_form.html", context)


# Create Annoucement    
def createAnnoucement(request, pk):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, user=request.user)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.save()
            messages.success(request, 'Announcement created successfully.')
            return redirect('create-announcement', pk=request.user)  # Redirect to the announcement list view
    else:
        form = AnnouncementForm(user=request.user)

    context = {'form': form}
    return render(request, "myapp/announcement_form.html", context)

# Create Resource
def createResource(request, pk):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.save()
            messages.success(request, 'Resource created successfully.')
            return redirect('create-resource', pk=request.user)  # Redirect to the announcement list view
    else:
        form = ResourceForm(user=request.user)

    context = {'form': form}
    return render(request, "myapp/resource_form.html", context)

# Create room
def createRoom(request, pk):
    if request.method == 'POST':
        form = RoomForm(request.POST, user=request.user)
        if form.is_valid():
            room = form.save(commit=False)
            room.save()
            messages.success(request, 'Room created successfully.')
            return redirect('create-room', pk=request.user)  # Redirect to the announcement list view
    else:
        form = RoomForm(user=request.user)

    context = {'form': form}
    return render(request, "myapp/room_form.html", context)


# Course page for employees
def coursePage(request, pk):
    # Get course by id and display resources, announcements, rooms based on the course
    employee = request.user
    course = Course.objects.get(id=pk)
    resources = Resource.objects.filter(course=course)
    announcements = Announcement.objects.filter(course=course)
    rooms = Room.objects.filter(course=course)

    enrollments = Enrollment.objects.filter(participants__user=employee)

    context = {
        'course':course, 
        'resources':resources, 
        'announcements':announcements, 
        'rooms':rooms, 
        'enrollments': enrollments
        }

    return render(request, "myapp/course_page.html", context)


# resource page
def resourcePage(request, pk):
    employee = request.user

    enrollments = Enrollment.objects.filter(participants__user=employee)

     # Retrieve the course based on the provided pk
    course = Course.objects.get(id=pk)

    # Retrieve the resources associated with the course
    resources = Resource.objects.filter(course=course).order_by('-updated')
    
    # Pass the course and resources to the template
    context = {
        'course': course,
        'resources': resources,
        'enrollments': enrollments
    }

    return render(request, "myapp/resource_page.html", context)

# announcement page
def announcementPage(request, pk):
    employee = request.user

    enrollments = Enrollment.objects.filter(participants__user=employee)

    # Retrieve the course based on the provided pk
    course = Course.objects.get(id=pk)

    # Retrieve the announcements associated with the course
    announcements = Announcement.objects.filter(course=course).order_by('-updated')

    context = {
        'course': course,
        'announcements': announcements,
        'enrollments': enrollments
    }

    return render(request, "myapp/announcement_page.html", context)


# room page
def roomPage(request, pk):
    employee = request.user

    enrollments = Enrollment.objects.filter(participants__user=employee)

    # Retrieve the course based on the provided pk
    course = Course.objects.get(id=pk)

    # Retrieve the announcements associated with the course
    rooms = Room.objects.filter(course=course)

    context = {
        'course': course,
        'rooms': rooms,
        'enrollments': enrollments,
    }

    return render(request, "myapp/room_page.html", context)


# Employee Chat room
def chatRoom(request,pk2,pk):
    employee = request.user

    enrollments = Enrollment.objects.filter(participants__user=employee)

    # Retrieve the course based on the provided pk
    course = Course.objects.get(id=pk2)

    # We find the room based on the room_id
    room = Room.objects.get(id=pk)

    # We get all messages from a specific room
    room_messages = room.message_set.all().order_by('-created')
        
    # We get all participants in the specific room

    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        return redirect('chat-room', pk2=course.id, pk=room.id)
    
    context = {
        'room': room,
        'room_messages': room_messages,
        'enrollments': enrollments,
        'course': course,
        'page': 'chat-room'
    }
    
    return render(request, "myapp/chat_room.html", context)

# Update courses created by employer
def updateCourse(request, pk):
    course = Course.objects.get(id=pk)
    form = CourseForm(instance=course)
    participants = Participants.objects.filter(course=course)
   
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course updated successfully.')
            return redirect('update-course', pk=pk)
         
    context = {'form': form, 'page':'update', 'participants':participants}
    return render(request, "myapp/course_form.html", context)


# Update resources created by employer
def updateResource(request, pk):
    resource = Resource.objects.get(id=pk)
    form = ResourceForm(instance=resource, user=request.user)

    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES, instance=resource, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resources updated successfully.')
            return redirect('update-resource', pk=pk)
        
    context = {'form': form, 'page':'update'}
    return render(request, "myapp/resource_form.html", context)


# Update announcement created by employer
def updateAnnouncement(request, pk): 
    announcement = Announcement.objects.get(id=pk)
    form = AnnouncementForm(instance=announcement, user=request.user)

    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=announcement, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Announcement updated successfully.')
            return redirect('update-announcement', pk=pk)
        
    context = {'form': form, 'page':'update'}
    return render(request, "myapp/announcement_form.html", context)


# Update room created by employer
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room, user=request.user)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Room updated successfully.')
            return redirect('update-room', pk=pk)
            
    
    context = {'form': form, 'page':'update'}
    return render(request, "myapp/room_form.html", context)

# Update user
def updateUser(request, pk):
    employers = User.objects.filter(is_employer=True)
    user = request.user 
    form = UserForm(instance=user, user=request.user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user, user=request.user)
        if form.is_valid():
            form.instance.my_employer = request.POST.get('my_employer')  # Assign the selected value to my_employer
            form.save()
            messages.success(request, 'User updated successfully.')
            return redirect('update-user', pk=user.id)

    context = {'form':form, 'page':'update', 'employers':employers}

    return render(request, "myapp/employee_signup.html", context)

# Delete course
def deleteCourse(request, pk):
    course = Course.objects.get(id=pk)

    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course deleted successfully.')
        return redirect('employer-home', pk=request.user)
    
    return render(request, 'myapp/delete.html', {'obj': course})


# Delete announcement
def deleteAnnouncement(request, pk):
    announcement = Announcement.objects.get(id=pk)

    if request.method == 'POST':
        announcement.delete()
        messages.success(request, 'Announcement deleted successfully.')
        return redirect('employer-home', pk=request.user)
    
    return render(request, 'myapp/delete.html', {'obj': announcement})


# Delete Resource
def deleteResource(request, pk):
    resource = Resource.objects.get(id=pk)

    if request.method == 'POST':
        resource.delete()
        messages.success(request, 'Resource deleted successfully.')
        return redirect('employer-home', pk=request.user)
    
    return render(request, 'myapp/delete.html', {'obj': resource})


# Delete room
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == 'POST':
        room.delete()
        messages.success(request, 'Room deleted successfully.')
        return redirect('employer-home', pk=request.user)
    
    return render(request, 'myapp/delete.html', {'obj': room})


        