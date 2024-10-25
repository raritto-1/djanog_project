from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import FinanceData
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def calculator(request):
    if request.method == "POST":
        date = request.POST.get('date')
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        description = request.POST.get('description')

        try:
            FinanceData.objects.create(
                date=date,
                amount=amount,
                category=category,
                description=description
            )
            messages.success(request, 'Transaction added successfully.')
            return redirect('calculator')  # optional if any one stay on the same page change to main.py
        except Exception as e:
            messages.error(request, 'Error adding transaction: {}'.format(e))

    return render(request, 'main.html')

def transaction_history(request):
    transactions = FinanceData.objects.all().order_by('-date')
    
    total_income = FinanceData.objects.filter(category='Income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expenses = FinanceData.objects.filter(category='Expense').aggregate(Sum('amount'))['amount__sum'] or 0
    
    total_remaining = total_income - total_expenses
    total_days = transactions.values('date').distinct().count()

    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'total_remaining': total_remaining,
        'total_days': total_days,
    }
    
    return render(request, 'history.html', context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            
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
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')
