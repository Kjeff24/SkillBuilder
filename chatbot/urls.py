from django.urls import path
from .views import predict

urlpatterns = [
    path('<str:pk>/contact/predict/', predict, name='predict'),
]