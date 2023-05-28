from django.shortcuts import render
from myapp.models import User
from course.models import Course, Announcement, Resource, Room, Participants, Enrollment
from django.contrib import messages


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
    return render(request, "usersPage/employer_home.html", context)


# Employee home
def employeeHome(request, pk):
    # Render the enrollment form with a list of available courses
    employee = request.user
    employer = User.objects.get(username=employee.my_employer)
    # print(employer)
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
                return render(request, "usersPage/employee_home.html", context)
            else:
                # Create a new participant
                participant = Participants.objects.create(user=user, course=course)
                enrollment.participants.add(participant)
                messages.success(request, 'Enrollment successfully.')
                return render(request, "usersPage/employee_home.html", context)
        else:
            # Create a new enrollment and participant
            enrollment = Enrollment.objects.create(course=course)
            participant = Participants.objects.create(user=user, course=course)
            enrollment.participants.add(participant)

            messages.success(request, 'Enrollment successfully.')
            return render(request, "usersPage/employee_home.html", context)
    
    return render(request, "usersPage/employee_home.html", context)
