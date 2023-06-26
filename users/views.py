from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User


def register_user_view(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "users/register.html", context={"form": form})
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confirm = form.cleaned_data["password_confirm"]
            if User.objects.filter(username=username).exists():
                form.add_error("username", "Пользователь с таким именем уже существует")
                return render(request, "users/register.html", context={"form": form})
            elif password == password_confirm:
                user = User.objects.create_user(username=username, password=password)
                login(request, user)
                return redirect("/pastries/")
            else:
                form.add_error("password_confirm", "Пароли не совпадают")
                return render(request, "users/register.html", context={"form": form})
        else:
            return render(request, "users/register.html", context={"form": form})


def login_user_view(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "users/login.html", context={"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/pastries/")
            else:
                form.add_error(None, "Неправильное имя пользователя или пароль")
                return render(request, "users/login.html", context={"form": form})
        else:
            return render(request, "users/login.html", context={"form": form})


def logout_user_view(request):
    logout(request)
    return redirect("/pastries/")