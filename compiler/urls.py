from django.urls import path
from . import views

urlpatterns = [
    path('', views.compile_code, name='compile_code'),
]
