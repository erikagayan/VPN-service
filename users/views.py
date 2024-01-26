from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User
from users.forms import UserRegisterForm, UserEditForm, PasswordChangingForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {"form": form})


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "dashboard.html")


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
            else:
                messages.error(request, "Error")
        else:
            messages.error(request, "Error")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def stats_view(request):
    data = User.objects.all()
    return render(request, "information.html", {"data": data})


@login_required
def edit_user(request):
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("information")
    else:
        form = UserEditForm(instance=request.user)
    return render(request, "edit_user.html", {"form": form})


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangingForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("information")
    else:
        form = PasswordChangingForm(user=request.user)
    return render(request, "change_password.html", {"form": form})
