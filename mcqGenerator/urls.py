from django.urls import path
from .views import *

urlpatterns = [
    path('generate-quiz-home/', genQuizHome, name='generate-quiz-home'),
    path('quizGenPage/', quizGenPage, name='quizGenPage'),
]