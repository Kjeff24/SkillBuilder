from django.shortcuts import render
from course.models import Enrollment, Course, Resource

# resource page
def resourcePage(request, pk):
    employee = request.user

    enrollments = Enrollment.objects.filter(members__user=employee)

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

    return render(request, "page/resource_page.html", context)