from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login

# User Registration
def register(request):
    if request.method == "POST":
        import json
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            confirm_password = data.get('confirm_password')

            # Check if all fields are provided
            if not username or not password or not confirm_password:
                return JsonResponse({'error': 'All fields are required!'}, status=400)

            # Check if passwords match
            if password != confirm_password:
                return JsonResponse({'error': 'Passwords do not match!'}, status=400)

            # Check if username already exists
            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'Username already exists!'}, status=400)

            # Create a new user
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return JsonResponse({'message': 'Registration successful!'}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format!'}, status=400)

    return JsonResponse({'error': 'Invalid request method!'}, status=405)


# User Login
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Validate input
        if not username or not password:
            return JsonResponse({'error': 'Both username and password are required!'}, status=400)

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Log the user in
            return JsonResponse({'message': f"Welcome, {user.username}!"}, status=200)
        else:
            return JsonResponse({'error': 'Invalid username or password!'}, status=401)

    return JsonResponse({'error': 'Invalid request method. Use POST.'}, status=400)
