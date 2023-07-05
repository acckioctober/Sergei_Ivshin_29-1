from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm


class RegisterUserCBV(CreateView):
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('pastries')

    def form_invalid(self, form):
        username = form.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            form.add_error('username', 'Пользователь с таким именем уже существует')
        return super().form_invalid(form)

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response


class UserLoginCBV(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    authentication_form = AuthenticationForm

    def get_success_url(self):
        return reverse_lazy('pastries')

    def form_invalid(self, form):
        form.add_error(None, 'Неправильное имя пользователя или пароль')
        return self.render_to_response(self.get_context_data(form=form))


class UserLogoutCBV(LogoutView):
    next_page = reverse_lazy('pastries')
