from django.shortcuts import render, get_object_or_404
from course.models import Course, Room, Participants

# room page
def roomPage(request, pk):
    employee = request.user

    participants = Participants.objects.filter(user=employee)
    courses = [participant.course for participant in participants]
    
    # Retrieve the course based on the provided pk
    course = Course.objects.get(id=pk)

    # Retrieve the announcements associated with the course
    rooms = Room.objects.filter(course__in=courses)

    context = {
        'course': course,
        'rooms': rooms,
        'courses': courses,
    }

    return render(request, "page/room_page.html", context)