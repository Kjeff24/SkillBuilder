from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from urllib.parse import urlencode
from course.models import Course, Resource, Participants
from django.db.models import Q
from django.http import StreamingHttpResponse

# Resource page
def resourcePage(request, pk):
    employee = request.user
    
    participants = Participants.objects.filter(user=employee)
    courses = [participant.course for participant in participants]

    q = request.GET.get('q', '')

    files_by_type = {
        'pdf': 'pdf_files',
        'image': 'image_files',
        'audio': 'audio_files',
        'video': 'video_files',
        'link': 'youtube_links',
    }

    file_types = files_by_type.keys()
    resources = {}

    for file_type in file_types:
        resources[files_by_type[file_type]] = Resource.objects.filter(
            Q(name__icontains=q) |
            Q(description__icontains=q) |
            Q(file__icontains=q) |
            Q(youtubeLink__icontains=q) |
            Q(file_type__icontains=q),
            file_type=file_type,
            course__in=courses
        ).order_by('-updated')

    context = {
        'course': Course.objects.get(id=pk),
        'courses': courses,
        **resources
    }

    return render(request, "page/resource_page.html", context)


# count the number of downloads
def downloadFile(request, pk):
    file = Resource.objects.get(id=pk)
    # Get the current user's participant object for the specific course
    user_activities = Participants.objects.get(user=request.user, course=file.course)
    # Increase the download count for the user
    user_activities.download_count()
    # increase number of downloads of a particular
    file.download_count()
    messages.success(request, 'Download successfully.')
    return redirect('resource', pk=file.course.id)

# Preview pdf
def previewPdf(request, pk):
    file = Resource.objects.get(id=pk)
    # pdf is streamed in chunks, rather than loading entire file
    def file_iterator():
        with open(file.file.path, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                yield chunk
    # use StreamingHttpResponse to load pdf content
    response = StreamingHttpResponse(
        file_iterator(), content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="{}"'.format(
        urlencode({'': file.file.name}))
    return response