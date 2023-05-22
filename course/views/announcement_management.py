from django.shortcuts import render, redirect
from django.contrib import messages
from course.forms import AnnouncementForm
from course.models import Announcement


# Create Annoucement    
def createAnnoucement(request, pk):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, user=request.user)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.save()
            messages.success(request, 'Announcement created successfully.')
            return redirect('create-announcement', pk=request.user)  # Redirect to the announcement list view
    else:
        form = AnnouncementForm(user=request.user)

    context = {'form': form}
    return render(request, "form/announcement_form.html", context)


# Update announcement created by employer
def updateAnnouncement(request, pk): 
    announcement = Announcement.objects.get(id=pk)
    form = AnnouncementForm(instance=announcement, user=request.user)

    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=announcement, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Announcement updated successfully.')
            return redirect('update-announcement', pk=pk)
        
    context = {'form': form, 'page':'update'}
    return render(request, "form/announcement_form.html", context)


# Delete announcement
def deleteAnnouncement(request, pk):
    announcement = Announcement.objects.get(id=pk)

    if request.method == 'POST':
        announcement.delete()
        messages.success(request, 'Announcement deleted successfully.')
        return redirect('employer-home', pk=request.user)
    
    return render(request, 'course/delete.html', {'obj': announcement})