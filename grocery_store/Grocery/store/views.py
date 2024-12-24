from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, Product, Order
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import ProfileForm, ImagePostForm
from django.http import HttpResponse

# Profile view
@login_required
def profile(request):
    return render(request, "profile.html", {"user": request.user})

# Edit profile view
@login_required
def edit_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "edit_profile.html", {'form': form})

# Home page view
def home(request):
    return render(request, 'home.html')

# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "login.html")

# Register view
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email_address = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get("confirm_password")

        if not username or not email_address or not password or not confirm_password:
            messages.error(request, "All fields are required")
        elif password != confirm_password:
            messages.error(request, "Both passwords must be the same")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        elif User.objects.filter(email=email_address).exists():
            messages.error(request, "Email already exists")
        else:
            user = User.objects.create_user(username=username, password=password, email=email_address)
            user.save()
            messages.success(request, 'Registration successful. Please login.')
            return redirect("login_view")
    return render(request, "register.html")

# Logout view
def user_logout(request):
    logout(request)
    return redirect("login_view")

# Dashboard view
@login_required
def dashboard(request):
    if request.method == "POST":
        form = ImagePostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "dashboard.html", {"form": form, "obj": form.instance})
    else:
        form = ImagePostForm()
    return render(request, "dashboard.html", {'form': form})

# Add product to cart
@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart.quantity += 1
        cart.save()
    return redirect('cart')

# View cart
@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

# Remove item from cart
@login_required
def remove_from_cart(request, cart_id):
    cart_item = Cart.objects.get(id=cart_id)
    cart_item.delete()
    return redirect('cart')

# Place order
@login_required
def place_order(request):
    cart_items = Cart.objects.filter(user=request.user)
    if cart_items:
        for item in cart_items:
            Order.objects.create(user=request.user, product=item.product, quantity=item.quantity)
            item.delete()
        return redirect('order_summary')
    return HttpResponse("Your cart is empty.")

# Order summary page
@login_required
def order_summary(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order.html', {'orders': orders})
