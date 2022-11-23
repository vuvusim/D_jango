from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required
from . forms import UserUpdateForm, ProfileUpdateForm

User = get_user_model()

@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        error = False
        if not username or User.objects.filter(username=username).first():
            messages.error(request, 'Username not enetered or username already exists.')
            error = True
        if not email or User.objects.filter(email=email).first():
            messages.error(request, 'Email not enterd or user with this email already exist')
            error = True
        else:
            try:
                validate_email(email)
            except:
                messages.error(request, 'Invalid email')
                error = True
        if not password or not password2 or password != password2:
            messages.error(request, "Password not entered, or do not match")
            error = True
        if not error:
            new_user = User.objects.create(username=username, email=email, password=password)
            messages.success(request, f'User {username} registration successful. You can log in now')
            return redirect('login')

    return render(request, 'user_profile/register.html')

@login_required
def profile(request):
    return render(request, 'user_profile/profile.html')


@login_required
def update_profile(request):
    if request.method == "POST":
        user_form  = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f"User {request.user.username} profile updated.")
            return redirect('profile')
    else:
        user_form  = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    return render(request, 'user_profile/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })