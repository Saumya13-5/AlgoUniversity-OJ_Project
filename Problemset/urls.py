# problems/urls.py
from django.urls import path
from . import views

urlpatterns = [
     path('problem/<int:problem_id>/', views.problem_detail, name='problem_detail'),
]