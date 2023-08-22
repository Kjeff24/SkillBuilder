from django.contrib import admin
from .models import Question, Answer, Quiz, Result


# Display answers in tabular format in question
class AnswerInline(admin.TabularInline):
    """
    Admin inline class for displaying answers in tabular format within a question.
    """
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    """
    Admin model class for configuring the display of Question model in the admin interface.
    """
    inlines = [AnswerInline]


# Register your models here.
admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Answer)
admin.site.register(Result)