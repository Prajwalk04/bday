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
        username = request.POST.get('username')
        password = request.POST.get('password')
        valid_user = next((user for user in VALID_USERS if user['username'] == username and user['password'] == password), None)
        
        if valid_user:
            return render(request, 'mainpage.html')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    # Render the login page for GET requests
    return render(request, 'login.html')
                 





# # Define valid credentials
# VALID_USERS = [
#     {'username': 'arpitha_2004', 'password': 'arpi$2004'},
#     {'username': 'john', 'password': 'john123'},  # Add other users here
# ]
# from django.utils import timezone
# from datetime import datetime  # This is the correct import
# from django.utils import timezone
# from datetime import datetime
# from django.utils import timezone
# from datetime import datetime, timezone as dt_timezone  # Importing timezone from datetime
# from django.utils import timezone
# from datetime import datetime

# def login_view(request):
#     # Get the current date and time (timezone-aware)
#     current_datetime = timezone.now()

#     # Print current datetime for debugging
#     print("Current datetime (server time, timezone-aware):", current_datetime)

#     # Define the allowed login date (test with today's date and the specific time)
#     # Example: Test with today's date and the time you want
#     allowed_login_date = datetime(2024, 9, 17, 22, 2, 0)  # Set to 9:49 PM for testing

#     # Convert allowed_login_date to a timezone-aware datetime (in server's timezone)
#     allowed_login_date_aware = timezone.make_aware(allowed_login_date, timezone.get_current_timezone())

#     # Print allowed login date for debugging
#     print("Allowed login date (timezone-aware):", allowed_login_date_aware)

#     # Check if the current date and time is before the allowed login date
#     if current_datetime < allowed_login_date_aware:
#         # Print message for debugging
#         print("Login is not allowed yet!")
#         # If before the allowed date, show a message
#         return render(request, 'login.html', {'error': f'Please wait for the date. The login will be available starting from {allowed_login_date_aware}.'})
    
#     # If it's the allowed date or after, proceed with the login logic
#     if request.method == 'POST':
#         # Collect the username and password from the form
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         # Print collected username and password for debugging
#         print("Username:", username)
#         print("Password:", password)

#         # Check if the username and password match any in the VALID_USERS list
#         valid_user = next((user for user in VALID_USERS if user['username'] == username and user['password'] == password), None)
        
#         if valid_user:
#             # Print success message for debugging
#             print("Login successful!")
#             # If valid, render the main page
#             return render(request, 'mainpage.html')
#         else:
#             # Print failure message for debugging
#             print("Invalid credentials!")
#             # If invalid, render the login page with an error message
#             return render(request, 'login.html', {'error': 'Invalid credentials'})

#     # Render the login page for GET requests
#     return render(request, 'login.html')
