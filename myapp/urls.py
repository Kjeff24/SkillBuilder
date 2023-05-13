from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('employee_home/<str:pk>/', views.employeeHome, name='employee-home'),
    path('employer_home/<str:pk>/', views.employerHome, name='employer-home'),
    path('employee_signup/', views.employeeSignupPage, name='employee-signup'),
    path('employer_signup/', views.employerSignupPage, name='employer-signup'),
    path('employer_home/<str:pk>/create_room/', views.createRoom, name='create-room'),
    path('employer_home/<str:pk>/create_course/', views.createCourse, name='create-course'),
    path('employer_home/<str:pk>/create_announcement/', views.createAnnoucement, name='create-announcement'),
    path('employer_home/<str:pk>/create_resource/', views.createResource, name='create-resource'),
]