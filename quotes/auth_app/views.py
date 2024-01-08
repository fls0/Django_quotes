from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import RegisterForm, LoginForm


def signupuser(request): 
    if request.user.is_authenticated:
        return redirect(to="quotesapp:quotes")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotesapp:quotes")
        else:
            return render(request, "auth_app/register.html", context={"form": form})
    return render(request, "auth_app/register.html", context={"form": RegisterForm()})


def loginuser(request):
    if request.user.is_authenticated:
        return redirect(to="quotesapp:quotes")
    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"], password=request.POST["password"]
        )
        if user is None:
            messages.error(request, "Username or password didn't match")
            return redirect(to="auth_app:login")
        login(request, user)
        return redirect(to="quotesapp:quotes")
    return render(request, "auth_app/login.html", context={"form": LoginForm()})


@login_required
def logoutuser(request):
    logout(request)
    return redirect(to="quotesapp:quotes")