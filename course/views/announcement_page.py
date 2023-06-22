from django.shortcuts import render, get_object_or_404
from course.models import Course, Announcement, Participants

"""Announcement page """
def announcementPage(request, pk):
    employee = request.user
    
    """get all courses, enrolled by user """
    participants = Participants.objects.filter(user=employee)
    courses = [participant.course for participant in participants]

    """Retrieve the course based on the provided pk """
    course = Course.objects.get(pk=pk)

    """Retrieve the announcements associated with the course """
    announcements = Announcement.objects.filter(course=course).order_by('-updated')

    context = {
        'course': course,
        'announcements': announcements,
        'courses': courses
    }

    return render(request, "page/announcement_page.html", context)
