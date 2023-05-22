from django.shortcuts import render, redirect
from django.contrib import messages
from course.forms import CourseForm
from course.models import Course, Participants


# Course form
def createCourse(request, pk):
    form = CourseForm()
    if request.method == 'POST':
        Course.objects.create(
            instructor=request.user,
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )
        messages.success(request, 'Course created successfully.')
        return redirect('create-course', pk=request.user)

    context = {'form': form}

    return render(request, "form/course_form.html", context)


# Update courses created by employer
def updateCourse(request, pk):
    course = Course.objects.get(id=pk)
    form = CourseForm(instance=course)
    participants = Participants.objects.filter(course=course)
   
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course updated successfully.')
            return redirect('update-course', pk=pk)
         
    context = {'form': form, 'page':'update', 'participants':participants}
    return render(request, "form/course_form.html", context)


# Delete course
def deleteCourse(request, pk):
    course = Course.objects.get(id=pk)

    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course deleted successfully.')
        return redirect('employer-home', pk=request.user)
    
    return render(request, 'course/delete.html', {'obj': course})