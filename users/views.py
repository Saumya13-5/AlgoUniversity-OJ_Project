import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from Problemset.models import Problem  # Import the Problem model

def welcome_view(request):
    return render(request, 'users/welcome.html')

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return JsonResponse({'success': False, 'message': 'All fields are required.'}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'success': False, 'message': 'Username already exists.'}, status=409)
        
        if User.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'message': 'Email address already registered.'}, status=409)

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return JsonResponse({'success': True})
    
    return render(request, 'users/register.html')

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return JsonResponse({'success': False, 'message': 'Username and password are required.'}, status=400)

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'redirect_url': '/dashboard/'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid username or password.'}, status=401)
    
    return render(request, 'users/login.html')

@login_required

def dashboard_view(request):
   problems = Problem.objects.all()  # Get all problems from the database
   return render(request, 'users/dashboard.html', {'questions': problems})
