from django.shortcuts import render
from course.models import Enrollment, Course, Announcement

# announcement page
def announcementPage(request, pk):
    employee = request.user

    enrollments = Enrollment.objects.filter(members__user=employee)

    # Retrieve the course based on the provided pk
    course = Course.objects.get(id=pk)

    # Retrieve the announcements associated with the course
    announcements = Announcement.objects.filter(course=course).order_by('-updated')

    context = {
        'course': course,
        'announcements': announcements,
        'enrollments': enrollments
    }

    return render(request, "page/announcement_page.html", context)