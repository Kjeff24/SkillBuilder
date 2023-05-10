from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('employee_home/', views.employeeHome, name='employee-home'),
    path('employer_home/', views.employerHome, name='employer-home'),
    path('employee_signup/', views.employeeSignupPage, name='employee-signup'),
    path('employer_signup/', views.employerSignupPage, name='employer-signup'),
    path('create_room/', views.createRoom, name='create-room'),
    path('create_course/', views.createCourse, name='create-course'),
    path('create_announcement/', views.createAnnoucement, name='create-announcement'),
    path('create_resource/', views.createResource, name='create-resource'),
]