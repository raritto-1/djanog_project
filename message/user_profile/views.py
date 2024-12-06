from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.http import HttpResponse

# Login Page View
# def login_page(request):
#     """Handle user login logic."""
#     if request.user.is_authenticated:
#         return redirect('profile_page')  # Redirect logged-in users to the profile page

#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         # Authentication logic
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'Login successful!')
#             # return redirect('profile_page')
#             return HttpResponse('you are write')  # Redirect to profile page
#         else:
#             # Check if the username exists
#             if User.objects.filter(username=username).exists():
#                 messages.error(request, 'Invalid password. Please try again.')
#             else:
#                 messages.error(request, 'No user found with that username. Please register first.')

#     return render(request, 'login.html')

def login_page(request):
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user = authenticate(request, username=username, password=password)

    #     if user is not None:
    #         login(request, user)
    #         return redirect('profile_page')
    #     else:
            
    #         if User.objects.filter(username=username).exists():
    #             messages.error(request, 'Invalid password. Please try again.')
    #         else:
    #             messages.error(request, 'No user found with that username. Please register first.')

    return render(request, 'login_page.html')

# Registration Page View
def register_page(request):
    """Handle user registration logic."""
    if request.method == 'POST':
        username = request.POST.get('username')
        email_address = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validation checks
        if not all([username, email_address, password, confirm_password]):
            messages.error(request, 'All fields are required.')
        elif password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        elif User.objects.filter(email=email_address).exists():
            messages.error(request, 'Email is already in use.')
        else:
            # Create and save the new user
            user = User.objects.create_user(username=username, password=password, email=email_address)
            user.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')  # Redirect to login page after registration

    return render(request, 'register.html')


# Profile Page View
@login_required
def profile_page(request):
    """Render the profile page for logged-in users."""
    # Ensure that the UserProfile model is related to User and exists
    user_profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'profile.html', {'user_profile': user_profile})


# Home Page View
@login_required
def home(request):
    return render(request, 'base.html')


# Logout View
@login_required
def log_out(request):
    """Log out the user and redirect to login page."""
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')  # Redirect to login page after logging out

