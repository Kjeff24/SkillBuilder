from django.shortcuts import render, redirect
from django.contrib import messages
from myapp.models import User
from course.forms import UserForm

# Update user
def updateUser(request, pk):
    employers = User.objects.filter(is_employer=True).distinct()
    user = request.user 
    form = UserForm(instance=user, user=request.user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user, user=request.user)
        if form.is_valid():
            form.instance.my_employer = request.POST.get('my_employer')
            form.save()
            messages.success(request, 'User updated successfully.')
            return redirect('update-user', pk=user.id)

    context = {'form':form, 'page':'update', 'employers':employers}

    return render(request, "authenticate/employee_signup.html", context)
