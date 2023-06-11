from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from myapp.models import User
from course.models import Course, Participants


# Employee home
@login_required(login_url='login')
def employeeHome(request, pk):
    # Render the enrollment form with a list of available courses
    employee = request.user
    employer = User.objects.get(username=employee.my_employer)
    # print(employer)
    employer_courses = Course.objects.filter(instructor__username=employer).distinct()
    
    # get all courses, enrolled by user
    participants = Participants.objects.filter(user=employee)
    courses = [participant.course for participant in participants]

    context = {'courses': courses, 'employer_courses':employer_courses}


    if request.method == 'POST':
        course_selected = request.POST.get('course')

        course = Course.objects.get(name=course_selected)
        user = User.objects.get(username=request.user.username)

        # Check if the course exists in the enrollment
        enrollment = Participants.objects.filter(course=course).first()

        if enrollment:
            # Check if the user exists in the participants
            participant = Participants.objects.filter(user=user).first()

            if participant:
                messages.success(request, 'You have already enrolled.')
                return render(request, "usersPage/employee_home.html", context)
            else:
                # Create a new participant
                participant = Participants.objects.create(user=user, course=course)
                messages.success(request, 'Enrollment successfully.')
                return render(request, "usersPage/employee_home.html", context)
        else:
            participant = Participants.objects.create(user=user, course=course)

            messages.success(request, 'Enrollment successfully.')
            return render(request, "usersPage/employee_home.html", context)
    
    return render(request, "usersPage/employee_home.html", context)