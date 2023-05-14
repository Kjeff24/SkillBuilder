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
    path('course/<str:pk>/', views.coursePage, name='course'),
    path('update_course/<str:pk>/', views.updateCourse, name='update-course'),
    path('update_resource/<str:pk>/', views.updateResource, name='update-resource'),
    path('update_announcement/<str:pk>/', views.updateAnnouncement, name='update-announcement'),
    path('update_room/<str:pk>/', views.updateRoom, name='update-room'),
    path('delete_course/<str:pk>/', views.deleteCourse, name='delete-course'),
    path('delete_announcement/<str:pk>/', views.deleteAnnouncement, name='delete-announcement'),
    path('delete_resource/<str:pk>/', views.deleteResource, name='delete-resource'),
    path('delete_room/<str:pk>/', views.deleteRoom, name='delete-room'),
]