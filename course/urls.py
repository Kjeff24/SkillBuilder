from django.urls import path
from .views import course_management, resource_management, room_management, announcement_management
from .views import announcement_page, course_page, resource_page, room_page
from .views import chat_room, user_management, quiz_page


urlpatterns = [
    path('employer_home/<str:pk>/create_room/', room_management.createRoom, name='create-room'),
    path('employer_home/<str:pk>/create_course/', course_management.createCourse, name='create-course'),
    path('employer_home/<str:pk>/create_announcement/', announcement_management.createAnnoucement, name='create-announcement'),
    path('employer_home/<str:pk>/create_resource/', resource_management.createResource, name='create-resource'),
    path('update_course/<str:pk>/', course_management.updateCourse, name='update-course'),
    path('update_resource/<str:pk>/', resource_management.updateResource, name='update-resource'),
    path('update_announcement/<str:pk>/', announcement_management.updateAnnouncement, name='update-announcement'),
    path('update_room/<str:pk>/', room_management.updateRoom, name='update-room'),
    path('delete_course/<str:pk>/', course_management.deleteCourse, name='delete-course'),
    path('delete_announcement/<str:pk>/', announcement_management.deleteAnnouncement, name='delete-announcement'),
    path('delete_resource/<str:pk>/', resource_management.deleteResource, name='delete-resource'),
    path('delete_room/<str:pk>/', room_management.deleteRoom, name='delete-room'),
    path('course/<str:pk>/', course_page.coursePage, name='course'),
    path('course/<str:pk>/resource', resource_page.resourcePage, name='resource'),
    path('course/<str:pk>/announcement', announcement_page.announcementPage, name='announcement'),
    path('course/<str:pk>/chat_room', room_page.roomPage, name='room-page'),
    path('course/<str:pk>/quiz_page', quiz_page.quizPage, name='quiz-page'),
    path('course/<str:pk2>/chat_room/<str:pk>/', chat_room.chatRoom, name='chat-room'),
    path('update_user/<str:pk>/', user_management.updateUser, name='update-user'),
]