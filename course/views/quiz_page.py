from django.shortcuts import render
from course.models import Course, Enrollment

# room page
def quizPage(request, pk):
    employee = request.user

    enrollments = Enrollment.objects.filter(participants__user=employee)
    course = Course.objects.get(id=pk)
    context = {
        "course":course, 
        'enrollments':enrollments
    }

    return render(request, "page/quiz_page.html", context)