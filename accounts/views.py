from django.contrib.auth.models import User
from django.contrib.auth import autheticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

#User Registration View
@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error':'Username already exists'}, status=400)

        user = User.objects.create_user(username=username, password=password)
        return JsonResponse({'message': 'User registered successfully'}, status=201)


#User Login View
@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = autheticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'}, status=200)
        return JsonResponse({'error': 'Invalid credentials'}, status=400)
    

#User Logout View
def user_logout(request):
    logout(request)
    return JsonResponse({'message': 'Logout successful'}, status=200)