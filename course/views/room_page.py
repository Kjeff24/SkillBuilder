from django.shortcuts import render
from course.models import Enrollment, Course, Room

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

    return render(request, "page/room_page.html", context)