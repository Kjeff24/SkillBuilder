from django.contrib import admin
from django.db.models import Max
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
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Filter the users and rooms displayed in the user and room fields to show only those created by the logged-in admin
        if db_field.name == 'user':
            kwargs['queryset'] = User.objects.filter(my_employer=request.user)
        elif db_field.name == 'room':
            kwargs['queryset'] = Room.objects.filter(course__instructor=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



@register(Course, site=employer_admin_site)
class CourseAdmin(admin.ModelAdmin):
    inlines = [ParticipantsInline]
    # Customize the fields displayed in the admin list view for courses
    list_display = ('name', 'instructor', 'created', 'updated')
    
    def get_queryset(self, request):
        # Filter queryset to show only the courses created by the logged-in employer
        qs = super().get_queryset(request)
        if request.user.is_employer:
            return qs.filter(instructor=request.user)
        else:
            return qs
        
    def save_model(self, request, obj, form, change):
        # Set the currently logged-in user as the instructor for new courses
        if not change:
            obj.instructor = request.user
        super().save_model(request, obj, form, change)
        
    def get_form(self, request, obj=None, **kwargs):
        # Remove the instructor field from the form
        form = super().get_form(request, obj, **kwargs)
        form.base_fields.pop('instructor', None)  # Remove the field if it exists
        return form
    
    
@register(Participants, site=employer_admin_site)
class ParticipantsAdmin(admin.ModelAdmin):
    # Customize the fields displayed in the admin list view for participants
    list_display = ('user', 'course')
    
    def get_queryset(self, request):
        # Filter queryset to show only the courses created by the logged-in employer
        qs = super().get_queryset(request)
        if request.user.is_employer:
            return qs.filter(course__instructor=request.user)
        else:
            return qs
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "course":
            kwargs["queryset"] = Course.objects.filter(instructor=request.user)
        elif db_field.name == "room":
            kwargs["queryset"] = Room.objects.filter(course__instructor=request.user)
        elif db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(my_employer=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@register(Resource, site=employer_admin_site)
class ResourceAdmin(admin.ModelAdmin):
    # Customize the fields displayed in the admin list view for resources
    list_display = ('name', 'course', 'created', 'updated')
    
    def get_queryset(self, request):
        # Filter queryset to show only the courses created by the logged-in employer
        qs = super().get_queryset(request)
        if request.user.is_employer:
            return qs.filter(course__instructor=request.user)
        else:
            return qs
        
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "course":
            kwargs["queryset"] = Course.objects.filter(instructor=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@register(Announcement, site=employer_admin_site)
class AnnouncementAdmin(admin.ModelAdmin):
    # Customize the fields displayed in the admin list view for announcements
    list_display = ('title', 'course', 'date', 'created', 'updated')
    
    def get_queryset(self, request):
        # Filter queryset to show only the courses created by the logged-in employer
        qs = super().get_queryset(request)
        if request.user.is_employer:
            return qs.filter(course__instructor=request.user)
        else:
            return qs
        
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "course":
            kwargs["queryset"] = Course.objects.filter(instructor=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@register(Room, site=employer_admin_site)
class RoomAdmin(admin.ModelAdmin):
    # Customize the fields displayed in the admin list view for rooms
    list_display = ('room_topic', 'course', 'created', 'updated')
    
    def get_queryset(self, request):
        # Filter queryset to show only the courses created by the logged-in employer
        qs = super().get_queryset(request)
        if request.user.is_employer:
            return qs.filter(course__instructor=request.user)
        else:
            return qs
        
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "course":
            kwargs["queryset"] = Course.objects.filter(instructor=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


# Quiz 

@register(Quiz, site=employer_admin_site)
class QuizAdmin(admin.ModelAdmin):
    # Customize the fields displayed in the admin list view for quizzes
    list_display = ('name', 'course', 'number_of_questions', 'time', 'required_score_to_pass', 'difficluty')
    
    def get_queryset(self, request):
        # Filter queryset to show only the courses created by the logged-in employer
        qs = super().get_queryset(request)
        if request.user.is_employer:
            return qs.filter(course__instructor=request.user)
        else:
            return qs
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "course":
            kwargs["queryset"] = Course.objects.filter(instructor=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

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
            return qs.filter(quiz__course__instructor=request.user)
        else:
            return qs
        
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "quiz":
            kwargs["queryset"] = Quiz.objects.filter(course__instructor=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@register(Result, site=employer_admin_site)
class ResultAdmin(admin.ModelAdmin):
    # Customize the fields displayed in the admin list view for results
    list_display = ('quiz', 'user', 'score', 'quiz_highest_score', 'completion_time', 'created')
        
    def quiz_highest_score(self, obj):
        quiz_highest_score = Result.objects.filter(quiz=obj.quiz, user=obj.user).aggregate(Max('score'))['score__max']
        if obj.score == quiz_highest_score:
            return quiz_highest_score
        else:
            return ''
    quiz_highest_score.short_description = 'User Highest Score'
    
    def get_queryset(self, request):
        # Filter queryset to show only the courses created by the logged-in employer
        qs = super().get_queryset(request)
        if request.user.is_employer:
            return qs.filter(quiz__course__instructor=request.user)
        else:
            return qs
        
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "quiz":
            kwargs["queryset"] = Quiz.objects.filter(course__instructor=request.user)
        elif db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(my_employer=request.user) 
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
            

@register(Event, site=employer_admin_site)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'start', 'end')
    
    def get_queryset(self, request):
        # Filter queryset to show only the courses created by the logged-in employer
        qs = super().get_queryset(request)
        if request.user.is_employer:
            return qs.filter(course__instructor=request.user)
        else:
            return qs
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "course":
            kwargs["queryset"] = Course.objects.filter(instructor=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)