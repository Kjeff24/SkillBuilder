from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import JsonResponse
from .models import Quiz, Question, Answer, Result
from course.models import Course
from django.contrib import messages
from django.http import Http404
from django.db.models import Subquery


def quiz_list_view(request, pk2):
    course = Course.objects.get(id=pk2)
    quizzes = Quiz.objects.filter(course=course)
    
    # Exclude quizzes that already exist in the Result model for the current user
    user_results = Result.objects.filter(user=request.user)
    quizzes = Quiz.objects.filter(course=course).exclude(id__in=Subquery(user_results.values('quiz_id')))
    
    filtered_quizzes = []
    for quiz in quizzes:
        if quiz.question_set.exists():  # Check if the quiz has questions
            filtered_quizzes.append(quiz)
    
    context = {
        'quizzes': filtered_quizzes,
        'course': course,
    }
    
    return render(request, 'quiz/main.html', context)


def quiz_view(request, pk, pk2):
    quiz = Quiz.objects.get(pk=pk)
    course = Course.objects.get(id=pk2)
    
    Result.objects.create(quiz=quiz, user=request.user, started=True)
    
    context = {'obj': quiz, 'course': course, 'page':'quiz_page' }
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
        
        save_result = Result.objects.get(user=user)
        save_result.score=score_
        save_result.completion_time=completionTime
        save_result.save()

        if score_ >= quiz.required_score_to_pass:
            return JsonResponse({'passed': True, 'score': score_, 'results': results})
        else:
            return JsonResponse({'passed': False, 'score': score_, 'results': results})