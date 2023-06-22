from django.contrib import admin
from django.contrib.admin import register
from employerAdmin.employer_admin import employer_admin_site
from quiz.models import Quiz, Question, Answer, Result
from course.models import *
from event.models import *

class ParticipantsInline(admin.TabularInline):
    """
    Inline model admin for Participants.

    Provides an inline editing interface for Participants model within QuestionAdmin.
    """
    model = Participants


@register(Course, site=employer_admin_site)
class CourseAdmin(admin.ModelAdmin):
    inlines = [ParticipantsInline]
    # Customize the fields displayed in the admin list view for courses
    list_display = ('name', 'instructor', 'created', 'updated')
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_employer:
            return qs
        else:
            return qs.filter(instructor=request.user)

@register(Participants, site=employer_admin_site)
class ParticipantsAdmin(admin.ModelAdmin):
    # Customize the fields displayed in the admin list view for participants
    list_display = ('user', 'course')
    
    def get_queryset(self, request):
        # Filter queryset to show only the courses created by the logged-in employer
        qs = super().get_queryset(request)
        if request.user.is_employer:
            return qs
        else:
            return qs.filter(instructor=request.user)

@register(Resource, site=employer_admin_site)
class ResourceAdmin(admin.ModelAdmin):
    # Customize the fields displayed in the admin list view for resources
    list_display = ('name', 'course', 'created', 'updated')
    
    def get_queryset(self, request):
        # Filter queryset to show only the courses created by the logged-in employer
        qs = super().get_queryset(request)
        if request.user.is_employer:
            return qs
        else:
            return qs.filter(instructor=request.user)

@register(Announcement, site=employer_admin_site)
class AnnouncementAdmin(admin.ModelAdmin):
    # Customize the fields displayed in the admin list view for announcements
    list_display = ('title', 'course', 'date', 'created', 'updated')
    
    def get_queryset(self, request):
        # Filter queryset to show only the courses created by the logged-in employer
        qs = super().get_queryset(request)
        if request.user.is_employer:
            return qs
        else:
            return qs.filter(instructor=request.user)

@register(Room, site=employer_admin_site)
class RoomAdmin(admin.ModelAdmin):
    # Customize the fields displayed in the admin list view for rooms
    list_display = ('room_topic', 'course', 'created', 'updated')
    
    def get_queryset(self, request):
        # Filter queryset to show only the courses created by the logged-in employer
        qs = super().get_queryset(request)
        if request.user.is_employer:
            return qs
        else:
            return qs.filter(instructor=request.user)


# Quiz 

@register(Quiz, site=employer_admin_site)
class QuizAdmin(admin.ModelAdmin):
    # Customize the fields displayed in the admin list view for quizzes
    list_display = ('name', 'course', 'number_of_questions', 'time', 'required_score_to_pass', 'difficluty')
    
    def get_queryset(self, request):
        # Filter queryset to show only the courses created by the logged-in employer
        qs = super().get_queryset(request)
        if request.user.is_employer:
            return qs
        else:
            return qs.filter(instructor=request.user)

class AnswerInline(admin.TabularInline):
    """
    Inline model admin for Answer.

    Provides an inline editing interface for Answer model within QuestionAdmin.
    """
    model = Answer

@register(Question, site=employer_admin_site)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    # Customize the fields displayed in the admin list view for questions
    list_display = ('text', 'quiz', 'created')
    
    def get_queryset(self, request):
        # Filter queryset to show only the courses created by the logged-in employer
        qs = super().get_queryset(request)
        if request.user.is_employer:
            return qs
        else:
            return qs.filter(instructor=request.user)

@register(Answer, site=employer_admin_site)
class AnswerAdmin(admin.ModelAdmin):
    # Customize the fields displayed in the admin list view for answers
    list_display = ('text', 'correct', 'question', 'created')
    
    def get_queryset(self, request):
        # Filter queryset to show only the courses created by the logged-in employer
        qs = super().get_queryset(request)
        if request.user.is_employer:
            return qs
        else:
            return qs.filter(instructor=request.user)

@register(Result, site=employer_admin_site)
class ResultAdmin(admin.ModelAdmin):
    # Customize the fields displayed in the admin list view for results
    list_display = ('quiz', 'user', 'score', 'completion_time', 'created', 'started')
    
    def get_queryset(self, request):
        # Filter queryset to show only the courses created by the logged-in employer
        qs = super().get_queryset(request)
        if request.user.is_employer:
            return qs
        else:
            return qs.filter(instructor=request.user)

@register(Event, site=employer_admin_site)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'start', 'end')
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_employer:
            return qs
        else:
            return qs.filter(instructor=request.user)