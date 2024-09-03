from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def login_1(request):
#     print("login page entered")
#     return render (request,"login.html")
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm  # Assuming you've created this form for your CustomUser model
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

# # Define valid credentials
VALID_USERS = [
    {'username': 'arpitha_2004', 'password': 'arpi$2004'},
    {'username': 'john', 'password': 'john123'},  # Add other users here
]

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        # Collect the username and password from the form
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("username------",username,"")
        # Check if the username and password match any in the VALID_USERS list
        valid_user = next((user for user in VALID_USERS if user['username'] == username and user['password'] == password), None)
        
        if valid_user:
            print("hiii---------")
            # If valid, render the mainpage
            return render(request, 'mainpage.html')
        else:
            # If invalid, render the login page with an error message
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    # Render the login page for GET requests
    return render(request, 'login.html')









# from django.shortcuts import render
# from django.utils import timezone
# from datetime import datetime

# # Define valid credentials
# VALID_USERS = [
#     {'username': 'arpitha_2004', 'password': 'arpi$2004'},
#     {'username': 'john', 'password': 'john123'},  # Add other users here
# ]

# @csrf_exempt
# def login_view(request):
#     # Get the current date and time
#     current_datetime = timezone.now()

#     # Define the allowed login date
#     allowed_login_date = datetime(2024, 10, 9, 0, 0, 0)  # October 9, 2024, 12:00 AM

#     # Convert allowed_login_date to timezone-aware datetime
#     allowed_login_date = timezone.make_aware(allowed_login_date, timezone.get_current_timezone())

#     # Check if the current date and time are before the allowed login date
#     if current_datetime < allowed_login_date:
#         # If before the allowed date, show a message
#         return render(request, 'login.html', {'error': f'Please wait for the date. The login will be available starting from October 9, 2024, 12:00 AM.'})
    
#     # If it's the allowed date or after, proceed with the login logic
#     if request.method == 'POST':
#         # Collect the username and password from the form
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print("username------", username)
#         # Check if the username and password match any in the VALID_USERS list
#         valid_user = next((user for user in VALID_USERS if user['username'] == username and user['password'] == password), None)
        
#         if valid_user:
#             print("hiii---------")
#             # If valid, render the mainpage
#             return render(request, 'mainpage.html')
#         else:
#             # If invalid, render the login page with an error message
#             return render(request, 'login.html', {'error': 'Invalid credentials'})

#     # Render the login page for GET requests
#     return render(request, 'login.html')
