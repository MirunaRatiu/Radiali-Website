# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import User

# User Registration
def register(request):
    if request.method == "POST":
        import json
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            confirm_password = data.get('confirm_password')
# def register(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

            # Check if all fields are provided
            if not username or not password or not confirm_password:
                return JsonResponse({'error': 'All fields are required!'}, status=400)

            # Check if passwords match
            if password != confirm_password:
                return JsonResponse({'error': 'Passwords do not match!'}, status=400)

            # Check if username already exists
            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'Username already exists!'}, status=400)
#         # Check if username or email already exists
#         if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
#             return HttpResponse("User already exists!")

            # Create a new user
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return JsonResponse({'message': 'Registration successful!'}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format!'}, status=400)

    return JsonResponse({'error': 'Invalid request method!'}, status=405)
#         # Create a new user
#         user = User(username=username, email=email, password=password)
#         user.save()
#         return HttpResponse("Registration successful!")
    
#     return render(request, 'register.html')


# User Login
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
# def login(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')

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
#         try:
#             user = User.objects.get(username=username, password=password)
#             return HttpResponse(f"Welcome, {user.username}!")
#         except User.DoesNotExist:
#             return HttpResponse("Invalid username or password!")

#     return render(request, 'login.html')