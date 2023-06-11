from django.shortcuts import render
from course.models import Course, Announcement, Resource, Room, Participants

# Course page for employees
def coursePage(request, pk):
    # Get course by id and display resources, announcements, rooms based on the course
    employee = request.user
    
    participants = Participants.objects.filter(user=employee)
    courses = [participant.course for participant in participants]
    
    course = Course.objects.get(pk=pk)

    context = {
        'course':course, 
        'courses':courses
        }

    return render(request, "page/course_page.html", context)