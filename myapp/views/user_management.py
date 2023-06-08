from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from myapp.models import User
from myapp.forms import UserForm

# Update user
@login_required(login_url='login')
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

    return render(request, "authenticate/user_update.html", context)
