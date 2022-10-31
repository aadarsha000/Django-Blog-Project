from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .form import ProfileUpdateForm
from .models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.

def register_newUser(request):
    context = {}
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("account:login")
        else:
            context['form'] = form
    else:
        form = UserCreationForm()
        context['form'] = form
    return render(request, 'account/register.html', context)

def login_user(request):
    context={}
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('blog:home')
            else:
                messages.error(request, "Invalid username or password.")
                print("Invalid username or password 1.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    context['form']=form
    return render(request, 'account/login.html', context)

def logout_user(request):
    logout(request)
    return redirect("blog:home")


@login_required(login_url='/account/login')
def profileUpdate(request):
    context = {}
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("blog:home")
        else:
            form=ProfileUpdateForm(instance=request.user.profile)
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
        context['form'] = form
    return render(request, 'account/profile.html', context)


@login_required(login_url='/account/login')
def userprofile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'account/userprofile.html', {'profile':profile})
