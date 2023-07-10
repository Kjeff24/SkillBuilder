from django.urls import path
from .views import predict

urlpatterns = [
    path('<str:pk>/predict/', predict, name='predict'),
    path('<str:pk>/about/predict/', predict, name='predict'),
    path('<str:pk>/contact/predict/', predict, name='predict'),
]