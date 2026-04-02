from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser

def login_view(request):
    if request.method == 'POST':
        login_input = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user_obj = CustomUser.objects.get(email=login_input)
            auth_username = user_obj.username
        except CustomUser.DoesNotExist:
            auth_username = login_input

        user = authenticate(request, username=auth_username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            if user.is_admin:
                return redirect('dashboard') # or specific admin dashboard
            elif user.is_teacher:
                return redirect('dashboard')
            elif user.is_student:
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid user role')
                return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'authentication/login.html')
    return render(request, 'authentication/login.html')

def register_view(request):
    if request.method == 'POST':
        # logic for register (simplified)
        messages.success(request, 'Signup successful!')
        return redirect('index')
    return render(request, 'authentication/register.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('index')

def forgot_password_view(request):
    return render(request, 'authentication/forgot-password.html')
