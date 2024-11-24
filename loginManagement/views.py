from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if username or email already exists
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return HttpResponse("User already exists!")

        # Create a new user
        user = User(username=username, email=email, password=password)
        user.save()
        return HttpResponse("Registration successful!")
    
    return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username, password=password)
            return HttpResponse(f"Welcome, {user.username}!")
        except User.DoesNotExist:
            return HttpResponse("Invalid username or password!")

    return render(request, 'login.html')