from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse
from .models import Quiz, Question, Answer, Result
from course.models import Course
import json

class QuizListView(ListView):
    model = Quiz 
    template_name = 'quiz/main.html'
    
    # Get Quizzes based on the course_id
    def get_queryset(self):
        course_id = self.kwargs.get('pk2') 
        if course_id:
            course = Course.objects.get(id=course_id)
            queryset = Quiz.objects.filter(course=course)
        else:
            queryset = Quiz.objects.all()
        return queryset

def quiz_view(request, pk, pk2):
    quiz = Quiz.objects.get(pk=pk)
    course = Course.objects.get(id=pk2)
    # quiz = Quiz.objects.filter(course=course)
    
    context = {
        'obj': quiz,
        'course': course
    }
    return render(request, 'quiz/quiz.html', context)

def quiz_data_view(request, pk, pk2):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })

# def save_quiz_view(request, pk, pk2):
#     if request.is_ajax():
#         questions = []
#         data = request.POST
#         data_ = dict(data.lists())

#         data_.pop('csrfmiddlewaretoken')

#         for k in data_.keys():
#             print('key: ', k)
#             question = Question.objects.get(text=k)
#             questions.append(question)
#         print(questions)

#         user = request.user
#         quiz = Quiz.objects.get(pk=pk)

#         score = 0
#         multiplier = 100 / quiz.number_of_questions
#         results = []
#         correct_answer = None

#         for q in questions:
#             a_selected = request.POST.get(q.text)

#             if a_selected != "":
#                 question_answers = Answer.objects.filter(question=q)
#                 for a in question_answers:
#                     if a_selected == a.text:
#                         if a.correct:
#                             score += 1
#                             correct_answer = a.text
#                     else:
#                         if a.correct:
#                             correct_answer = a.text

#                 results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
#             else:
#                 results.append({str(q): 'not answered'})
            
#         score_ = score * multiplier
#         Result.objects.create(quiz=quiz, user=user, score=score_)

#         if score_ >= quiz.required_score_to_pass:
#             return JsonResponse({'passed': True, 'score': score_, 'results': results})
#         else:
#             return JsonResponse({'passed': False, 'score': score_, 'results': results})


def save_quiz_view(request, pk, pk2):
    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        questions = []
        data = request.POST
        print(request.POST)
        data_ = dict(data.lists())
        
        # save completion time from response data
        completionTime = float(data_["completionTime"][0])
        print(f" Time take to complete {completionTime}")

        # remove csrfmiddlewaretoken and completionTime, and returns the list of questions
        data_.pop('csrfmiddlewaretoken')
        data_.pop('completionTime')

        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(text=k)
            questions.append(question)
        print(questions)

        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        score = 0
        multiplier = 100 / quiz.number_of_questions
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.text)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text

                results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                results.append({str(q): 'not answered'})
            
        score_ = score * multiplier
        Result.objects.create(quiz=quiz, user=user, score=score_, completion_time=completionTime)

        if score_ >= quiz.required_score_to_pass:
            return JsonResponse({'passed': True, 'score': score_, 'results': results})
        else:
            return JsonResponse({'passed': False, 'score': score_, 'results': results})