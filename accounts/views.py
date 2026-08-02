from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]

            if User.objects.filter(username=username).exists():
                messages.error(request, "User already exists. Please login.")
                return redirect("login")

            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            Profile.objects.create(user=user)

            messages.success(request, "Registration Successful. Please Login.")
            return redirect("login")

    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})




def user_login(request):
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check whether the username exists
        if not User.objects.filter(username=username).exists():
            messages.error(request, "User not registered. Please register first.")
            return redirect("register")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful.")
            return redirect("home")

        else:
            messages.error(request, "Incorrect password.")

    return render(request, "accounts/login.html")


def user_logout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully.")
    return redirect("home")


def profile(request):
    return render(request, "accounts/profile.html")