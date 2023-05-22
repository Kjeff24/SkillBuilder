from django.shortcuts import render, redirect
from django.contrib import messages
from course.forms import ResourceForm
from course.models import Resource


# Create Resource
def createResource(request, pk):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.save()
            messages.success(request, 'Resource created successfully.')
            return redirect('create-resource', pk=request.user)  # Redirect to the announcement list view
    else:
        form = ResourceForm(user=request.user)

    context = {'form': form}
    return render(request, "form/resource_form.html", context)


# Update resources created by employer
def updateResource(request, pk):
    resource = Resource.objects.get(id=pk)
    form = ResourceForm(instance=resource, user=request.user)

    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES, instance=resource, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resources updated successfully.')
            return redirect('update-resource', pk=pk)
        
    context = {'form': form, 'page':'update'}
    return render(request, "form/resource_form.html", context)


# Delete Resource
def deleteResource(request, pk):
    resource = Resource.objects.get(id=pk)

    if request.method == 'POST':
        resource.delete()
        messages.success(request, 'Resource deleted successfully.')
        return redirect('employer-home', pk=request.user)
    
    return render(request, 'course/delete.html', {'obj': resource})