from django.shortcuts import render
from course.models import Enrollment, Course, Announcement, Resource, Room

# Course page for employees
def coursePage(request, pk):
    # Get course by id and display resources, announcements, rooms based on the course
    employee = request.user
    course = Course.objects.get(id=pk)
    resources = Resource.objects.filter(course=course)
    announcements = Announcement.objects.filter(course=course)
    rooms = Room.objects.filter(course=course)

    enrollments = Enrollment.objects.filter(members__user=employee)

    context = {
        'course':course, 
        'resources':resources, 
        'announcements':announcements, 
        'rooms':rooms, 
        'enrollments': enrollments
        }

    return render(request, "page/course_page.html", context)