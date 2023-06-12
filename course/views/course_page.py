from django.shortcuts import render
from django.http import JsonResponse 
from course.models import Course, Participants
from event.models import Event

# Course page for employees
def coursePage(request, pk):
    # Get course by id and display resources, announcements, rooms based on the course
    employee = request.user
    
    participants = Participants.objects.filter(user=employee)
    courses = [participant.course for participant in participants]
    
    course = Course.objects.get(pk=pk)
    
    context = {
        'course':course, 
        'courses':courses,
        'page': 'course_overview',
        }

    return render(request, "page/course_page.html", context)

# show all events in course page
def all_events(request, pk): 
    course = Course.objects.get(pk=pk)                                                                                                
    all_events = Event.objects.filter(course=course)                                                                                    
    out = []                                                                                                             
    for event in all_events:                                                                                             
        out.append({                                                                                                     
            'title': event.name,                                                                                         
            'id': event.id,                                                                                              
            'start': event.start.isoformat(),                                                        
            'end': event.end.isoformat(),                                                           
        })                                                                                                               
                                                                                                                      
    return JsonResponse(out, safe=False) 