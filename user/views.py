from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from user.forms import UserCreation, UserUpdate, ProfileUpdate, UserLogin


def log_in(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hello {username} You Logged In!")
            return redirect('dashboard')
    form = UserCreation()
    return render(request, 'login.html', {'form': form})


def dashboard(request):
    return render(request, "dashboard.html")


def register(request):
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hello {username} Your Account Has Been Created!")
            return redirect('login')
    form = UserCreation()
    return render(request, 'registration.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdate(request.POST, instance=request.user)
        p_form = ProfileUpdate(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your Account Has Been Updated!")
            return redirect('profile')

    else:
        u_form = UserUpdate(instance=request.user)
        p_form = ProfileUpdate(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)
