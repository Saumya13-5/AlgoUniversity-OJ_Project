from django.urls import path
from .views import compile_code

urlpatterns = [
    path('run_code/', compile_code, name='compile_code'),
]
