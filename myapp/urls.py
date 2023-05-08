from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('employee-home/', views.employeeHome, name='employee_home'),
    path('employer-home/', views.employerHome, name='employer_home'),
    path('employee-signup/', views.employeeSignupPage, name='employee_signup'),
    path('employer-signup/', views.employerSignupPage, name='employer_signup'),
]