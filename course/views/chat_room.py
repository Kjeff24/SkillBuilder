from django.shortcuts import render, redirect
from course.models import Enrollment, Course, Room, Message

# Employee Chat room
def chatRoom(request,pk2,pk):
    employee = request.user

    enrollments = Enrollment.objects.filter(members__user=employee)

    # Retrieve the course based on the provided pk
    course = Course.objects.get(id=pk2)

    # We find the room based on the room_id
    room = Room.objects.get(id=pk)

    # We get all messages from a specific room
    room_messages = room.message_set.all().order_by('-created')
        
    # We get all participants in the specific room

    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        return redirect('chat-room', pk2=course.id, pk=room.id)
    
    context = {
        'room': room,
        'room_messages': room_messages,
        'enrollments': enrollments,
        'course': course,
        'page': 'chat-room'
    }
    
    return render(request, "chat/chat_room.html", context)