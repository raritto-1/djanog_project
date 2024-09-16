from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def recipes(request):
    if request.method == "POST":
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')

        # Create a new recipe
        Recipe.objects.create(
            recipe_image=recipe_image,
            recipe_name=recipe_name,
            recipe_description=recipe_description
        )

        # Redirect to the recipes page to avoid resubmission on refresh
        return redirect('recipes')

    # Get all recipes to display
    all_recipes = Recipe.objects.all()
    context = {'recipes': all_recipes}
    return render(request, 'recipes.html', context)

@login_required
def delete_recipe(request, recipe_id):
    # Get the recipe or 404 if not found
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.delete()
    # Redirect to the recipes page after deletion
    return redirect('recipes')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('recipes')
        else:
            # Provide appropriate error messages
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Invalid password. Please try again.')
            else:
                messages.error(request, 'No user found with that username. Please register first.')

    return render(request, 'login.html')

def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email_address = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate the registration form
        if not username or not email_address or not password or not confirm_password:
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
            return redirect('login')

    return render(request, 'register.html')

def log_out(request):
    # Log the user out and redirect to login page
    logout(request)
    return redirect('login')
