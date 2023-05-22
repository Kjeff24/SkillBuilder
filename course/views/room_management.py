

from django.shortcuts import render, redirect
from django.contrib import messages
from course.forms import RoomForm
from course.models import Room


# Create room
def createRoom(request, pk):
    if request.method == 'POST':
        form = RoomForm(request.POST, user=request.user)
        if form.is_valid():
            room = form.save(commit=False)
            room.save()
            messages.success(request, 'Room created successfully.')
            return redirect('create-room', pk=request.user)  # Redirect to the announcement list view
    else:
        form = RoomForm(user=request.user)

    context = {'form': form}
    return render(request, "form/room_form.html", context)


# Update room created by employer
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room, user=request.user)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Room updated successfully.')
            return redirect('update-room', pk=pk)
            
    
    context = {'form': form, 'page':'update'}
    return render(request, "form/room_form.html", context)


# Delete room
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == 'POST':
        room.delete()
        messages.success(request, 'Room deleted successfully.')
        return redirect('employer-home', pk=request.user)
    
    return render(request, 'course/delete.html', {'obj': room})
