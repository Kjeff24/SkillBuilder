from django.urls import path
from .views import authentication_page, front_page, users_page

urlpatterns = [
    path('', front_page.home, name='home'),
    path('about/', front_page.about, name='about'),
    path('contact/', front_page.contact, name='contact'),
    path('login/', authentication_page.loginPage, name='login'),
    path('logout/', authentication_page.logoutUser, name='logout'),
    path('employee_home/<str:pk>/', users_page.employeeHome, name='employee-home'),
    path('employer_home/<str:pk>/', users_page.employerHome, name='employer-home'),
    path('employee_signup/', authentication_page.employeeSignupPage, name='employee-signup'),
    path('employer_signup/', authentication_page.employerSignupPage, name='employer-signup'),
]