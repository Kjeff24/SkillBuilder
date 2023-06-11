from django.shortcuts import render
from course.models import Course

# room page
def quizPage(request, pk):
    employee = request.user

    courses = Course.objects.filter(participants__user=employee)
    course = Course.objects.get(id=pk)
    context = {
        "course":course, 
        'courses':courses
    }

    return render(request, "page/quiz_page.html", context)